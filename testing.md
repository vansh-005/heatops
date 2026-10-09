# Verification and release gates

These checks are for the application to be built. Only the standalone planning-fixture checker can be run from this pack today.

## Domain correctness

| Case | Expected result |
|---|---|
| Supplied baseline | 135 flagged worker-hours, 270 task worker-hours |
| Gate 06:00 proposal | 45 flagged, 270 total |
| Gate 07:00 proposal | 60 flagged, 270 total; 55.6% displayed reduction |
| Block ends at 13:00 | No overlap with [13:00,16:00) |
| Block ends at 13:30 | 0.5 hour per person in flagged interval |
| Baseline exposure zero | Percent is null, no divide by zero |
| Missing hourly weather or stale live snapshot | INSUFFICIENT_DATA; no optimistic zero |
| Contradictory fixed task / gate time | Candidate infeasible, reason named |
| Rest area exceeds supplied capacity | Candidate rejected or explicit unresolved constraint; never silently accepted |
| Same crew overlaps itself | Invalid schedule |
| Water reported ready | Exposure arithmetic unchanged |
| Task deferred | Deferred task-hours separately reported; no productivity claim |

## Integration and authority

1. Model invokes actual tools using Bedrock. Capture model/region, duration, run ID, sanitized tool receipts. Verify callback wiring does not expose hidden reasoning.
2. Duplicate job and duplicate approval produce one proposal/task set. Retry idempotency key with a different payload fails.
3. Fail between durable run creation and queue send. Maintenance recovers the pending dispatch. Fail after send before marking SENT: duplicate processing remains harmless.
4. Expire a worker lease and allow a new worker claim. Old fencing token cannot write a proposal. Terminal failure after bounded attempts is visible.
5. Change gate, forecast, or policy after proposal. Approval fails with stale-input conflict, even if the browser still shows the old review drawer.
6. Sign in as the wrong organization or role. All site/run/task mutations deny access. Public replay cannot invoke Bedrock or change a task.
7. Acknowledge a schedule. It completes receipt only; water readiness is unchanged. A readiness report is visibly supervisor-reported.
8. Advance synthetic clock and repeat due evaluation. Exactly one escalation per due version. Clock API rejects live sessions and unauthorized users.
9. Simulate Bedrock denial/throttle/timeout and weather outage. Show truthful failures. No generated success from frontend timers.
10. Put prompt-injection text into site notes. Agent cannot approve, alter policy, cross tenants, or call unrestricted tools.

## One complete AWS rehearsal

Start fresh synthetic session → run agent → inspect 135 to 45 proposal → change gate to 07:00 → rerun → inspect 135 to 60 and residual hours → approve current revision → inspect four tasks → supervisor acknowledges schedule → reports one resource ready → leave another pending → advance demo clock → verify overdue action → refresh both views → show matching CloudWatch run ID.

Also test maintenance with a real near-future live deadline once; the accelerated scenario alone is not proof of scheduled execution.

## Visual and recording gate

At 1920×1080 and 390px mobile verify source badges, units, timezone, metrics, residual exposure, editable gate, approval limitations, acknowledged vs ready states, keyboard access, and loading/error states. No clipped important text or color-only meaning. Test replay in a signed-out browser.

Record three consecutive successful rehearsals against the deployed system. Capture the first successful one as backup. Stop extending the test matrix once these risks are resolved; use remaining time for recording and submission.

## Evidence log template

For each release check record: check ID, date/time, commit if available, run/session ID, expected, actual, pass/fail, evidence location, and limitation. Do not prefill passes. Screenshots should hide credentials/account details.
