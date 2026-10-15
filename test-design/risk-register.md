# Risk register

Likelihood (L) and impact (I) on a 1 to 3 scale. Score = L x I.

| ID | Type | Risk | L | I | Score | Mitigation |
|----|------|------|---|---|-------|------------|
| R-01 | Product | Filler logic shows old reviews even when recent ones exist | 2 | 3 | 6 | Decision table rules 6, 7, 9 on every release |
| R-02 | Product | Lower-star reviews leak into the collapsed state | 2 | 3 | 6 | Seeded newer 1 to 4★ reviews; automated check A03 |
| R-03 | Product | Year boundary sorts wrongly (2025-12-31 vs 2026-01-01) | 2 | 2 | 4 | Boundary cases TC-REV-007 |
| R-04 | Product | Unstable order on same-day reviews | 2 | 2 | 4 | Tie cases; agree the tie-break with the team |
| R-05 | Product | Infinite scroll duplicates or skips items | 2 | 2 | 4 | Charter CH-1; compare against the oracle |
| R-06 | Product | Fallback appears when it should not, or not when it should | 2 | 2 | 4 | Route interception checks A06, A07 |
| R-07 | Product | Layout breaks on small screens | 2 | 2 | 4 | Mobile project in Playwright; charter CH-2 |
| R-08 | Project | Ambiguous rules (zero 5★ providers, tie-break) | 3 | 2 | 6 | List assumptions early and ask the owners |
| R-09 | Project | No stable design reference or app build for mobile | 2 | 2 | 4 | Request both before execution; mark cases blocked if missing |
| R-10 | Project | Only 3 days and one tester | 3 | 2 | 6 | Risk-based order: high-priority sets first, charters last |
