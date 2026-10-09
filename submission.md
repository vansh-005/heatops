# Submission preparation

## Event checklist

Official rules require a public repository, a YouTube demo under three minutes (public or unlisted), and a short writeup. AWS usage must appear in the video. AI coding tools must be disclosed and reused material credited. Confirm the exact cutoff in the event form, and keep a signed-out link check. See sources.md for official pages.

## Deliverables

- [ ] Correct track and project name.
- [ ] New project history reflects actual work during the event; no backdated commits or fabricated AI logs.
- [ ] Repository contains runnable setup, architecture, env examples, license/attribution, and known limitations.
- [ ] Secret scan and repository review completed before making it public.
- [ ] Video exported, under 3:00, captions legible, synthetic/replay labels retained.
- [ ] AWS proof and matching application run appear in the recording.
- [ ] Uploaded YouTube link opens signed out.
- [ ] Writeup claims only implemented, verified features.
- [ ] Deployed URL or reviewer replay tested signed out, if included.
- [ ] Registration/profile details and final submission form checked.
- [ ] Submission confirmation saved after user-authorized submission.

## Short description draft

HeatOps helps construction-site supervisors turn heat forecasts into actionable work plans. Its AI agent reads site constraints, compares schedules using deterministic calculation tools, and revises its proposal when a supervisor changes an operational constraint. Approved coordination plans create assigned preparation tasks with acknowledgment and overdue follow-up. The demo uses synthetic weather, reports remaining exposure openly, and does not claim to certify workplace safety.

## Build paragraph — use only after verified

HeatOps uses React on AWS Amplify, API Gateway and Lambda for application requests, DynamoDB for versioned plans and audit records, and SQS for asynchronous planning. A Strands agent invokes typed tools through Amazon Bedrock. EventBridge triggers due checks and recovery. Cognito protects write actions; reviewers can inspect a sanitized read-only run replay.

## Result paragraph — use only if the deployed run matches

In our synthetic 45-worker scenario, changing a gate-opening constraint forces the agent to revise its plan. Scheduled worker-hours overlapping the demo screening threshold fall from 135 to 60 while 270 outdoor task-hours remain scheduled. The remaining 60 flagged worker-hours stay visible and require further decisions. These figures demonstrate scheduling arithmetic, not measured health outcomes or productivity.

## AI assistance disclosure template

“We used [actual tools] for [actual activities]. We reviewed the generated implementation and verified [actual checks]. Runtime planning uses [tested Strands version] and [actual Bedrock model]. Synthetic fixture inputs and assumptions are documented.”

Replace placeholders truthfully. Don't list tests or model calls that did not run. Distinguish coding assistants from the runtime agent. Optional blog should explain a real obstacle and its resolution, not invented development drama.
