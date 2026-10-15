import { test, expect } from '@playwright/test';

// Skeleton: replace the base URL, paths and test ids with those of the real application.
// Expected seed IDs come from automation/oracle.py (HOME collapsed: 1, 7, 3).

const HOME = '/';
const CARD = '[data-testid="review-card"]';
const EXPECTED_HOME_IDS = ['1', '7', '3'];

test.describe('Reviews component, collapsed state', () => {
  test('A01 home page shows exactly 3 cards', async ({ page }) => {
    await page.goto(HOME);
    await expect(page.locator(CARD)).toHaveCount(3);
  });

  test('A02 home page shows the expected cards in order', async ({ page }) => {
    await page.goto(HOME);
    const ids = await page.locator(CARD).evaluateAll((els) =>
      els.map((el) => el.getAttribute('data-review-id')),
    );
    expect(ids).toEqual(EXPECTED_HOME_IDS);
  });

  test('A06 corrupted image shows the fallback', async ({ page }) => {
    await page.route('**/*.{png,jpg,jpeg,webp}', (route) => route.abort());
    await page.goto(HOME);
    await expect(page.locator('[data-testid="review-avatar-fallback"]').first()).toBeVisible();
  });

  test('A07 slow connection shows a placeholder, then the cards', async ({ page }) => {
    await page.route('**/api/reviews*', async (route) => {
      await new Promise((r) => setTimeout(r, 3000));
      await route.continue();
    });
    await page.goto(HOME);
    await expect(page.locator('[data-testid="reviews-loading"]')).toBeVisible();
    await expect(page.locator(CARD)).toHaveCount(3);
  });
});
