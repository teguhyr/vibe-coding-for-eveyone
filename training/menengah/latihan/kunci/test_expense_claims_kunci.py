# Kunci Latihan 2.2-2.4: tes kasus tepi untuk expense_claims.py.
from datetime import date

import pytest
from expense_claims import (
    APPROVED,
    DEFAULT_DATA,
    PARTIAL,
    REJECTED_LATE,
    REJECTED_NO_RECEIPT,
    Claim,
    load_claims,
    payable_by_department,
    review_claim,
)


def claim(category="meal", amount=50_000, days_late=1, receipt=True) -> Claim:
    expense = date(2026, 10, 1)
    submitted = date.fromordinal(expense.toordinal() + days_late)
    return Claim("T-1", "K999", "Test", category, expense, submitted, amount, receipt)


def test_submitted_exactly_30_days_later_is_still_on_time():
    assert review_claim(claim(days_late=30)).status == APPROVED


def test_submitted_31_days_later_is_late():
    assert review_claim(claim(days_late=31)).status == REJECTED_LATE


def test_exactly_at_limit_is_paid_in_full():
    decision = review_claim(claim(category="lodging", amount=1_200_000))
    assert (decision.status, decision.payable) == (APPROVED, 1_200_000)


def test_one_rupiah_above_limit_is_capped():
    decision = review_claim(claim(category="lodging", amount=1_200_001))
    assert (decision.status, decision.payable) == (PARTIAL, 1_200_000)


def test_receipt_is_required_from_exactly_100_000():
    assert review_claim(claim(amount=100_000, receipt=False)).status == REJECTED_NO_RECEIPT
    assert review_claim(claim(amount=99_999, receipt=False)).status == APPROVED


def test_late_rule_wins_over_missing_receipt():
    decision = review_claim(claim(amount=200_000, days_late=40, receipt=False))
    assert decision.status == REJECTED_LATE


@pytest.mark.parametrize(
    ("column", "bad_value", "message"),
    [
        ("category", "meals", "unknown category"),
        ("receipt", "ya", "expected yes/no"),
        ("amount", "0", "must be positive"),
        ("expense_date", "2026-10-32", "day is out of range"),
    ],
)
def test_bad_rows_name_the_claim_id(tmp_path, column, bad_value, message):
    row = {
        "claim_id": "X-9",
        "employee_id": "K1",
        "department": "Test",
        "category": "meal",
        "expense_date": "2026-10-01",
        "submitted_date": "2026-10-02",
        "amount": "50000",
        "receipt": "yes",
    }
    row[column] = bad_value
    csv_file = tmp_path / "claims.csv"
    csv_file.write_text(",".join(row) + "\n" + ",".join(row.values()) + "\n", encoding="utf-8")
    with pytest.raises(ValueError, match=f"X-9: .*{message}"):
        load_claims(csv_file)


def test_sample_data():
    decisions = [review_claim(c) for c in load_claims(DEFAULT_DATA)]
    assert [d.status for d in decisions] == [
        APPROVED,
        PARTIAL,
        REJECTED_LATE,
        APPROVED,
        REJECTED_NO_RECEIPT,
        APPROVED,
        APPROVED,
        PARTIAL,
    ]
    assert payable_by_department(decisions) == {
        "Sales": 620_000,
        "Finance": 1_200_000,
        "IT": 85_000,
        "Operations": 1_500_000,
    }
