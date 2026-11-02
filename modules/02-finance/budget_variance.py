"""Finance: budget vs. actual variance report.

Variance   = actual - budget        (positive means overspent)
Variance % = variance / budget x 100
Lines whose variance % is beyond the threshold (default 10%) are flagged.
"""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from dataclasses import dataclass
from decimal import Decimal
from pathlib import Path

DEFAULT_DATA = Path(__file__).parent / "data" / "budget_vs_actual.csv"
DEFAULT_THRESHOLD_PCT = Decimal("10")


@dataclass(frozen=True)
class BudgetLine:
    department: str
    category: str
    budget: Decimal
    actual: Decimal

    @property
    def variance(self) -> Decimal:
        return self.actual - self.budget

    @property
    def variance_pct(self) -> Decimal | None:
        """None when there is no budget, because a percentage of zero is meaningless."""
        if self.budget == 0:
            return None
        return self.variance / self.budget * 100


def status(line: BudgetLine, threshold_pct: Decimal = DEFAULT_THRESHOLD_PCT) -> str:
    pct = line.variance_pct
    if pct is None:
        return "UNBUDGETED" if line.actual else "OK"
    if pct > threshold_pct:
        return "OVER"
    if pct < -threshold_pct:
        return "UNDER"
    return "OK"


def load_lines(path: Path) -> list[BudgetLine]:
    # Decimal, not float: float cannot store 0.1 exactly, which causes cent-level errors.
    with path.open(newline="", encoding="utf-8") as f:
        return [
            BudgetLine(
                department=row["department"],
                category=row["category"],
                budget=Decimal(row["budget"]),
                actual=Decimal(row["actual"]),
            )
            for row in csv.DictReader(f)
        ]


def department_totals(lines: list[BudgetLine]) -> dict[str, BudgetLine]:
    budgets: dict[str, Decimal] = defaultdict(Decimal)
    actuals: dict[str, Decimal] = defaultdict(Decimal)
    for line in lines:
        budgets[line.department] += line.budget
        actuals[line.department] += line.actual
    return {dept: BudgetLine(dept, "TOTAL", budgets[dept], actuals[dept]) for dept in budgets}


def format_pct(pct: Decimal | None) -> str:
    return "n/a" if pct is None else f"{pct:+.1f}%"


def main() -> None:
    parser = argparse.ArgumentParser(description="Budget vs. actual variance report.")
    parser.add_argument("csv_file", nargs="?", type=Path, default=DEFAULT_DATA)
    parser.add_argument("--threshold", type=Decimal, default=DEFAULT_THRESHOLD_PCT)
    args = parser.parse_args()

    lines = load_lines(args.csv_file)
    header = (
        f"{'Department':<12} {'Category':<18} {'Budget':>11} {'Actual':>11} "
        f"{'Variance':>11} {'Var %':>8}  Status"
    )
    print(header)
    print("-" * len(header))
    for line in lines:
        print(
            f"{line.department:<12} {line.category:<18} "
            f"{line.budget:>11,.2f} {line.actual:>11,.2f} {line.variance:>+11,.2f} "
            f"{format_pct(line.variance_pct):>8}  {status(line, args.threshold)}"
        )

    print("\nTotals by department")
    for total in department_totals(lines).values():
        print(
            f"{total.department:<12} {total.budget:>11,.2f} {total.actual:>11,.2f} "
            f"{total.variance:>+11,.2f} {format_pct(total.variance_pct):>8}"
        )


if __name__ == "__main__":
    main()
