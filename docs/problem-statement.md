# Problem Statement: PRD Reviewer

## The problem

Product requirement documents (PRDs) often reach engineering without the basics: a measurable success metric, a clearly named user, explicit non-goals and known risks. These gaps usually surface late, in engineering review or after launch, when they cost the most to fix. Junior PMs rarely get detailed, structured feedback on a draft before they share it.

## Who has the problem

Two groups write or review PRDs, and each needs something different from a first-pass review.

| User | Situation | What they need |
| --- | --- | --- |
| Junior and mid-level PMs | Write PRDs, often without a senior PM nearby to review them | Specific feedback before the PRD is shared |
| Product leads and engineering managers | Review many PRDs and spot the same gaps repeatedly | A consistent first pass, so review time goes to the idea |

## Why it matters

A weak PRD pushes avoidable questions and rework downstream. These are hypotheses to test with real reviewers, not measured facts.

- No success metric: the team cannot tell whether the feature worked.
- No non-goals: scope grows during build.
- Unnamed risks: they appear as late surprises.
- Missing basics: review meetings are spent on structure instead of on whether the idea is right.

## Current alternatives and why they fall short

No alternative gives a PM fast, consistent, evidence-based feedback on their own draft. These gaps are assumptions to check in user feedback.

| Alternative | What it does well | Where it falls short |
| --- | --- | --- |
| PRD templates | Show which sections to include | Do not check the quality of what is written |
| Asking a general AI chatbot | Fast and flexible | No fixed rubric, so results vary, and nothing is measured |
| Review by a peer or manager | Deep, contextual feedback | Slow, depends on availability, differs between reviewers |
| Courses and books | Teach what a good PRD looks like | Give no feedback on your own document |

## Opportunity and hypothesis

We believe a tool that applies a fixed, written rubric will give faster and more consistent first-pass feedback than a general chatbot prompt. Every finding will quote the passage of the PRD it refers to, so the PM can check it and decide. The tool checks structure and clarity only. It does not judge whether the product idea is good, and a human reviewer stays in the loop.

## How we will know it works

Version 1 succeeds if it reliably catches missing PRD elements and reviewers find the feedback useful.

| Metric | Target |
| --- | --- |
| Detection rate on test PRDs with one element removed | At least 80% |
| Findings that quote evidence from the PRD | 100% |
| Time to return a review | Under 60 seconds |
| Cost per review | To be measured |
| Usefulness rating from 3 external reviewers | To be measured |

**Out of scope for v1:** rewriting the PRD, judging the product idea, storing uploaded documents, and replacing human review.
