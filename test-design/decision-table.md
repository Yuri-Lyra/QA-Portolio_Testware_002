# Decision table: cards shown per provider (collapsed state)

Conditions are the number of **5-star** reviews a provider has, split into *recent* (2026) and *old* (2024/2025). Only 5-star reviews are eligible. The limit is 3 cards.

| Rule | Provider | Recent 5★ | Old 5★ | Expected cards | Composition |
|------|----------|-----------|--------|----------------|-------------|
| 1 | E | 0 | 0 | 0 | Empty (assumption A3) |
| 2 | G | 0 | 1 | 1 | 1 old |
| 3 | H | 0 | 2 | 2 | 2 old |
| 4 | C | 0 | 3 | 3 | 3 old |
| 5 | I | 1 | 0 | 1 | 1 recent |
| 6 | D | 1 | 1 | 2 | 1 recent + 1 old |
| 7 | J | 1 | 3 | 3 | 1 recent + 2 old (1 old hidden) |
| 8 | K | 2 | 0 | 2 | 2 recent |
| 9 | B | 2 | 2 | 3 | 2 recent + 1 old (1 old hidden) |
| 10 | A | 4 | 0 | 3 | 3 recent (1 recent hidden) |

## Why these rules
- Rules 1, 5 and 8 isolate "no filler needed".
- Rules 2, 3, 4 test old reviews alone, including exactly 3 (boundary).
- Rules 6, 7 and 9 test the **filler** logic: old reviews fill only free slots.
- Rule 10 tests the limit with more qualifying reviews than slots.

## Extra traps built into the seed data
- Newer 4-star, 3-star, 2-star and 1-star reviews that must **not** displace older 5-star ones (providers A, B, C, D).
- Reviews on 2025-12-31 and 2026-01-01 to test the year boundary.
- Three 5-star reviews on the same date (provider F) to test the tie-break.

Verified by `automation/oracle.py`: **10 of 10 rules OK**.
