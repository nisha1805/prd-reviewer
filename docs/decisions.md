# Decision log

## 2026-10-30: Expect most real PRDs to rate Weak
- Observation: after hand-rating one real proposal (2 Good, 5 Weak, 2 Missing), I believe most human-written PRDs will be mostly Weak. This is a hypothesis to test on the 10-document set, not a measured fact.
- Implications: (1) the report must rank findings by severity and show the top few first, to avoid alert fatigue; (2) evaluation must beat the always-Weak baseline and report results per rating; (3) the defect-injection test provides a balanced check.
- Owner: Swet

## 2026-10-31: Rubric v2, three clarifications after comparing with the tool
- Context: on two hand-rated Kubernetes proposals the tool agreed on 15 of 18 ratings (baseline 7 of 18). The three disagreements came from ambiguous wording in the rubric.
- Decisions: (1) criterion 3: a stated goal with no measure is Weak, and Missing means no goal at all; (2) criterion 8: "decide before a named release" counts as a decision date; (3) criterion 9: owners must be named people or teams, and a tracker link does not count as an owner.
- Caveat: decision 3 changed my own hand rating of document 2, criterion 9 (Good to Weak), after I had seen the tool's answer. Document 2 is therefore not a blind test for that criterion. Results on new documents will be the fair test.
- Owner: Swet

## 2026-10-31: Rubric v2.1, content outside the dedicated section
- Observation: after rubric v2 the tool credited relevant content found outside a criterion's own section (3 new disagreements with my section-based hand ratings).
- Decision: substantial coverage elsewhere in the document is rated Weak and noted as scattered; a generic mention does not count.
- Next: re-check the three affected hand ratings against the actual text before changing any of them, so ratings are not simply changed to match the tool.
- Owner: Swet

- Update, same day: after reading the text, I re-rated two hand ratings from Missing to Weak because substantial relevant content sits outside the dedicated section: doc 1 criterion 6 (Version Skew Strategy) and doc 2 criterion 5 (Alpha limitations). Doc 2 criterion 2 stays Missing, since only a generic mention of "users" exists. These changes follow the text, not the tool's output, but I had seen the tool's answer first, so these two documents are practice data, not a blind test.

## 2026-10-31: Consistency test, document 1, three runs
- Result: stable on 7 of 9 criteria. Flips were criterion 4 (Weak/Good/Good) and criterion 7 (Weak/Weak/Good), both between neighbouring ratings, both on criteria where I rated Good by hand.
- Interpretation: the tool is stricter than me on borderline Good calls. Criterion 7 is borderline in the document itself (loose rollback trigger).
- Decision: no further rubric changes on documents 1 and 2, which were already used for tuning. Next evidence: a third document rated by hand before running the tool.
- Possible later fixes: set temperature to 0, take the majority of 3 runs, or show a "borderline" label when runs disagree.
