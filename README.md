# QA Portfolio: Reviews Component (Testware #002)

An anonymized showcase of how I planned and designed the tests for a reviews component of a health & aesthetics services marketplace. It follows ISO/IEC/IEEE 29119 and ISTQB CTFL 4.0: test plan, conditions, decision table, test cases, risks, a Playwright automation plan and a Python "oracle" that computes the expected result from seeded data. No internal company data, names or links are included.

---

## What this is

A worked example of a test design for a **reviews component** that appears on several pages of a health & aesthetics services marketplace (home page, a reviews page and provider profile pages). The feature has simple-looking rules that hide many edge cases, which makes it a good subject for systematic test design.

All company, product, person and environment names were removed. The seed data is synthetic.

## Rules under test

| # | Rule |
|---|------|
| R1 | Collapsed state shows **at most 3** review cards |
| R2 | Collapsed state shows **5-star reviews only** |
| R3 | Cards are ordered **newest first** |
| R4 | Older 5-star reviews (2024/2025) appear **only to fill free slots** left by recent (2026) ones |
| R5 | Expanded state shows **all ratings**, newest first, with infinite scroll |
| R6 | Every review is linked to a **provider** |
| R7 | A fallback appears **only** for a corrupted image or a slow connection |

Open assumptions are tracked in [`docs/approach.md`](docs/approach.md) (for example: the tie-break for same-day reviews, and what to show when a provider has zero 5-star reviews).

## Repository map

| Path | Content |
|------|---------|
| `docs/approach.md` | Scope, standards, techniques, assumptions, schedule |
| `test-design/decision-table.md` | 10-rule decision table (provider vs. recent/old 5-star counts) |
| `test-design/test-cases.md` | Representative test cases with technique and expected result |
| `test-design/risk-register.md` | Product and project risks with mitigation |
| `data/review_oracle.csv` | 34 synthetic seed reviews across 11 providers |
| `automation/oracle.py` | Computes expected cards from the CSV and checks the decision table |
| `automation/playwright-plan.md` | Plan for 8 Playwright checks (A01 to A08) |
| `automation/tests/reviews.spec.ts` | Skeleton spec with placeholders to adapt to a real app |

## Test design techniques used

- **Equivalence partitioning:** providers grouped by how many recent and old 5-star reviews they have.
- **Boundary value analysis:** 2, 3 and 4 qualifying reviews (limit of 3); reviews on 2025-12-31 and 2026-01-01.
- **Decision table:** 10 rules cover every meaningful combination of recent/old counts.
- **State-based testing:** collapsed to expanded to collapsed, plus loading, slow and error states.
- **Error guessing:** same-day ties, a newer 4-star review that must not displace older 5-star ones, providers with no 5-star review.
- **Exploratory charters:** time-boxed sessions for responsiveness and infinite scroll.

## Running the oracle

Requires Python 3.9 or later. No packages to install.

```bash
python3 -I automation/oracle.py
```

Expected end of output: `10 of 10 rules OK`.

The oracle does two things. It sorts the seed data with the stated rules to get the expected cards for the home page and for each provider. It also checks that the data really has the composition each decision-table rule claims, so a bad edit to the CSV is caught before it can mislead a test.

## Running the Playwright skeleton

```bash
npm init -y
npm i -D @playwright/test
npx playwright install chromium
BASE_URL=https://your-app.example npx playwright test
```

The selectors in the spec are placeholders (`data-testid` names). Replace them with those of the application under test.

## Skills shown

Test planning and estimation, risk-based testing, test design techniques, traceability from rule to condition to case, test data design, oracle thinking, and a first step into UI test automation.

## Status

Design and planning are complete. Execution results are not included because the target application is private.
