"""Latihan Level 2: pemeriksa klaim reimburse (penggantian biaya).

Aturan bisnis (dari tim keuangan, data fiktif):
1. Klaim yang diajukan lebih dari 30 hari setelah tanggal biaya -> REJECTED (late).
2. Klaim >= Rp100.000 tanpa bukti (receipt) -> REJECTED (no receipt).
3. Klaim di atas batas kategori -> PARTIAL, dibayar sebesar batasnya.
4. Selain itu -> APPROVED, dibayar penuh.
Aturan diperiksa berurutan: klaim yang terlambat ditolak walaupun buktinya ada.
"""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from dataclasses import dataclass
from datetime import date
from pathlib import Path

DEFAULT_DATA = Path(__file__).parent / "data" / "klaim_reimburse.csv"
# Rupiah tidak memakai sen dalam praktik, jadi uang disimpan sebagai int.
CATEGORY_LIMITS = {"meal": 150_000, "transport": 500_000, "lodging": 1_200_000}
MAX_SUBMIT_DAYS = 30
RECEIPT_REQUIRED_FROM = 100_000

APPROVED = "APPROVED"
PARTIAL = "PARTIAL"
REJECTED_LATE = "REJECTED: late"
REJECTED_NO_RECEIPT = "REJECTED: no receipt"


@dataclass(frozen=True)
class Claim:
    claim_id: str
    employee_id: str
    department: str
    category: str
    expense_date: date
    submitted_date: date
    amount: int
    has_receipt: bool

    @property
    def days_to_submit(self) -> int:
        return (self.submitted_date - self.expense_date).days


@dataclass(frozen=True)
class Decision:
    claim: Claim
    status: str
    payable: int


def review_claim(claim: Claim) -> Decision:
    if claim.days_to_submit > MAX_SUBMIT_DAYS:
        return Decision(claim, REJECTED_LATE, 0)
    if claim.amount >= RECEIPT_REQUIRED_FROM and not claim.has_receipt:
        return Decision(claim, REJECTED_NO_RECEIPT, 0)
    limit = CATEGORY_LIMITS[claim.category]
    if claim.amount > limit:
        return Decision(claim, PARTIAL, limit)
    return Decision(claim, APPROVED, claim.amount)


def payable_by_department(decisions: list[Decision]) -> dict[str, int]:
    totals: dict[str, int] = defaultdict(int)
    for d in decisions:
        totals[d.claim.department] += d.payable
    return dict(totals)


def parse_yes_no(value: str) -> bool:
    normalized = value.strip().lower()
    if normalized in {"yes", "y"}:
        return True
    if normalized in {"no", "n"}:
        return False
    raise ValueError(f"expected yes/no, got {value!r}")


def parse_claim(row: dict[str, str]) -> Claim:
    claim = Claim(
        claim_id=row["claim_id"],
        employee_id=row["employee_id"],
        department=row["department"],
        category=row["category"].strip().lower(),
        expense_date=date.fromisoformat(row["expense_date"]),
        submitted_date=date.fromisoformat(row["submitted_date"]),
        amount=int(row["amount"]),
        has_receipt=parse_yes_no(row["receipt"]),
    )
    if claim.category not in CATEGORY_LIMITS:
        raise ValueError(f"unknown category {row['category']!r}")
    if claim.amount <= 0:
        raise ValueError(f"amount must be positive, got {claim.amount}")
    if claim.submitted_date < claim.expense_date:
        raise ValueError("submitted before the expense date")
    return claim


def load_claims(path: Path) -> list[Claim]:
    claims = []
    with path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            try:
                claims.append(parse_claim(row))
            except ValueError as error:
                # Sebutkan ID klaim agar baris yang salah mudah ditemukan di CSV.
                raise ValueError(f"{row['claim_id']}: {error}") from error
    return claims


def main() -> None:
    parser = argparse.ArgumentParser(description="Expense claim checker.")
    parser.add_argument("csv_file", nargs="?", type=Path, default=DEFAULT_DATA)
    args = parser.parse_args()

    decisions = [review_claim(c) for c in load_claims(args.csv_file)]
    print(f"{'Claim':<6} {'Emp':<5} {'Category':<10} {'Amount':>10} {'Payable':>10}  Status")
    for d in decisions:
        c = d.claim
        print(
            f"{c.claim_id:<6} {c.employee_id:<5} {c.category:<10} "
            f"{c.amount:>10,} {d.payable:>10,}  {d.status}"
        )

    print("\nPayable by department")
    totals = payable_by_department(decisions)
    for department, total in totals.items():
        print(f"{department:<12} {total:>10,}")
    print(f"{'TOTAL':<12} {sum(totals.values()):>10,}")


if __name__ == "__main__":
    main()
