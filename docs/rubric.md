# PRD Review Rubric

Each criterion describes what a good PRD contains and what a weak one looks like. The tool checks structure and clarity only, not whether the product idea is good. Every finding must quote the passage of the PRD it refers to.

## Rating definitions
- Good: meets the criterion's Good line.
- Weak: something relevant is present but falls short of the Good line, for example a vague aim or a missing owner.
- Missing: nothing relevant is present. An empty heading, an unfilled template placeholder or "N/A" counts as Missing.
- Content outside the dedicated section: if a substantial part of the criterion is covered elsewhere in the document, rate Weak and note that it is scattered. A passing generic mention, such as the word "users", does not count.

## 1. Problem statement
- Why it matters: without a stated problem, the team builds a solution that nobody can check against a real need.
- Good: describes the user's pain with evidence (a number, a quote or an observed behaviour) before mentioning any solution, such as "Support agents spend 12 minutes per ticket searching three tools, and 40% of tickets are reopened."
- Weak: states a solution as the problem, such as "We need a new dashboard."

## 2. Target user
- Why it matters: without a specific user, requirements and priorities cannot be decided or tested.
- Good: names one primary user group and their context, such as "Customer success managers at B2B software companies who handle 30 or more accounts."
- Weak: "All users" or "customers."

## 3. Success metrics
- Why it matters: without a measurable target, nobody can tell whether the feature worked.
- Good: a number, a baseline and a deadline, such as "cut report time from 30 minutes to 5 by Q2".
- Weak: a vague aim such as "improve user satisfaction".
- Rating note: a stated goal without a measurable target is Weak. Missing means no goal or success measure at all.

## 4. Scope and requirements
- Why it matters: vague requirements get interpreted differently by design, engineering and testing.
- Good: each requirement is specific enough to test, and must-haves are separated from later ideas, such as "Users can export a report as CSV in under 10 seconds (must-have). Scheduled exports (later)."
- Weak: "The export should be fast and easy to use."

## 5. Non-goals
- Why it matters: without explicit exclusions, scope grows during the build and people disagree on what "done" means.
- Good: lists at least two things a reader might reasonably expect that are deliberately left out of this version, each with a one-line reason.
- Weak: no non-goals section, or "Nothing is out of scope."

## 6. Risks and dependencies
- Why it matters: unnamed risks appear as late surprises, when plans are hardest to change.
- Good: names specific risks (technical, privacy or adoption), the teams or systems the work relies on, and a fallback for the biggest risk, such as "Depends on the billing API. If it is late, ship without invoice export."
- Weak: "Risk: timeline" or "Some technical challenges may occur."

## 7. Rollout plan
- Why it matters: a good feature can still fail if the release is uncontrolled and cannot be reversed.
- Good: says who gets it first, in what phases, what result triggers a wider release, and how to switch it off, such as "10% of users in week 1, full release if the error rate stays under 1%, with a feature flag for rollback."
- Weak: "Release to everyone at once, with no way to roll back."

## 8. Open questions
- Why it matters: unlisted unknowns turn into silent assumptions that are discovered during the build.
- Good: lists each unresolved question with an owner and a decision date, such as "Do we store uploaded files? Owner: Legal, decide by 15 Nov."
- Weak: no list, or "TBD" with no owner.
- Rating note: a question tied to a named release milestone (for example "decide before Alpha") counts as having a decision date. The owner must be a named person, team or approver group.

## 9. Timeline and milestones
- Why it matters: without dated milestones and owners, nobody can tell whether the work is on track until it is already late.
- Good: lists key milestones with target dates and owners, and links to the backlog or epic where sprint-level tasks are tracked, such as "Design complete 14 Nov (Design lead); beta 12 Dec (Engineering); tasks tracked in Epic ABC-123."
- Weak: "Launch in Q2."
- Rating note: owners must be named people or teams. A link to a tracking issue or pull request shows where work is tracked but does not count as an owner.

## Scoring

Each criterion gets one rating: **Missing**, **Weak** or **Good**. A criterion may be marked **Not applicable** only for criteria 7 and 8, when the PRD describes a small, low-risk change.

Severity when a criterion is Missing or Weak:

| Severity | Criteria | Reason |
| --- | --- | --- |
| Critical | 1 Problem statement, 3 Success metrics, 4 Scope and requirements | The team cannot build or judge the feature without them |
| Major | 2 Target user, 5 Non-goals, 6 Risks and dependencies | Gaps here usually cause rework or late surprises |
| Minor | 7 Rollout plan, 8 Open questions, 9 Timeline and milestones | Important, but easier to add late |

## Planned for v2

- Consistency check: does the success metric measure the problem named in criterion 1?
