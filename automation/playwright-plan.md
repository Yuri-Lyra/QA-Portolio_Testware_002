# Playwright plan

## Why automate these checks
The collapsed-state rules are deterministic and are repeated on every release. A script is faster and never forgets the edge cases. Visual judgement (spacing, look and feel) stays manual.

## Why an oracle
Hard-coding "3 cards" would pass even if the wrong 3 appear. The oracle (`oracle.py`) computes the exact expected seed IDs from the data, so the test checks **which** cards are shown, not just how many.

## Checks

| ID | What it checks | Technique used in Playwright |
|----|----------------|------------------------------|
| A01 | Home page collapsed: 3 cards | `toHaveCount(3)` |
| A02 | Home page cards are the expected ones in the expected order | `allTextContents()` compared with the oracle |
| A03 | Only 5-star cards in collapsed state | Count star elements per card |
| A04 | Provider B: 2 recent + 1 old | Compare card dates with the oracle |
| A05 | Provider E: no broken layout when there is no 5★ | Assert the section follows the confirmed behaviour |
| A06 | Corrupted image shows the fallback | `page.route()` aborts the image request |
| A07 | Slow connection shows a placeholder, then real cards | `page.route()` delays the API response |
| A08 | Mobile viewport shows the same 3 cards | Mobile project with the iPhone 13 preset |

## Practical notes
- Use `data-testid` attributes; ask developers to add them if missing.
- Run the oracle first in CI; if it fails, the data is wrong and the UI tests would be meaningless.
- Keep tests independent: each opens its own page.
- Expected IDs are placeholders until the app exposes the seed ID in the DOM (for example `data-review-id`).
