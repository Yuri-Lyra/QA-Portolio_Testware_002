# Approach

## Scope
- **In scope:** reviews component on the home page, the reviews page and provider pages; desktop and mobile web; collapsed and expanded states; image and connection fallbacks.
- **Out of scope:** how reviews are submitted, moderation, and the review API internals (treated as a black box).

## Standards and method
- ISO/IEC/IEEE 29119-2 (test processes), -3 (documentation), -4 (techniques).
- ISTQB CTFL 4.0 vocabulary and techniques.
- Testware split into: Test Plan, Test Analysis (conditions), Test Design (decision table, cases, charters), Test Implementation (sets, procedures, data, schedule) and Defect Report template.

## Traceability
Rule (R1 to R7) -> Test condition -> Test case -> Test set. Every rule has at least one condition and every condition at least one case.

## Assumptions to confirm
| ID | Assumption | Impact if wrong |
|----|------------|-----------------|
| A3 | Behaviour when a provider has zero 5-star reviews is undefined; the oracle expects an empty section | Cases for decision-table rule 1 need a new expected result |
| A4 | Same-day reviews are ordered by lower seed ID first | Tie cases (seeds 21 to 23) change |
| Others | Design reference, build availability for the mobile app | Execution of mobile cases |

Assumptions are listed in the design because an untestable or ambiguous rule is a finding in itself, and asking early is cheaper than a defect later.

## Schedule (3 days)
| Day | Focus |
|-----|-------|
| 1 | Analysis and design review; seed data loaded; oracle verified |
| 2 | Execution of high-priority sets (collapsed rules, decision table) |
| 3 | Expanded state, fallbacks, responsiveness, retests, report |

## Entry and exit criteria
- **Entry:** seed data loaded, test environment reachable, assumptions A3 and A4 answered or accepted.
- **Exit:** all high-priority cases executed, no open critical or high defects, every deviation logged.
