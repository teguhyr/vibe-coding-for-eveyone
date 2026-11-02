"""Procurement: score vendor quotes and recommend the best vendor per item.

Each quote is scored 0-1 on three criteria, compared with the other quotes for
the same item (min-max normalization):
- price:     cheapest = 1, most expensive = 0
- lead time: fastest  = 1, slowest        = 0
- quality:   best     = 1, worst          = 0
The final score is a weighted sum. The weights reflect company priorities.
"""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

DEFAULT_DATA = Path(__file__).parent / "data" / "quotes.csv"
WEIGHTS = {"price": 0.5, "lead_time": 0.3, "quality": 0.2}


@dataclass(frozen=True)
class Quote:
    item: str
    vendor: str
    unit_price: float
    lead_time_days: int
    quality_rating: float


def normalize(value: float, values: list[float], higher_is_better: bool) -> float:
    """Scale value to 0-1 relative to the others. All equal -> everyone gets 1."""
    low, high = min(values), max(values)
    if high == low:
        return 1.0
    scaled = (value - low) / (high - low)
    return scaled if higher_is_better else 1 - scaled


def score_quotes(
    quotes: list[Quote], weights: dict[str, float] = WEIGHTS
) -> list[tuple[Quote, float]]:
    """Score quotes for ONE item. Returns (quote, score) pairs, best first."""
    if abs(sum(weights.values()) - 1) > 1e-9:
        raise ValueError(f"Weights must add up to 1, got {sum(weights.values())}")
    prices = [q.unit_price for q in quotes]
    leads = [float(q.lead_time_days) for q in quotes]
    ratings = [q.quality_rating for q in quotes]

    scored = [
        (
            q,
            weights["price"] * normalize(q.unit_price, prices, higher_is_better=False)
            + weights["lead_time"] * normalize(q.lead_time_days, leads, higher_is_better=False)
            + weights["quality"] * normalize(q.quality_rating, ratings, higher_is_better=True),
        )
        for q in quotes
    ]
    return sorted(scored, key=lambda pair: pair[1], reverse=True)


def group_by_item(quotes: list[Quote]) -> dict[str, list[Quote]]:
    groups: dict[str, list[Quote]] = defaultdict(list)
    for q in quotes:
        groups[q.item].append(q)
    return dict(groups)


def load_quotes(path: Path) -> list[Quote]:
    with path.open(newline="", encoding="utf-8") as f:
        return [
            Quote(
                r["item"],
                r["vendor"],
                float(r["unit_price"]),
                int(r["lead_time_days"]),
                float(r["quality_rating"]),
            )
            for r in csv.DictReader(f)
        ]


def main() -> None:
    parser = argparse.ArgumentParser(description="Score vendor quotes per item.")
    parser.add_argument("csv_file", nargs="?", type=Path, default=DEFAULT_DATA)
    args = parser.parse_args()

    weights_text = ", ".join(f"{k} {v:.0%}" for k, v in WEIGHTS.items())
    print(f"Weights: {weights_text}")
    for item, quotes in group_by_item(load_quotes(args.csv_file)).items():
        print(f"\n{item}")
        for rank, (q, score) in enumerate(score_quotes(quotes), start=1):
            marker = "  <-- recommended" if rank == 1 else ""
            print(
                f"  {rank}. {q.vendor:<9} price {q.unit_price:>12,.0f}  "
                f"lead {q.lead_time_days:>2}d  "
                f"quality {q.quality_rating:.1f}  score {score:.2f}{marker}"
            )


if __name__ == "__main__":
    main()
