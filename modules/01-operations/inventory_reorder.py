"""Operations: flag inventory items that need reordering.

Reorder point = (average daily usage x supplier lead time) + safety stock.
When stock on hand falls to the reorder point or below, it is time to order.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path

DEFAULT_DATA = Path(__file__).parent / "data" / "inventory.csv"


@dataclass(frozen=True)
class Item:
    sku: str
    name: str
    on_hand: int
    avg_daily_usage: float
    lead_time_days: int
    safety_stock: int

    @property
    def reorder_point(self) -> float:
        # Stock needed to survive until the next delivery arrives, plus a buffer.
        return self.avg_daily_usage * self.lead_time_days + self.safety_stock

    @property
    def days_of_cover(self) -> float:
        """How many days the current stock lasts at the usual usage rate."""
        if self.avg_daily_usage == 0:
            return float("inf")
        return self.on_hand / self.avg_daily_usage


def load_items(path: Path) -> list[Item]:
    with path.open(newline="", encoding="utf-8") as f:
        return [
            Item(
                sku=row["sku"],
                name=row["name"],
                on_hand=int(row["on_hand"]),
                avg_daily_usage=float(row["avg_daily_usage"]),
                lead_time_days=int(row["lead_time_days"]),
                safety_stock=int(row["safety_stock"]),
            )
            for row in csv.DictReader(f)
        ]


def items_to_reorder(items: list[Item]) -> list[Item]:
    """Items at or below their reorder point, most urgent (fewest days of cover) first."""
    due = [item for item in items if item.on_hand <= item.reorder_point]
    return sorted(due, key=lambda item: item.days_of_cover)


def main() -> None:
    parser = argparse.ArgumentParser(description="Flag inventory items that need reordering.")
    parser.add_argument("csv_file", nargs="?", type=Path, default=DEFAULT_DATA)
    args = parser.parse_args()

    due = items_to_reorder(load_items(args.csv_file))
    if not due:
        print("All items are above their reorder point.")
        return

    print(f"{'SKU':<8} {'Item':<20} {'On hand':>8} {'Reorder pt':>10} {'Days left':>9}")
    for item in due:
        print(
            f"{item.sku:<8} {item.name:<20} {item.on_hand:>8} "
            f"{item.reorder_point:>10.0f} {item.days_of_cover:>9.1f}"
        )


if __name__ == "__main__":
    main()
