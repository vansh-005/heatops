# Application implementation tasks

Execute in dependency order. Mark tasks complete only after their acceptance criteria are verified.

## P0 tasks and acceptance

- [ ] **T00 — Verify account and model access.** Check AWS identity, region, quotas, available credits/billing, and one real Bedrock tool-use round trip. Select/pin model and SDK. Done: recorded model/region, redacted successful tool result, tested configuration in decisions.md. If access is blocked, report it and continue independent local work without assuming model availability.
- [ ] **T01 — Repository and domain (T00).** Create layout, runtime lockfiles, env examples, fixture schemas, clock interface. Run supplied fixture checker. Done: 135/45/60 exposure totals, all schedules 270 task-hours, no secrets.
- [ ] **T02 — Screening and planner (T01).** Implement interval intersections, complete-hour validation, whole-crew candidate enumeration, gate/fixed-window/rest/resource constraints. Done: initial 06:00 and revised 07:00 plans match fixture; impossible constraints return explicit failure.
- [ ] **T03 — Infrastructure skeleton (T00).** CDK for table/indexes, queue/DLQ, API, worker, maintenance, Cognito, logs; frontend hosting. Done: cloud health check and authenticated request on real URL. Confirm no unintended reserved-concurrency failure.
- [ ] **T04 — Durable async run (T01,T03).** Create run+dispatch+idempotency transaction, send/repair queue dispatch, leases/fencing, event polling, bounded errors. Done: API returns 202 quickly; refresh retains run; duplicate delivery cannot publish twice.
- [ ] **T05 — Real agent loop (T02,T04).** Add six typed tools, model configuration, budgets, input snapshots, proposal validation, audit events. Done: real Bedrock run selects a verified candidate; injected invalid candidate rejected; source visible. Preserve the sanitized run ID and tool results.
- [ ] **T06 — Hero operations screen (T01, then T04/T05).** Build timeline, source badge, tool receipts, comparison, loading/error states. Done: screenshot reads clearly at 1080p; UI uses actual run responses. Fixture UI work can start early, but live integration is required to complete.
- [ ] **T07 — Constraint correction and revision (T05,T06).** Gate edit → site version increment → invalidate → new run → 135 to 60 comparison. Done: old proposal unapprovable, new revision carries correct input versions and remaining work.
- [ ] **T08 — Approval and coordination (T07).** Transactionally validate/hash approval and publish four tasks. Done: repeat click returns same result; changed forecast/site rejects approval; unresolved conditions visible.
- [ ] **T09 — Mobile receipt and readiness (T08).** Supervisor view, role checks, independent acknowledgment and readiness reporting. Done: acknowledgment appears in ops view after refresh; water remains unconfirmed until reported.
- [ ] **T10 — Due checks and recovery (T04,T09).** Maintenance due evaluation, one escalation per due version, lease recovery, demo clock isolation. Done: synthetic +15-minute action shows overdue once; live-mode clock mutation returns forbidden/error; live timer exercised at least once.
- [ ] **T11 — Live weather adapter (T02,T05).** Fetch temperature, humidity, apparent temperature with units/timezone/provenance; cache, timeout, freshness. Done: actual forecast loads or explicit outage; no fixture fallback presented as live. Live weather may not trigger the screening threshold.
- [ ] **T12 — Read-only reviewer replay (T09,T10).** Publish sanitized capture of a real completed synthetic-input run. Done: incognito opens replay without model spend; no write access; capturedAt/source/run ID visible.
- [ ] **T13 — Risk-based verification (T07–T12).** Execute testing.md release gates, repair concrete failures, document limitations. Done: three successful complete end-to-end runs and evidence for critical boundary cases.
- [ ] **T14 — Technical delivery (T13).** Complete runnable setup instructions, architecture documentation, environment examples, attribution, known limitations, and the repository/writeup checklist in submission.md. Done: documented commands match the implementation and claims match verified behavior.

## P1, after the core application passes verification

- [ ] Optional SES to an explicitly configured test recipient, with delivery semantics and sandbox prerequisites verified.
- [ ] Reviewed Hindi labels; optional generated plan translation with number/time parity checks.
- [ ] Historical replay with correctly identified weather data product and provenance.
- [ ] Two additional sample sites, clearly separated from the hero metrics.
- [ ] CSV export / richer comparison / blog post for optional blog prize.

## Scope gates

Complete a real deployed proposal before adding optional features. Keep authorization and approval correctness in scope. If an integration remains incomplete, document that limitation and remove unsupported claims. Prioritize fixing failed acceptance criteria over extending scope.

## Implementation progress log

No implementation milestones completed yet. Append actual date/time, task IDs, verified evidence, and blockers below. The supplied planning fixture check is not evidence that the application runs.

