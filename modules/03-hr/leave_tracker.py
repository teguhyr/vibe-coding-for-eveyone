"""HR: annual leave balance tracker.

Counts working days (Monday to Friday, excluding public holidays) in each
approved leave request, then compares the total with each employee's entitlement.
"""

from __future__ import annotations

import argparse
import csv
from collections.abc import Iterable
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
VALID_STATUSES = {"approved", "pending", "rejected"}


@dataclass(frozen=True)
class Employee:
    employee_id: str
    name: str
    department: str
    annual_entitlement: int


@dataclass(frozen=True)
class LeaveRequest:
    employee_id: str
    start_date: date
    end_date: date
    status: str


@dataclass(frozen=True)
class Balance:
    employee: Employee
    used: int
    pending: int

    @property
    def remaining(self) -> int:
        return self.employee.annual_entitlement - self.used


def working_days(start: date, end: date, holidays: Iterable[date] = ()) -> int:
    """Count Monday-Friday days from start to end (both included), skipping holidays."""
    if end < start:
        raise ValueError(f"Leave ends ({end}) before it starts ({start})")
    holiday_set = set(holidays)
    days = 0
    current = start
    while current <= end:
        if current.weekday() < 5 and current not in holiday_set:  # 0=Mon ... 4=Fri
            days += 1
        current += timedelta(days=1)
    return days


def calculate_balances(
    employees: list[Employee], requests: list[LeaveRequest], holidays: Iterable[date] = ()
) -> list[Balance]:
    holiday_set = set(holidays)
    used = {e.employee_id: 0 for e in employees}
    pending = {e.employee_id: 0 for e in employees}

    for req in requests:
        if req.employee_id not in used:
            raise ValueError(f"Leave request for unknown employee {req.employee_id}")
        days = working_days(req.start_date, req.end_date, holiday_set)
        if req.status == "approved":
            used[req.employee_id] += days
        elif req.status == "pending":
            pending[req.employee_id] += days

    return [Balance(e, used[e.employee_id], pending[e.employee_id]) for e in employees]


def load_employees(path: Path) -> list[Employee]:
    with path.open(newline="", encoding="utf-8") as f:
        return [
            Employee(r["employee_id"], r["name"], r["department"], int(r["annual_entitlement"]))
            for r in csv.DictReader(f)
        ]


def load_requests(path: Path) -> list[LeaveRequest]:
    requests = []
    with path.open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            status = r["status"].strip().lower()
            if status not in VALID_STATUSES:
                raise ValueError(f"Unknown leave status {r['status']!r} for {r['employee_id']}")
            requests.append(
                LeaveRequest(
                    r["employee_id"],
                    date.fromisoformat(r["start_date"]),
                    date.fromisoformat(r["end_date"]),
                    status,
                )
            )
    return requests


def load_holidays(path: Path) -> list[date]:
    with path.open(newline="", encoding="utf-8") as f:
        return [date.fromisoformat(r["date"]) for r in csv.DictReader(f)]


def main() -> None:
    parser = argparse.ArgumentParser(description="Annual leave balance tracker.")
    parser.add_argument("--data-dir", type=Path, default=DATA_DIR)
    args = parser.parse_args()

    balances = calculate_balances(
        load_employees(args.data_dir / "employees.csv"),
        load_requests(args.data_dir / "leave_requests.csv"),
        load_holidays(args.data_dir / "holidays.csv"),
    )

    print(
        f"{'ID':<5} {'Name':<14} {'Dept':<11} "
        f"{'Entitled':>8} {'Used':>5} {'Left':>5} {'Pending':>7}"
    )
    for b in balances:
        flag = "  <-- OVER ENTITLEMENT" if b.remaining < 0 else ""
        print(
            f"{b.employee.employee_id:<5} {b.employee.name:<14} {b.employee.department:<11} "
            f"{b.employee.annual_entitlement:>8} {b.used:>5} {b.remaining:>5} {b.pending:>7}{flag}"
        )


if __name__ == "__main__":
    main()
