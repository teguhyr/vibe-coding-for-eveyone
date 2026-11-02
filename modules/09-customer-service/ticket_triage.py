"""Customer service: triage incoming messages by keyword.

Each message gets a category (the one with the most keyword hits) and an
urgency flag. Rules are simple and transparent, a good first step before
trying AI-based classification.
"""

from __future__ import annotations

import argparse
import csv
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

DEFAULT_DATA = Path(__file__).parent / "data" / "messages.csv"

# Order matters: on a tie, the category listed first wins.
CATEGORY_KEYWORDS: dict[str, list[str]] = {
    "billing": ["invoice", "refund", "charge", "charged", "payment", "bill", "billing"],
    "delivery": [
        "delivery",
        "shipping",
        "courier",
        "package",
        "parcel",
        "late",
        "arrived",
        "tracking",
    ],
    "technical": ["error", "crash", "crashes", "bug", "not working", "slow", "broken"],
    "account": ["account", "password", "login", "log in", "sign in", "username"],
}
URGENT_KEYWORDS = ["urgent", "asap", "immediately", "emergency"]
OTHER = "other"


@dataclass(frozen=True)
class Triage:
    ticket_id: str
    channel: str
    category: str
    urgent: bool


def count_hits(text: str, keywords: list[str]) -> int:
    # \b = word boundary, so "late" does not match inside "translate".
    return sum(1 for kw in keywords if re.search(rf"\b{re.escape(kw)}\b", text))


def categorize(message: str) -> str:
    text = message.lower()
    hits = {category: count_hits(text, kws) for category, kws in CATEGORY_KEYWORDS.items()}
    best = max(hits, key=lambda category: hits[category])  # first one wins on a tie
    return best if hits[best] > 0 else OTHER


def is_urgent(message: str) -> bool:
    return count_hits(message.lower(), URGENT_KEYWORDS) > 0


def triage(rows: list[dict[str, str]]) -> list[Triage]:
    return [
        Triage(r["ticket_id"], r["channel"], categorize(r["message"]), is_urgent(r["message"]))
        for r in rows
    ]


def main() -> None:
    parser = argparse.ArgumentParser(description="Triage customer messages by keyword.")
    parser.add_argument("csv_file", nargs="?", type=Path, default=DEFAULT_DATA)
    args = parser.parse_args()

    with args.csv_file.open(newline="", encoding="utf-8") as f:
        results = triage(list(csv.DictReader(f)))

    # Urgent first, then by category, so agents see the most pressing work at the top.
    for t in sorted(results, key=lambda t: (not t.urgent, t.category)):
        print(f"{'URGENT' if t.urgent else '':<7}{t.ticket_id:<7} {t.channel:<9} {t.category}")

    print("\nMessages per category")
    for category, count in Counter(t.category for t in results).most_common():
        print(f"  {category:<10} {count}")


if __name__ == "__main__":
    main()
