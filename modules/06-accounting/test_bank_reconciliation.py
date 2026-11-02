from datetime import date
from decimal import Decimal

from bank_reconciliation import DATA_DIR, Transaction, load_transactions, reconcile


def txn(day: int, amount: str, desc: str = "x") -> Transaction:
    return Transaction(date(2026, 10, day), desc, Decimal(amount))


def test_same_amount_within_tolerance_matches():
    result = reconcile([txn(5, "100")], [txn(3, "100")])
    assert len(result.matches) == 1
    assert result.only_in_bank == result.only_in_ledger == []


def test_date_outside_tolerance_does_not_match():
    result = reconcile([txn(10, "100")], [txn(3, "100")])
    assert result.matches == []
    assert len(result.only_in_bank) == len(result.only_in_ledger) == 1


def test_different_amount_does_not_match():
    result = reconcile([txn(5, "100.00")], [txn(5, "100.01")])
    assert result.matches == []


def test_ledger_entry_is_used_only_once():
    result = reconcile([txn(5, "100", "a"), txn(5, "100", "b")], [txn(5, "100")])
    assert len(result.matches) == 1
    assert len(result.only_in_bank) == 1


def test_closest_date_is_preferred():
    near, far = txn(6, "100", "near"), txn(3, "100", "far")
    result = reconcile([txn(5, "100")], [far, near])
    assert result.matches[0][1].description == "near"


def test_sample_data():
    result = reconcile(
        load_transactions(DATA_DIR / "bank_statement.csv", "description"),
        load_transactions(DATA_DIR / "ledger.csv", "reference"),
    )
    assert len(result.matches) == 5
    assert [t.description for t in result.only_in_bank] == ["Bank admin fee", "Interest income"]
    assert [t.description for t in result.only_in_ledger] == [
        "CHQ-5512 Utilities",
        "INV-2050 receipt",
    ]
