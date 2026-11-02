from datetime import date

import pytest
from leave_tracker import (
    DATA_DIR,
    Employee,
    LeaveRequest,
    calculate_balances,
    load_employees,
    load_holidays,
    load_requests,
    working_days,
)


def test_full_week_is_five_working_days():
    assert working_days(date(2026, 11, 2), date(2026, 11, 6)) == 5  # Mon-Fri


def test_weekend_is_not_counted():
    assert working_days(date(2026, 10, 30), date(2026, 11, 3)) == 3  # Fri-Tue


def test_single_day_leave():
    assert working_days(date(2026, 11, 2), date(2026, 11, 2)) == 1


def test_public_holiday_is_not_counted():
    week = (date(2026, 8, 17), date(2026, 8, 21))
    assert working_days(*week, holidays=[date(2026, 8, 17)]) == 4


def test_end_before_start_is_an_error():
    with pytest.raises(ValueError):
        working_days(date(2026, 11, 6), date(2026, 11, 2))


def test_only_approved_leave_reduces_balance():
    emp = Employee("E1", "Test", "Ops", 12)
    requests = [
        LeaveRequest("E1", date(2026, 11, 2), date(2026, 11, 3), "approved"),
        LeaveRequest("E1", date(2026, 11, 4), date(2026, 11, 4), "pending"),
        LeaveRequest("E1", date(2026, 11, 5), date(2026, 11, 6), "rejected"),
    ]
    [balance] = calculate_balances([emp], requests)
    assert (balance.used, balance.pending, balance.remaining) == (2, 1, 10)


def test_unknown_employee_is_an_error():
    request = LeaveRequest("E9", date(2026, 11, 2), date(2026, 11, 2), "approved")
    with pytest.raises(ValueError, match="E9"):
        calculate_balances([], [request])


def test_sample_data():
    balances = calculate_balances(
        load_employees(DATA_DIR / "employees.csv"),
        load_requests(DATA_DIR / "leave_requests.csv"),
        load_holidays(DATA_DIR / "holidays.csv"),
    )
    summary = {b.employee.employee_id: (b.used, b.remaining, b.pending) for b in balances}
    assert summary == {
        "E001": (9, 3, 0),
        "E002": (10, 2, 4),
        "E003": (3, 12, 0),
        "E004": (13, -1, 0),
    }
