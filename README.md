# HeatOps — implementation pack

Track 02: Heat and Water.

**HeatOps turns a heat forecast into a supervisor-approved work plan—and follows up on the actions that plan requires.**

This is a planning and implementation handoff, not an implemented or deployed application. Checkboxes describe work still to do. The included synthetic fixture and arithmetic checker are executable planning aids; no AWS resources were created.

## Start here

1. Read `product.md` and `frontend.md` for the application scope and user experience.
2. Read `architecture.md`, `contracts.md`, and `agent.md` for implementation requirements.
3. Give your coding assistant `AGENTS.md` and `CLAUDE.md`, then execute `tasks.md` in dependency order.
4. Use `testing.md`, `deployment.md`, and `submission.md` for verification and technical delivery.

Supporting files: `sources.md`, `decisions.md`, `fixtures/delhi-heat-demo.json`, and `scripts/verify_fixture.py`.

## Core workflow

A supervisor manages 45 outdoor workers. HeatOps proposes earlier work. The supervisor changes the gate opening time from 6 AM to 7 AM. The agent retrieves the new constraint, recomputes feasible options, exposes the remaining heat overlap, and requests approval of a specific revision. The supervisor receives an action card, acknowledges the schedule, and reports water preparation separately. One missed preparation check becomes overdue.

The product promise is operational follow-through. An acknowledgment is evidence someone responded; it is not evidence that a real site is safe.

## Non-negotiable build choices

- React + TypeScript + Vite + Tailwind frontend; Python application backend and Strands agent; TypeScript AWS CDK.
- AWS Amplify Hosting, API Gateway HTTP API, Lambda, DynamoDB, SQS, EventBridge, Cognito, and Bedrock. No always-on server or VPC for this MVP.
- One orchestrating agent with typed tools. Observation, planning, and follow-up are phases, not three artificial agents.
- Deterministic scheduling and metrics; the LLM chooses tools and explains results.
- In-app dispatch and follow-up are P0. SES, WhatsApp, maps, historical weather replay, and voice are stretch work.
- Real AWS execution with a persistent `Synthetic weather scenario` badge on fixture data.
- Public read-only saved-run replay for reviewers; authenticated writes for the presenter.

## Kickoff prompt

> Read AGENTS.md, CLAUDE.md, and the application specifications. Implement tasks.md in dependency order, beginning with T00 and the synthetic vertical slice. Preserve the product requirements and API contracts. Verify current SDK interfaces before selecting dependency versions and maintain lockfiles. Report completed task IDs, verification evidence, and blockers accurately. Keep progress in tasks.md. Use deployment.md for account-specific setup; do not invent account IDs, model access, URLs, or credentials.

Run the planning fixture check from this directory with `python3 scripts/verify_fixture.py`.

