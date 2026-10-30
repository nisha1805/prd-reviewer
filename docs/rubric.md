# PRD Review Rubric

Each criterion describes what a good PRD contains and what a weak one looks like. The tool checks structure and clarity only, not whether the product idea is good. Every finding must quote the passage of the PRD it refers to.

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
- Weak: "Launch in Q2."

## 8. Open questions
- Why it matters: unlisted unknowns turn into silent assumptions that are discovered during the build.
- Good: lists each unresolved question with an owner and a decision date, such as "Do we store uploaded files? Owner: Legal, decide by 15 Nov."
- Weak: no list, or "TBD" with no owner.

## Scoring

Each criterion gets one rating: **Missing**, **Weak** or **Good**. A criterion may be marked **Not applicable** only for criteria 7 and 8, when the PRD describes a small, low-risk change.

Severity when a criterion is Missing or Weak:

| Severity | Criteria | Reason |
| --- | --- | --- |
| Critical | 1 Problem statement, 3 Success metrics, 4 Scope and requirements | The team cannot build or judge the feature without them |
| Major | 2 Target user, 5 Non-goals, 6 Risks and dependencies | Gaps here usually cause rework or late surprises |
| Minor | 7 Rollout plan, 8 Open questions | Important, but easier to add late |

## Planned for v2

- Consistency check: does the success metric measure the problem named in criterion 1?
