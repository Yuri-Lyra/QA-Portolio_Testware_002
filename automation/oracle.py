"""Review Oracle: computes the expected collapsed cards for the Home page
and for each Provider page, from data/review_oracle.csv.

Rules under test (confirmed with the team):
  - collapsed state shows at most LIMIT cards
  - only 5-star reviews
  - newest first; older 5-star reviews only fill free slots
  - tie on date: lower seed id first (an assumption to confirm)

Run:  python3 -I automation/oracle.py
"""
import csv
import sys
from collections import defaultdict
from pathlib import Path

LIMIT = 3
STARS = 5
RECENT_YEAR = 2026  # "recent" = 2026, "old" = 2024/2025 (labels only)

DATA = Path(__file__).resolve().parent.parent / "data" / "review_oracle.csv"


def load():
    with open(DATA, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        r["seed_id"] = int(r["seed_id"])
        r["rating"] = int(r["rating"])
    return rows


def sort_key(r):
    # newest first, then lower seed id first
    return (-int(r["review_date"].replace("-", "")), r["seed_id"])


def collapsed(rows):
    eligible = [r for r in rows if r["rating"] == STARS]
    return sorted(eligible, key=sort_key)[:LIMIT]


def expanded(rows):
    return sorted(rows, key=sort_key)


# Decision table: provider -> (recent 5-star count, old 5-star count)
DECISION_TABLE = {
    1: ("Provider E", 0, 0),
    2: ("Provider G", 0, 1),
    3: ("Provider H", 0, 2),
    4: ("Provider C", 0, 3),
    5: ("Provider I", 1, 0),
    6: ("Provider D", 1, 1),
    7: ("Provider J", 1, 3),
    8: ("Provider K", 2, 0),
    9: ("Provider B", 2, 2),
    10: ("Provider A", 4, 0),
}


def check_decision_table(rows):
    by_provider = defaultdict(list)
    for r in rows:
        by_provider[r["provider"]].append(r)
    failures = 0
    for rule, (prov, recent, old) in DECISION_TABLE.items():
        five = [r for r in by_provider[prov] if r["rating"] == STARS]
        got_recent = sum(1 for r in five if int(r["review_date"][:4]) >= RECENT_YEAR)
        got_old = len(five) - got_recent
        # the data must really have the composition the rule claims
        data_ok = (got_recent, got_old) == (recent, old)
        shown_recent = min(LIMIT, recent)
        shown_old = min(LIMIT - shown_recent, old)
        expected = shown_recent + shown_old
        actual = len(collapsed(by_provider[prov]))
        ok = data_ok and expected == actual
        failures += not ok
        print(f"rule {rule:>2} {prov}: data {got_recent}+{got_old} "
              f"expected {expected} cards, oracle {actual} -> {'OK' if ok else 'CHECK'}")
    return failures


def main():
    rows = load()
    print("HOME (collapsed):", [r["seed_id"] for r in collapsed(rows)])
    by_provider = defaultdict(list)
    for r in rows:
        by_provider[r["provider"]].append(r)
    for prov in sorted(by_provider):
        print(f"{prov} (collapsed):", [r["seed_id"] for r in collapsed(by_provider[prov])],
              "| (expanded):", [r["seed_id"] for r in expanded(by_provider[prov])])
    print()
    failures = check_decision_table(rows)
    print(f"\n{len(DECISION_TABLE) - failures} of {len(DECISION_TABLE)} rules OK")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
