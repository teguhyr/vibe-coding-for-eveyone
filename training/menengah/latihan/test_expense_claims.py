# Tes awal untuk expense_claims.py. Di Modul 2 Anda menambah tes kasus tepi di file ini.
from datetime import date

from expense_claims import APPROVED, PARTIAL, REJECTED_LATE, Claim, review_claim


def claim(category="meal", amount=50_000, days_late=1, receipt=True) -> Claim:
    expense = date(2026, 10, 1)
    submitted = date.fromordinal(expense.toordinal() + days_late)
    return Claim("T-1", "K999", "Test", category, expense, submitted, amount, receipt)


def test_normal_claim_is_paid_in_full():
    decision = review_claim(claim(amount=50_000))
    assert (decision.status, decision.payable) == (APPROVED, 50_000)


def test_claim_above_limit_is_capped():
    decision = review_claim(claim(category="transport", amount=650_000))
    assert (decision.status, decision.payable) == (PARTIAL, 500_000)


def test_late_claim_is_rejected():
    decision = review_claim(claim(days_late=45))
    assert (decision.status, decision.payable) == (REJECTED_LATE, 0)
