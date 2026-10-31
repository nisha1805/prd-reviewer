# Hand ratings (ground truth)

Ratings: Missing, Weak, Good or N/A. Evidence: a short quote or the section name.

## 01-kep-3960-sleep-action.md

| # | Criterion | Rating | Evidence |
| --- | --- | --- | --- |
| 1 | Problem statement | Weak | Motivation explains the gap (exec and httpGet need extra scripting) but gives no number, quote or real failure |
| 2 | Target user | Weak | Stories name only "Kubernetes user"; Story 2 adds an nginx zero-downtime context but no specific user group |
| 3 | Success metrics | Weak | Goals are vague ("improve reliability"); Graduation Criteria are outputs (flag, tests, docs) with no numbers; SLOs answered N/A |
| 4 | Scope and requirements | Good | Implementation spells out the SleepAction and LifecycleHandler API changes and runtime behaviour; testable; phases separate what ships when |
| 5 | Non-goals | Weak | Two exclusions listed, but neither has a reason |
| 6 | Risks and dependencies | Missing | Risks and Mitigations section contains only "N/A" |
| 7 | Rollout plan | Good | Feature gate PodLifecycleSleepAction to switch off, Alpha/Beta/GA phases, rollback metric named; but trigger is vague ("increases unreasonably", no threshold) |
| 8 | Open questions | Missing | No unresolved or TBD questions listed anywhere; KEP template has no such section |
| 9 | Timeline and milestones | Weak | Implementation History has dated draft and beta/stable release targets, but no owners and no link to a tracker |

## 02-kep-4438-container-restart.md

| # | Criterion | Rating | Evidence |
| --- | --- | --- | --- |
| 1 | Problem statement | Weak | Motivation justifies splitting the KEP (avoid risk in beta) but never describes the user's pain, with no number, quote or incident |
| 2 | Target user | | |
| 3 | Success metrics | | |
| 4 | Scope and requirements | | |
| 5 | Non-goals | Missing | Heading present but only the template comment, nothing written |
| 6 | Risks and dependencies | Good | Three specific risks with mitigations, named dependencies (CRI stop/remove, DRA unprepare), alpha opt-in as fallback |
| 7 | Rollout plan | | |
| 8 | Open questions | | |
| 9 | Timeline and milestones | | |
