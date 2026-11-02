"""Accounting: bank reconciliation.

Matches each bank statement line to a ledger (book) entry with the same amount
and a date within a few days. Whatever is left unmatched needs attention:
- only in the bank:   e.g. bank fees or interest not yet recorded in the books
- only in the ledger: e.g. uncleared cheques or deposits in transit
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass, field
from datetime import date
from decimal import Decimal
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
DEFAULT_DATE_TOLERANCE_DAYS = 3


@dataclass(frozen=True)
class Transaction:
    txn_date: date
    description: str
    amount: Decimal  # positive = money in, negative = money out


@dataclass
class ReconciliationResult:
    matches: list[tuple[Transaction, Transaction]] = field(default_factory=list)
    only_in_bank: list[Transaction] = field(default_factory=list)
    only_in_ledger: list[Transaction] = field(default_factory=list)


def reconcile(
    bank: list[Transaction],
    ledger: list[Transaction],
    date_tolerance_days: int = DEFAULT_DATE_TOLERANCE_DAYS,
) -> ReconciliationResult:
    result = ReconciliationResult()
    unmatched_ledger = list(ledger)

    for bank_txn in sorted(bank, key=lambda t: t.txn_date):
        candidates = [
            entry
            for entry in unmatched_ledger
            if entry.amount == bank_txn.amount
            and abs((entry.txn_date - bank_txn.txn_date).days) <= date_tolerance_days
        ]
        if not candidates:
            result.only_in_bank.append(bank_txn)
            continue
        # If several entries qualify, take the one closest in date.
        best = min(candidates, key=lambda e: abs((e.txn_date - bank_txn.txn_date).days))
        unmatched_ledger.remove(best)  # each ledger entry can be matched only once
        result.matches.append((bank_txn, best))

    result.only_in_ledger = unmatched_ledger
    return result


def load_transactions(path: Path, description_column: str) -> list[Transaction]:
    with path.open(newline="", encoding="utf-8") as f:
        return [
            Transaction(date.fromisoformat(r["date"]), r[description_column], Decimal(r["amount"]))
            for r in csv.DictReader(f)
        ]


def print_section(title: str, txns: list[Transaction]) -> None:
    print(f"\n{title} ({len(txns)})")
    for t in txns:
        print(f"  {t.txn_date}  {t.description:<28} {t.amount:>12,.2f}")
    print(f"  {'Total':<40} {sum((t.amount for t in txns), Decimal(0)):>12,.2f}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Bank reconciliation.")
    parser.add_argument("--data-dir", type=Path, default=DATA_DIR)
    parser.add_argument("--tolerance", type=int, default=DEFAULT_DATE_TOLERANCE_DAYS)
    args = parser.parse_args()

    bank = load_transactions(args.data_dir / "bank_statement.csv", "description")
    ledger = load_transactions(args.data_dir / "ledger.csv", "reference")
    result = reconcile(bank, ledger, args.tolerance)

    print(f"Matched: {len(result.matches)} of {len(bank)} bank lines")
    print_section("In bank, not in ledger -> record in the books", result.only_in_bank)
    print_section("In ledger, not in bank -> check timing or errors", result.only_in_ledger)


if __name__ == "__main__":
    main()
