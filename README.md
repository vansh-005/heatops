# HeatOps — implementation pack

Finalized direction: Track 02, Heat and Water. Prepared 9 October 2026, IST.

**HeatOps turns a heat forecast into a supervisor-approved work plan—and follows up on the actions that plan requires.**

This is a planning and implementation handoff, not an implemented or deployed application. Checkboxes describe work still to do. The included synthetic fixture and arithmetic checker are executable planning aids; no AWS resources were created.

## Start here

1. Read `demo.md`: the product is built around a 2:50 recorded story.
2. Read `product.md` and `frontend.md`: what the supervisor sees and does.
3. Read `architecture.md`, `contracts.md`, and `agent.md`: how it works.
4. Give your coding assistant `AGENTS.md`, then execute `tasks.md` in order.
5. Use `testing.md`, `deployment.md`, and `submission.md` to finish.
6. Start the separate Opus video session using `video-production/README.md` or the standalone HeatOps-Video-Starter.zip. The app agent supplies evidence; the video agent owns animation/edit/rendering.

Supporting files: `sources.md`, `decisions.md`, `fixtures/delhi-heat-demo.json`, and `scripts/verify_fixture.py`.

## The memorable moment

A supervisor manages 45 outdoor workers. HeatOps proposes earlier work. The supervisor changes the gate opening time from 6 AM to 7 AM. The agent retrieves the new constraint, recomputes feasible options, exposes the remaining heat overlap, and requests approval of a specific revision. The supervisor receives an action card, acknowledges the schedule, and reports water preparation separately. One missed preparation check becomes overdue.

The product promise is operational follow-through. An acknowledgment is evidence someone responded; it is not evidence that a real site is safe.

## Non-negotiable build choices

- React + TypeScript + Vite + Tailwind frontend; Python application backend and Strands agent; TypeScript AWS CDK.
- AWS Amplify Hosting, API Gateway HTTP API, Lambda, DynamoDB, SQS, EventBridge, Cognito, and Bedrock. No always-on server or VPC for this MVP.
- One orchestrating agent with typed tools. Observation, planning, and follow-up are phases, not three artificial agents.
- Deterministic scheduling and metrics; the LLM chooses tools and explains results.
- In-app dispatch and follow-up are P0. SES, WhatsApp, maps, historical weather replay, and voice are stretch work.
- Live AWS run in the recording; persistent `Synthetic weather scenario` badge on fixture data.
- Public read-only saved-run replay for reviewers; authenticated writes for the presenter.

## Kickoff prompt

> Read AGENTS.md and this implementation pack. Implement the application tasks T00–T13 in dependency order, beginning with T00 and the synthetic vertical slice; also prepare the repository/writeup portion of T15. A separate video session owns T14 and final video production. Provide the evidence handoff described in video-production/handoff.md. Preserve the demo narrative and API contracts. Verify current SDK interfaces before selecting dependency versions and commit lockfiles. Report completed task IDs, evidence, and blockers honestly. Do not mark mock integrations as complete or substitute simulated model output for a real Bedrock run. Keep progress in tasks.md. Use deployment.md for account-specific setup; do not invent account IDs, model access, URLs, or credentials.

Run the planning fixture check from this directory with `python3 scripts/verify_fixture.py`.
