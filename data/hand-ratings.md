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
| 6 | Risks and dependencies | Weak | Risks and Mitigations and Drawbacks are N/A, but Version Skew Strategy describes real failure modes (feature enabled on only one of kubelet or kube-apiserver) and names both as dependencies; no mitigation (rubric v2.1, re-rated from Missing after checking the text) |
| 7 | Rollout plan | Good | Feature gate PodLifecycleSleepAction to switch off, Alpha/Beta/GA phases, rollback metric named; but trigger is vague ("increases unreasonably", no threshold) |
| 8 | Open questions | Missing | No unresolved or TBD questions listed anywhere; KEP template has no such section |
| 9 | Timeline and milestones | Weak | Implementation History has dated draft and beta/stable release targets, but no owners and no link to a tracker |

## 02-kep-4438-container-restart.md

| # | Criterion | Rating | Evidence |
| --- | --- | --- | --- |
| 1 | Problem statement | Weak | Motivation justifies splitting the KEP (avoid risk in beta) but never describes the user's pain, with no number, quote or incident |
| 2 | Target user | Missing | Story 1 and Story 2 headings present but empty; no user named in that section |
| 3 | Success metrics | Weak | Goals list behaviours to maintain but no numbers or baseline; Alpha criteria are outputs (gate, approval, tests); SLO question left blank |
| 4 | Scope and requirements | Good | Design Details set explicit scope (only pods with restartable init containers, gate on; no API or CRI changes) and Alpha limitations state what ships first; Proposal paragraph itself is thin |
| 5 | Non-goals | Weak | Non-Goals section empty, but Alpha limitations list real exclusions with reasons (probes not reattached, no durable checkpoint for local eviction); scattered under the wrong heading (rubric v2.1, re-rated from Missing after checking the text) |
| 6 | Risks and dependencies | Good | Three specific risks with mitigations, named dependencies (CRI stop/remove, DRA unprepare), alpha opt-in as fallback |
| 7 | Rollout plan | Good | Feature gate SidecarsRestartableDuringPodTermination, disabled by default, kubelet named; real-node validation and approver sign-off are release requirements; no rollback threshold seen |
| 8 | Open questions | Good | Two named UNRESOLVED decisions (deadline compatibility, local termination recovery) with options, assigned to reviewers/approvers, gated before Alpha; no calendar date |
| 9 | Timeline and milestones | Weak | Dated entries 2024-2026 and link to tracking PR, but no named owners; owners must be named people or teams (rubric v2, re-rated from Good after seeing tool output) |

## 03-kep-2079-network-policy-port-range.md (co-rated with Claude, not blind; do not use for accuracy figures)

| # | Criterion | Rating | Evidence |
| --- | --- | --- | --- |
| 1 | Problem statement | Good | Motivation cites two user issues (#67526, #93111) and a concrete example of listing ports 32000-32768 one by one, before the proposed endPort field |
| 2 | Target user | Weak | Three detailed scenarios, but generic groups ("a developer", "a Kubernetes User"); borderline because context is strong |
| 3 | Success metrics | | |
| 4 | Scope and requirements | | |
| 5 | Non-goals | Weak | Two exclusions listed, neither with a reason |
| 6 | Risks and dependencies | Weak | One risk (CNIs must support the new field), vague mitigation, CNIs named as dependency, no fallback |
| 7 | Rollout plan | | |
| 8 | Open questions | | |
| 9 | Timeline and milestones | | |
