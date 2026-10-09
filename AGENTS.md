# Instructions for the coding assistant

## Mission

Implement the HeatOps application. Priority order: correct end-to-end behavior, reliable user flow, clear interface, then additional features. Deliver application code, deployment configuration, tests, and accurate technical documentation.

This is a project instruction file, not a reusable installed skill. `agent.md` describes the runtime product agent; do not confuse it with these instructions.

## Read order and authority

Read README.md, product.md, contracts.md, architecture.md, agent.md, frontend.md, then tasks.md. Explicit user changes take precedence; record resulting design decisions in decisions.md and keep all affected contracts consistent. If a proposed shortcut contradicts a product requirement, resolve the discrepancy before marking the work complete.

## Suggested repository layout

- `apps/web/`: React app, components, query hooks, generated API types.
- `services/api/`: handlers, auth mapping, command validation.
- `services/worker/`: Strands setup, typed tool wrappers, lifecycle.
- `services/maintenance/`: dispatch repair, lease recovery, due evaluator.
- `packages/domain/`: Python schemas, scheduling, exposure, policy, clock abstraction.
- `infra/`: TypeScript CDK stacks and outputs.
- `fixtures/`: source-tagged synthetic inputs; keep supplied planning fixture.
- `tests/`: meaningful domain, contract, authorization, and end-to-end tests.
- `docs/evidence/`: sanitized screenshots, run IDs, known limitations, verification notes.
- `scripts/`: environment checks, seed, smoke, cleanup, fixture verification.

## Build discipline

Complete T00 before building on an untested model assumption. Pin tested dependency versions and lockfiles. Use environment variables for account-specific settings and `.env.example` placeholders only. Do not hardcode a provider's default model or silently use an external AI provider.

Build the smallest deployed vertical slice early. Frontend fixtures are allowed while wiring screens, but fixture-backed UI must have visible mode labels and be removed from the live service path. Keep pure domain functions independent of AWS adapters.

No metrics calculated by an LLM. No artificial tool receipts. No mocked approval, notification, or acknowledgment reported as real. Never fabricate build history, prompts, logs, users, testimonials, or results. Maintain an honest AI usage note and actual development log.

No credentials, account secrets, real employee records, or raw authentication tokens in logs, commits, browser bundles, or exported evidence. Do not commit generated secret files. Use the user's existing AWS profile only after checking identity and selected region; avoid changing unrelated resources.

Runtime agent privileges: no approval endpoint, shell tool, arbitrary HTTP tool, email destination selection, policy mutation, or unrestricted table access. Enforce organization and session at the service boundary.

## Scope control

No Kafka, Kubernetes, RAG, multi-agent swarm, chat-first UX, city-scale allocation, or new service without a concrete blocked acceptance criterion. Use one orchestrating agent and small deterministic tools. Do not spend time generating visual assets before the schedule workflow works.

Implement live weather with timeout and missing-data behavior. Do not fetch historical reanalysis and call it a forecast made before the event. In demo mode use the exact provided fixture unless the user intentionally changes it and recalculates expected results.

## Completion and evidence

Update task checkboxes only with actual verification. Each completed milestone note lists task IDs, commands/checks, relevant run IDs or screenshots, and remaining limitations. Track duration/cost only when measured. Do not claim deployment from successful CDK synth alone.

Before declaring the application ready, pass the gates in testing.md. Keep evidence proportionate: fixture arithmetic, stale approval, duplicate delivery, role enforcement, timeout handling, and one complete AWS flow are essential. Keep tests focused on the documented acceptance criteria.

Do not publish a public repository, send external messages, or submit the hackathon entry merely because the planning pack mentions them. Prepare those deliverables, then follow the user's actual authorization for publication/submission. Resource deployment should follow the user's selected AWS account and budget constraints.

