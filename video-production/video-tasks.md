# Video tasks — separate from application tasks

All production tasks start pending. Owner: video agent unless stated otherwise. The application can develop in parallel with V00–V04.

- [ ] **V00 — Setup and tiny render.** Verify local Node/Remotion/plugin; scaffold without overwriting brief files; pin versions. Render a 12-second opening proof. Done: actual playable MP4, no missing font/browser dependencies.
- [ ] **V01 — Visual system.** Build typography, palette, title, heat bands, schedule-block animation, captions, and callout primitives. Done: opening conveys the problem immediately and is readable at 1080p.
- [ ] **V02 — Complete edit skeleton.** Register HeatOpsDemo with the ten scenes/5100 frames from video.md. Use clearly visible draft slates for absent footage. Done: full-duration preview renders without requiring the app.
- [ ] **V03 — Footage and data interface.** Implement asset-manifest loader, deterministic FootageSlot, source badges, trimming, and final-mode validation. Done: missing evidence passes draft mode visibly and blocks final mode.
- [ ] **V04 — Architecture/end card and scratch audio.** Build provisional architecture explanation, closing treatment, and narration/caption layout. Vansh supplies scratch narration when convenient. Done: independent visuals are ready while app integration continues.
- [ ] **V05 — First real footage pass (app milestone B).** Import first real run and check crops/text size. Request specific retakes if necessary. Done: actual app replaces at least one placeholder without redesigning scenes.
- [ ] **V06 — Turning point (app milestone C).** Insert actual gate correction and replan; preserve source labels and residual exposure. Done: viewer sees cause and effect, metrics match verified data.
- [ ] **V07 — Complete proof (app milestone D).** Insert approval, receipt/readiness distinction, overdue task, and AWS evidence. Done: no final app/AWS shot uses a placeholder or fabricated interaction.
- [ ] **V08 — Final narration and captions (V06,V07).** Vansh records voice; video agent integrates, edits pauses, updates captions, and balances audio. Done: script matches actual footage and finishes comfortably in 170 seconds.
- [ ] **V09 — Final render and QA.** Validate evidence, render MP4, check actual duration, watch from start to finish with sound and muted. Done: 1080p playable H.264/AAC under 180 seconds, no black frames or placeholders; export SRT and poster.
- [ ] **V10 — Final user review/upload.** Vansh reviews narrative/claims and uploads/submits or explicitly delegates. Done only after actual link and playback check, not just a local render.

Budget: use the first 60–90 minutes for setup + opening + skeleton. Make a rough complete draft today, replacing its footage as the app becomes available. If rendering is slow, lower preview scale or concurrency; do not add cloud rendering to the hackathon critical path.

Progress log: no production tasks completed in this planning pack. Append actual commands, output files, evidence and blockers here.
