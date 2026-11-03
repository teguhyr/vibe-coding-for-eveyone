# Tes untuk overtime_pay.py. Satu tes SENGAJA gagal: temukan bug-nya di Modul 3.
import pytest
from overtime_pay import overtime_pay

WAGE = 5_190_000  # upah per jam tepat Rp30.000 (5.190.000 / 173)


def test_first_hour_is_one_and_a_half_times():
    assert overtime_pay(WAGE, 1) == 45_000


def test_next_hours_are_double():
    assert overtime_pay(WAGE, 3) == 45_000 + 2 * 60_000


def test_zero_hours_pays_nothing():
    assert overtime_pay(WAGE, 0) == 0


def test_more_than_four_hours_is_an_error():
    with pytest.raises(ValueError, match="4 hours"):
        overtime_pay(WAGE, 5)
