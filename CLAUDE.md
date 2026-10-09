# HeatOps — Claude Code project instructions

## Mission and priority

Build HeatOps: a heat-response planning application for construction-site supervisors. Your deliverable is the working application, AWS deployment configuration, tests, and technical documentation. Prioritize correct end-to-end behavior, reliable workflows, clear UI, and then optional features.

This file belongs at the repository root alongside `AGENTS.md` and the planning documents. Read `AGENTS.md` at the start of the session; it is the shared coding-agent policy. This file adds Claude-specific working context without replacing the domain contracts. `agent.md` describes the application's runtime AI agent, not you.

At the time this pack was created, the application was not implemented or deployed. Inspect the repository and current task log before reporting progress; do not mistake this specification for working code.

## First-session workflow

1. Read `AGENTS.md`, `README.md`, `product.md`, and `tasks.md`.
2. Read `product.md`, `contracts.md`, `architecture.md`, `agent.md`, and `frontend.md` before implementing their respective areas.
3. Inspect existing files and git status. Preserve user changes and any work from previous sessions.
4. Start with T00: verify the actual AWS account/region and available Bedrock tool-use model. Record verified choices in `decisions.md`.
5. Run `python3 scripts/verify_fixture.py` from the project root. This checks planning arithmetic only.
6. Implement the next unfinished P0 task in dependency order. For each milestone, verify the relevant acceptance criteria, update `tasks.md`, and report the evidence.

If cloud access is blocked, state the exact blocker and continue useful local domain/UI work that does not depend on it. Do not mark cloud tasks complete or silently substitute a different model provider.

## Core application workflow

The fictional Delhi site has 45 workers. HeatOps inspects weather and constraints and proposes moving a crew earlier. The supervisor changes gate opening from 06:00 to 07:00. The agent reruns its tools, presents a revised schedule, and exposes the remaining flagged work. The supervisor approves coordination tasks, acknowledges the schedule on mobile, and reports preparation separately. A missed preparation check becomes overdue.

Required synthetic-fixture results:

| Schedule | Flagged worker-hours | Scheduled outdoor task-hours |
|---|---:|---:|
| Baseline | 135 | 270 |
| Initial proposal | 45 | 270 |
| Revised proposal | 60 | 270 |

The revised reduction is 75 worker-hours, displayed as 55.6%. Compute these in backend code; never hardcode response metrics or ask the model to calculate them. Keep the weather source and scenario date visible. A reduction is not workplace safety clearance or measured productivity.

## Technical choices

- Frontend: React + TypeScript + Vite + Tailwind on Amplify Hosting.
- Backend: Python Lambda; shared Pydantic domain models and deterministic scheduling functions.
- Runtime AI: one Strands agent with six typed tools through Amazon Bedrock. Select and pin a tested model and SDK version.
- Infrastructure: TypeScript CDK, API Gateway HTTP API, DynamoDB, SQS + DLQ, EventBridge maintenance, Cognito, CloudWatch.
- Default application region: ap-south-1; Bedrock region/model are explicitly verified configuration.
- Async run creation returns 202; UI polls persisted status/events. No request or Lambda waits for human approval.
- In-app assignments and follow-up are P0. Email, maps, voice, historical replay, and extra sites are P1.

Follow the repository layout in `AGENTS.md`. Keep pure domain code separate from AWS adapters. Do not introduce another framework, microservice, database, or agent unless an actual acceptance criterion requires it.

## Runtime boundaries to enforce in code

- Model tools cannot approve plans, publish assignments, change policy, choose arbitrary recipients, execute shell commands, or make unrestricted HTTP requests.
- The planner calculates feasible schedules; the model orchestrates calls and explains verified results. Enforce the ranking and proposal rules in `agent.md`.
- Approval checks current versions and proposal hash transactionally. Changed site, forecast, or policy makes the old proposal stale.
- Duplicate jobs, retries, and repeated approval clicks must not create duplicate effects. Preserve lease fencing and idempotency.
- Derive organization and roles from authenticated server context, never caller-supplied identity fields.
- Synthetic clock controls are restricted to owned synthetic sessions. Public saved-run replay is immutable and cannot trigger model calls.
- Schedule acknowledgment does not confirm water/shade readiness. Readiness is supervisor-reported, not independently verified.
- Missing or stale weather is insufficient data, not zero risk. Never replace a failed live forecast with unlabeled fixture data.
- Enforce agent time/tool budgets outside the prompt. Record tool receipts, not hidden chain-of-thought or invented reasoning traces.

## UI behavior

Follow `frontend.md`: warm off-white canvas, navy text, clear amber/red alerts, teal acknowledgments. The schedule timeline and constraint change are the main visuals. Do not replace the product with a chat window.

Implement real queued/running/stale/failed/overdue states. No timer-generated fake progress. Keep remaining exposure prominent beside the improvement metric. Verify a real Bedrock-backed run and retain its sanitized run ID and results before extending scope.

## Commands and environment

At pack creation, only `python3 scripts/verify_fixture.py` is supplied as an executable check. Commands in `deployment.md` are targets to implement, not proof that package scripts exist. Inspect manifests before running them; add and document missing scripts as part of the scaffold.

Use locked dependencies and the matching current official documentation for SDK interfaces. Keep secrets out of files, logs, screenshots, and browser bundles. `.env.example` contains placeholders only. Local AWS access uses the configured profile; deployed Lambda uses IAM roles. The user works on Windows/PowerShell, so provide compatible setup commands.

Respect the user's current instructions for commits, deployment, publication, and submission. A planning checklist is not permission to publish a repository or contact people. Continue already-authorized work without repeatedly asking for confirmation.

## Verification and handoff

Use `testing.md` for risk-based checks: fixture arithmetic, constraint feasibility, stale approval, duplicate processing, role enforcement, provider failure, and the complete deployed workflow. Run checks appropriate to the change; avoid expanding scope with redundant tests.

Update checkboxes only after verification. Keep a short actual progress log in `tasks.md`: completed IDs, checks run, evidence/run IDs, failures, and the next task. Record important design changes in `decisions.md` and update affected specs together. Never fabricate development history, prompts, test results, users, or metrics.

Before a context reset or session end, leave enough state in those files for the next session to resume without guessing. Final milestone reports should distinguish implemented, verified locally, verified on AWS, and still pending.

