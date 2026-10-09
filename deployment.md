# Deployment and operating runbook

This is a target workflow. Package scripts and CDK stacks do not exist yet; implement them under tasks.md before running the proposed commands.

## First-hour checks

1. Confirm AWS CLI identity with `aws sts get-caller-identity` and region/profile selection. Do not paste full account details into a public log.
2. Verify actual current credits and account limits; prior Recollect credits/concurrency are history, not current guarantees.
3. In the selected Bedrock region, verify available tool-capable model access with a one-tool request and result. Record model ID/profile ID, SDK version, and regional policy. If using a cross-region inference profile, check required destination-region permissions.
4. Verify exact submission cutoff from the event's submission form and enter it in decisions.md. Keep the internal recording buffer.
5. Confirm DNS/HTTPS hosting route, Cognito callback/logout URLs, and budget notifications.

## Target local commands to implement

| Command | Expected responsibility |
|---|---|
| `python3 scripts/verify_fixture.py` | Available now: check supplied planning numbers |
| `npm ci` | Install locked frontend/infra dependencies after scaffold exists |
| `npm run dev --workspace apps/web` | Start UI after scripts exist |
| `python -m pytest` | Domain/service suite after tests exist |
| `npm run infra:synth` | Synthesize CDK template |
| `npm run infra:deploy` | Deploy selected HeatOps stack/account |
| `python scripts/seed_demo.py` | Seed synthetic org/site/roles without real worker data |
| `python scripts/smoke_cloud.py` | Exercise authorized deployed API/agent flow |
| `npm run build --workspace apps/web` | Build frontend with public config only |

Implement platform-neutral scripts where possible; user uses Windows/PowerShell. Do not assume bash env assignment in user-facing setup instructions. Maintain `.env.example` and a PowerShell setup example after choosing versions.

## Configuration contract

Backend: `AWS_REGION`, `BEDROCK_REGION`, `BEDROCK_MODEL_ID`, `TABLE_NAME`, `JOB_QUEUE_URL`, `MAX_AGENT_SECONDS=120`, `MAX_TOOL_CALLS=12`, `WEATHER_TIMEOUT_SECONDS=10`, `LIVE_WEATHER_MAX_AGE_SECONDS=10800`, `DEMO_ENABLED`, `LOG_LEVEL`.

Frontend public config: `VITE_API_BASE_URL`, `VITE_AWS_REGION`, `VITE_COGNITO_USER_POOL_ID`, `VITE_COGNITO_CLIENT_ID`, `VITE_COGNITO_DOMAIN`, `VITE_AUTH_REDIRECT_URI`.

No long-lived AWS keys in any application environment file; Lambda uses IAM roles. Local development uses the user's configured AWS profile. Never print credentials in setup output.

## Resource setup

Deploy one clearly named HeatOps stack. Lambda API gets only domain-table and queue permissions it requires. Worker gets scoped table, queue-consumer, and model invocation permissions. Maintenance gets indexes/table and queue send permissions. Public replay read path must select only published sanitized replay records.

Use on-demand DynamoDB; no VPC attachment or NAT. Queue settings from architecture.md; alarms for DLQ >0, worker errors, and maintenance lag. CORS allow only local development origins and the deployed frontend. Cognito JWT authorizer verifies intended audience and issuer.

Amplify: provision via the chosen supported path and document it in the resulting repository. A manual build upload is acceptable for the weekend if repository integration is unavailable; do not claim automatic deployment until configured. Record the actual HTTPS URL only after opening it successfully.

## Live weather adapter

Open-Meteo forecast endpoint: `https://api.open-meteo.com/v1/forecast`. Configure coordinates from the seeded site, `hourly=temperature_2m,relative_humidity_2m,apparent_temperature`, `timezone=Asia/Kolkata`, and an appropriate forecast window. Validate units, returned timezone, date coverage, and finite values. Persist fetch time and attribution. Don't invent a forecast issuance timestamp if the API doesn't provide it.

Cache a bounded per-site/date snapshot. Mode never changes on error. A failed live call returns an error, not the synthetic fixture. Display attribution/link and check current provider terms before broader use.

## Recording day operations

Seed a fresh session, confirm the model and maintenance are healthy, sign in both operations and supervisor tabs, verify source badges, and run the full rehearsal once. Capture a real Bedrock execution before editing. Create a sanitized immutable replay from successful evidence; do not expose access tokens, raw prompts with personal data, or full cloud account IDs.

## Recovery

Bedrock denied: inspect model access/config/IAM, then rerun a minimal tool request. No silent model substitution.

Run stuck QUEUED: inspect dispatch record, queue metrics, and maintenance logs. Run stuck RUNNING: inspect lease/fence and error log; use documented recovery, not manual success writes.

Approval conflict: refresh current inputs and replan. Never remove version checks to rescue a demo.

Auth failure: inspect callback/origin/issuer/audience. Never disable authorization on write routes.

## Teardown

Export desired demo evidence first. Disable scheduled triggers and new run creation, drain or purge only this project's queues if no work is needed, then destroy the named stack and hosting resources according to their retention policies. Verify leftover logs, hosted builds, and any retained table. Keep public submission artifacts available for judging as needed. Do not touch Recollect or unrelated resources.
