# Representative test cases

A selection that shows the style of the full set. Priority: H = high, M = medium.

| ID | Rule | Technique | Pri | Steps | Expected result |
|----|------|-----------|-----|-------|-----------------|
| TC-REV-001 | R1, R2, R3 | Equivalence partitioning | H | Open the home page in collapsed state | Exactly 3 cards, all 5★, newest first (oracle: seeds 1, 7, 3) |
| TC-REV-002 | R1 | Boundary value | H | Open provider A (4 recent 5★) | 3 cards; the 4th 5★ is hidden |
| TC-REV-003 | R2 | Error guessing | H | Open provider A; seed 2 is a 4★ dated after most 5★ | The 4★ review is not shown in collapsed state |
| TC-REV-004 | R4 | Decision table (rule 9) | H | Open provider B | 2 recent + 1 old 5★ (seeds 7, 8, 9) |
| TC-REV-005 | R4 | Decision table (rule 7) | H | Open provider J | 1 recent + 2 old (seeds 29, 30, 31); seed 32 hidden |
| TC-REV-006 | R4 | Error guessing | H | Open provider C; seed 15 is a recent 2★ | Only old 5★ shown (seeds 12, 13, 14); the 2★ does not replace any |
| TC-REV-007 | R3 | Boundary value | M | Open provider A and B and compare reviews dated 2025-12-31 and 2026-01-01 | Dates sort correctly across the year boundary |
| TC-REV-008 | R3 | Error guessing | M | Open provider F (three 5★ on the same date) | Order follows the tie-break assumption (A4); flag if unstable between reloads |
| TC-REV-009 | R1 | Decision table (rule 1) | M | Open provider E (no 5★) | Section follows the confirmed behaviour for A3 (assumed empty, no broken layout) |
| TC-REV-010 | R5 | State-based | H | Expand the list on provider A | All ratings visible, newest first, including 4★ seed 2 at the top |
| TC-REV-011 | R5 | State-based | M | Scroll to the end of an expanded list | Next page loads without duplicates or gaps; no endless spinner at the end |
| TC-REV-012 | R5 | State-based | M | Expand then collapse | Returns to the same 3 cards as TC-REV-001/002 |
| TC-REV-013 | R6 | Equivalence partitioning | M | Check each card on the home page | Each card shows a provider name that links to the provider page |
| TC-REV-014 | R7 | Error guessing | M | Block the avatar image request | Fallback image appears; layout does not shift |
| TC-REV-015 | R7 | State-based | M | Throttle the network to slow | Loading placeholder appears, then real cards; no fallback on success |
| TC-REV-016 | R7 | Error guessing | M | Return an API error for reviews | Behaviour matches the rule: the fallback is reserved for broken image and slow connection, anything else is a question to the team |
| TC-REV-017 | Responsive | Exploratory charter | M | Repeat TC-REV-001 on a phone viewport and a tablet viewport | Same 3 cards; no overlap, no horizontal scroll |

## Exploratory charters
- **CH-1:** Explore the expanded list with fast scrolling and flaky network to discover duplicates, gaps and stuck loaders (45 min).
- **CH-2:** Explore card layout with very long names, very long text and missing optional fields on small screens (45 min).
