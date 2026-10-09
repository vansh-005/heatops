# Domain, API, and persistence contracts

This is the contract to implement, not generated OpenAPI for an existing service. Use Pydantic models and generate TypeScript/OpenAPI after implementation; do not hand-maintain contradictory types.

## Shared rules

IDs: opaque UUIDs except deterministic task and idempotency keys. Execution timestamps: RFC3339 UTC. Display/operational schedule: date plus `Asia/Kolkata`; schedule blocks are half-open intervals `[start,end)`. Convert to aware datetimes in the backend. Counts are integers, hours are numeric; round percentages only in presentation.

Weather hourly points represent the following hour. Apply the documented synthetic step-value assumption when splitting a block into half-hour segments. No interpolation disguised as measured precision.

Every mutable entity has integer `version`. Commands carry `expectedVersion`; return 409 on conflict. Server derives actor identity and authorization. API errors contain `code`, `message`, `retryable`, `requestId`, and optional field errors. Never include tokens or stack traces.

## Core objects

| Object | Required fields and invariants |
|---|---|
| Site | id, orgId, version, name, coordinates, timezone, mode, crew definitions, task constraints, gateOpen, resource checks, policyId |
| ForecastSnapshot | id, sourceMode, fetchedAt, validDate, timezone, hourly values and units, attribution, policy-compatible variables; model/issue time only if provider supplies it |
| ScreeningPolicy | id, version, metric, threshold, provenance, validationStatus; demo policy is explicitly unvalidated |
| Run | id, siteId, sessionId, mode, status, attempt, leaseUntil, fence, input versions, dispatchStatus, startedAt, finishedAt, modelId, error |
| Candidate | id, schedule blocks, exposureWorkerHours, totalTaskWorkerHours, deferredTaskWorkerHours, remainingFlaggedBlocks, violations, feasible |
| Proposal | id, runId, revision, status, chosenCandidateId, immutable schedule, metric snapshot, explanation, unresolvedConditions, contentHash |
| CoordinationTask | id, proposalId, type, assigneeRole, status, dueAt, acknowledgedAt, readinessReport, completionEvidence, version |
| AuditEvent | runId, eventId, timestamp, actor, type, structured summary, toolCallId if applicable |

Run status: `QUEUED → RUNNING → AWAITING_APPROVAL | INSUFFICIENT_DATA | FAILED`. Approval changes AWAITING_APPROVAL to APPROVED. A proposal invalidated by a new site/forecast/policy version changes to SUPERSEDED; the replacement is a separate run with `supersedesRunId`. Preserve history.

Task state: `OPEN → ACKNOWLEDGED → COMPLETED`. Reject/blocked reports can set BLOCKED. Overdue is a derived flag for an incomplete task after dueAt; maintenance writes one escalation record per task/due version, not a duplicate status transition every minute. A receipt-only task may complete on acknowledgment. Readiness tasks require a structured readiness report and are labeled supervisor-reported.

`resolve_remaining_exposure` cannot be auto-completed. A defer/change decision updates site/task constraints and requires replanning; publishing coordination tasks alone never releases a task for hazardous work.

## Routes

| Method and path | Input | Output / behavior |
|---|---|---|
| GET /sites | authenticated organization | site summaries |
| GET /sites/{id} | id | full site and version |
| PATCH /sites/{id} | expectedVersion, allowlisted constraint changes | incremented site; pending proposals invalidated |
| POST /runs | siteId, sessionId, mode, idempotencyKey, optional supersedesRunId | 202 runId, status, dispatchStatus |
| GET /runs/{id} | id | run, proposal if present, current metrics |
| GET /runs/{id}/events | after cursor, limit ≤100 | ordered events, next cursor |
| POST /plans/{id}/approve | proposalHash, expectedRevision, idempotencyKey, acknowledgesUnresolvedConditions | approved plan + coordination tasks |
| POST /plans/{id}/reject | expectedRevision, reason | rejected proposal, no tasks |
| GET /tasks | siteId, bounded cursor | permitted tasks and overdue flags |
| POST /tasks/{id}/acknowledge | expectedVersion, idempotencyKey | receipt recorded; readiness unchanged |
| POST /tasks/{id}/report | expectedVersion, ready/blocked, note, idempotencyKey | structured supervisor report |
| POST /demo/sessions | fixtureId | isolated synthetic session; authenticated |
| POST /demo/sessions/{id}/advance-clock | expectedVersion, minutesForward | new demo time + due evaluation; synthetic only |
| GET /demo/replays/{id} | published replay id | public read-only sanitized capture |

Approval must fail with `STALE_INPUT` if site/forecast/policy versions no longer match, `STALE_PROPOSAL` for hash/revision mismatch, `NOT_APPROVABLE` for missing evidence or validation failure, and `FORBIDDEN` for wrong identity. Return the existing success on duplicate idempotent approval, not a second set of tasks.

## Suggested response shape

```json
{
  "runId": "example-run-id",
  "status": "AWAITING_APPROVAL",
  "sourceMode": "synthetic",
  "proposal": {
    "revision": 2,
    "status": "PROPOSED",
    "metrics": {
      "baselineFlaggedWorkerHours": 135,
      "proposedFlaggedWorkerHours": 60,
      "reductionWorkerHours": 75,
      "reductionPercent": 55.5555555556,
      "baselineTaskWorkerHours": 270,
      "proposedTaskWorkerHours": 270,
      "deferredTaskWorkerHours": 0
    },
    "unresolvedConditions": [
      "Crew A retains 15 flagged worker-hours",
      "Crew B retains 45 flagged worker-hours",
      "Drinking water availability is unconfirmed"
    ]
  }
}
```

Illustrative excerpt; implementation adds IDs, versions, source provenance, schedule, hash, and policy reference.

## DynamoDB access patterns

Single on-demand table, PK/SK. Prefix every organization-scoped record with the server-derived org. Demo session ID isolates resets; reset creates a fresh session rather than deleting global data.

| Entity | PK | SK |
|---|---|---|
| Site | ORG#o | SITE#s |
| Run | ORG#o#RUN#r | META |
| Input snapshot / proposal | ORG#o#RUN#r | INPUT / PROPOSAL#revision |
| Audit | ORG#o#RUN#r | EVENT#timestamp#eventId |
| Task | ORG#o#TASK#t | META |
| Dispatch | ORG#o#RUN#r | DISPATCH |
| Idempotency | ORG#o#IDEMPOTENCY#actor | OP#operation#key |
| Demo session | ORG#o#SESSION#session | META |
| Escalation | ORG#o#TASK#t | ESCALATION#dueVersion |
| Published replay | PUBLIC#REPLAY#id | META |

GSI1: site lookup of runs/tasks, PK `ORG#o#SITE#s#SESSION#session`, SK `RUN#createdAt#id` or `TASK#dueAt#id`.

GSI2: maintenance buckets, PK `WORK#DISPATCH`, `WORK#LEASE`, or `WORK#DUE#LIVE`; SK `time#orgId#entityId`. A record has only one maintenance purpose. Demo task due keys use `WORK#DUE#SESSION#id` to keep simulated time separate. Query bounded due ranges; this global small-demo partition is an acknowledged scale limit, not a production sharding design.

Idempotency keys map to request hashes. Reuse with different payload gives 409. Tasks use deterministic `proposalId:taskType` IDs. Proposal approval checks all relevant primary records in a transaction, writes at most four tasks, and keeps the payload below DynamoDB transaction/item limits.

## Four published coordination tasks

1. `schedule_notice`: supervisor acknowledges reading the revision.
2. `water_check`: supervisor reports drinking-water availability; no invented amount or vendor order.
3. `shade_check`: supervisor reports rest-area availability and capacity.
4. `resolve_remaining_exposure`: operations lead resolves remaining flagged work through changed constraints or deferral and replanning.

Demo dueAt is sessionClock + 10 minutes for readiness checks. Live dueAt is explicitly chosen relative to the scheduled shift; reject deadlines already in the past unless creating an immediately overdue task with an explicit UI warning.
