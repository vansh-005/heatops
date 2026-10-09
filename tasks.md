# Build tasks — all implementation pending

Prepared Friday 9 October 2026. Solo build assumption with coding assistance. Estimates are planning ranges, not promises. Critical-path budget roughly 18–24 focused hours plus 4–6 hours for rehearsal/editing/upload. Protect sleep and the recording buffer; cut stretch scope first.

## Owners and parallel work

Application agent: T00–T13 and T15 repository/writeup preparation. Video agent: Remotion project, animations, editing, captions, render, T14 and video portions of T15. Vansh: narration, manual capture where needed, final review and submission. Video work V00–V04 in `video-production/video-tasks.md` starts immediately; it does not wait for T09/T10. T14 needs those app milestones only to finish the real-footage cut. See `video-production/handoff.md`.

## Schedule

| Window (IST) | Milestone |
|---|---|
| Fri 9 Oct, afternoon | Verify account/model, fixture math, skeleton, first deploy |
| Fri 9 Oct, evening | One real Bedrock-backed proposal visible in the app |
| Sat 10 Oct, morning | Constraint change, comparison, approval, tasks |
| Sat 10 Oct, afternoon | Acknowledgment, overdue checks, live adapter, failure gates |
| Sat 10 Oct, evening | Feature freeze, first complete rough video, fixes only |
| Sun 11 Oct, by 11:00 | Final recording and edit target |
| Sun 11 Oct, by 14:00 | Internal submission-ready target; submit earlier if official cutoff requires |

The public page confirms event dates but did not expose an exact cutoff time in fetched content. T00 must check the actual submission form. These times are internal planning targets.

## P0 tasks and acceptance

- [ ] **T00 — De-risk access and rules (45–60 min).** Check event registration/check-in, student profile, exact cutoff, AWS identity, region, quotas, available credits/billing, and one real Bedrock tool-use round trip. Select/pin model and SDK. Done: recorded model/region, redacted successful tool result, confirmed cutoff in decisions.md. If access is blocked, resolve now; do not spend a day building around an unavailable model.
- [ ] **T01 — Repository and domain (45–60 min; T00).** Create layout, runtime lockfiles, env examples, fixture schemas, clock interface. Run supplied fixture checker. Done: 135/45/60 exposure totals, all schedules 270 task-hours, no secrets.
- [ ] **T02 — Screening and planner (90–120 min; T01).** Implement interval intersections, complete-hour validation, whole-crew candidate enumeration, gate/fixed-window/rest/resource constraints. Done: initial 06:00 and revised 07:00 plans match fixture; impossible constraints return explicit failure.
- [ ] **T03 — Infrastructure skeleton (60–90 min; T00).** CDK for table/indexes, queue/DLQ, API, worker, maintenance, Cognito, logs; frontend hosting. Done: cloud health check and authenticated request on real URL. Confirm no unintended reserved-concurrency failure.
- [ ] **T04 — Durable async run (60–90 min; T01,T03).** Create run+dispatch+idempotency transaction, send/repair queue dispatch, leases/fencing, event polling, bounded errors. Done: API returns 202 quickly; refresh retains run; duplicate delivery cannot publish twice.
- [ ] **T05 — Real agent loop (90–120 min; T02,T04).** Add six typed tools, model configuration, budgets, input snapshots, proposal validation, audit events. Done: real Bedrock run selects a verified candidate; injected invalid candidate rejected; source visible. Capture backup footage now.
- [ ] **T06 — Hero operations screen (90–120 min; T01, then T04/T05).** Build timeline, source badge, tool receipts, comparison, loading/error states. Done: screenshot reads clearly at 1080p; UI uses actual run responses. Fixture UI work can start early, but live integration is required to complete.
- [ ] **T07 — Constraint correction and revision (45–60 min; T05,T06).** Gate edit → site version increment → invalidate → new run → 135 to 60 comparison. Done: old proposal unapprovable, new revision carries correct input versions and remaining work.
- [ ] **T08 — Approval and coordination (60–90 min; T07).** Transactionally validate/hash approval and publish four tasks. Done: repeat click returns same result; changed forecast/site rejects approval; unresolved conditions visible.
- [ ] **T09 — Mobile receipt and readiness (45–60 min; T08).** Supervisor view, role checks, independent acknowledgment and readiness reporting. Done: acknowledgment appears in ops view after refresh; water remains unconfirmed until reported.
- [ ] **T10 — Due checks and recovery (45–60 min; T04,T09).** Maintenance due evaluation, one escalation per due version, lease recovery, demo clock isolation. Done: synthetic +15-minute action shows overdue once; live-mode clock mutation returns forbidden/error; live timer exercised at least once.
- [ ] **T11 — Live weather adapter (30–45 min; T02,T05).** Fetch temperature, humidity, apparent temperature with units/timezone/provenance; cache, timeout, freshness. Done: actual forecast loads or explicit outage; no fixture fallback presented as live. Weather may not trigger heat alerts in October.
- [ ] **T12 — Read-only reviewer replay (30–45 min; T09,T10).** Publish sanitized capture of a real completed synthetic-input run. Done: incognito opens replay without model spend; no write access; capturedAt/source/run ID visible.
- [ ] **T13 — Risk-based verification (60–90 min; T07–T12).** Execute testing.md release gates, repair concrete failures, document limitations. Done: three successful complete rehearsals and evidence for critical boundary cases.
- [ ] **T14 — Record rough video (video agent + Vansh; 45–60 min; T09,T10 for real-footage completion).** Follow demo.md. Done: a complete sub-three-minute story exists even if visuals need polish. Do not wait for P1.
- [ ] **T15 — Final video and submission pack (split ownership; 120–180 min; T13,T14).** Video agent owns edit/render/captions; application agent owns repository/writeup/evidence; Vansh owns final review/upload/submission. Record actual deployed run, captions, AWS evidence, trim to 2:50, draft writeup, repository cleanup, links and credits. Done: video accessible signed out, claims match shown features, submission.md complete. Publishing/submitting follows user authorization.

## P1, only after T14

- [ ] Optional SES to an explicitly configured test recipient, with delivery semantics and sandbox prerequisites verified.
- [ ] Reviewed Hindi labels; optional generated plan translation with number/time parity checks.
- [ ] Historical replay with correctly identified weather data product and provenance.
- [ ] Two additional sample sites, clearly separated from the hero metrics.
- [ ] CSV export / richer comparison / blog post for optional blog prize.

## Stop-loss rules

If no deployed proposal by Friday night: finish domain + one agent run before adding screens beyond the main timeline. If no full flow by Saturday afternoon: defer T11's visual cameo and P1, simplify styling, preserve auth/approval correctness. If the live weather adapter remains incomplete, remove live-weather claims and disclose the limitation. If no rough video by Saturday night: freeze features immediately.

## Implementation progress log

No implementation milestones completed yet. Append actual date/time, task IDs, verified evidence, and blockers below. The supplied planning fixture check is not evidence that the application runs.
