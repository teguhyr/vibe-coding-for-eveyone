"""Marketing: campaign performance report.

CTR  = clicks / impressions        (do people notice the ad?)
CPC  = spend / clicks              (cost of one visit)
CPA  = spend / conversions         (cost of one customer or sale)
ROAS = revenue / spend             (revenue earned per 1 unit spent)
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path

DEFAULT_DATA = Path(__file__).parent / "data" / "campaigns.csv"
DEFAULT_TARGET_ROAS = 2.0


def safe_divide(numerator: float, denominator: float) -> float | None:
    """Return None instead of crashing when there is nothing to divide by."""
    return None if denominator == 0 else numerator / denominator


@dataclass(frozen=True)
class Campaign:
    name: str
    channel: str
    spend: float
    impressions: int
    clicks: int
    conversions: int
    revenue: float

    @property
    def ctr(self) -> float | None:
        return safe_divide(self.clicks, self.impressions)

    @property
    def cpc(self) -> float | None:
        return safe_divide(self.spend, self.clicks)

    @property
    def cpa(self) -> float | None:
        return safe_divide(self.spend, self.conversions)

    @property
    def roas(self) -> float | None:
        return safe_divide(self.revenue, self.spend)


def load_campaigns(path: Path) -> list[Campaign]:
    with path.open(newline="", encoding="utf-8") as f:
        return [
            Campaign(
                name=r["campaign"],
                channel=r["channel"],
                spend=float(r["spend"]),
                impressions=int(r["impressions"]),
                clicks=int(r["clicks"]),
                conversions=int(r["conversions"]),
                revenue=float(r["revenue"]),
            )
            for r in csv.DictReader(f)
        ]


def rank_by_roas(campaigns: list[Campaign]) -> list[Campaign]:
    """Best return first. Campaigns with no spend (ROAS unknown) go last."""
    return sorted(campaigns, key=lambda c: (c.roas is None, -(c.roas or 0)))


def needs_review(campaign: Campaign, target_roas: float = DEFAULT_TARGET_ROAS) -> bool:
    return campaign.roas is not None and campaign.roas < target_roas


def fmt(value: float | None, pattern: str) -> str:
    return "n/a" if value is None else format(value, pattern)


def main() -> None:
    parser = argparse.ArgumentParser(description="Campaign performance report.")
    parser.add_argument("csv_file", nargs="?", type=Path, default=DEFAULT_DATA)
    parser.add_argument("--target-roas", type=float, default=DEFAULT_TARGET_ROAS)
    args = parser.parse_args()

    print(f"{'Campaign':<18} {'Channel':<11} {'CTR':>6} {'CPC':>6} {'CPA':>7} {'ROAS':>6}")
    for c in rank_by_roas(load_campaigns(args.csv_file)):
        flag = "  <-- below target ROAS" if needs_review(c, args.target_roas) else ""
        print(
            f"{c.name:<18} {c.channel:<11} {fmt(c.ctr, '.1%'):>6} {fmt(c.cpc, '.2f'):>6} "
            f"{fmt(c.cpa, '.2f'):>7} {fmt(c.roas, '.1f'):>6}{flag}"
        )


if __name__ == "__main__":
    main()
