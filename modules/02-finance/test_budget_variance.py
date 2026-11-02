from decimal import Decimal

from budget_variance import DEFAULT_DATA, BudgetLine, department_totals, load_lines, status


def line(budget: str, actual: str, dept: str = "Ops") -> BudgetLine:
    return BudgetLine(dept, "Test", Decimal(budget), Decimal(actual))


def test_positive_variance_means_overspent():
    assert line("100", "120").variance == Decimal("20")
    assert line("100", "120").variance_pct == Decimal("20")


def test_status_respects_threshold_boundaries():
    assert status(line("100", "110")) == "OK"  # exactly 10% is still OK
    assert status(line("100", "110.01")) == "OVER"
    assert status(line("100", "89.99")) == "UNDER"


def test_zero_budget_is_flagged_as_unbudgeted_not_crash():
    assert line("0", "50").variance_pct is None
    assert status(line("0", "50")) == "UNBUDGETED"
    assert status(line("0", "0")) == "OK"


def test_decimal_avoids_float_rounding_errors():
    assert line("0.30", "0.10").variance + Decimal("0.20") == 0


def test_department_totals_sum_each_department():
    totals = department_totals(
        [line("100", "90", "A"), line("50", "70", "A"), line("10", "10", "B")]
    )
    assert totals["A"].budget == Decimal("150")
    assert totals["A"].actual == Decimal("160")
    assert totals["B"].variance == 0


def test_sample_data():
    statuses = {f"{ln.department}/{ln.category}": status(ln) for ln in load_lines(DEFAULT_DATA)}
    assert statuses == {
        "Operations/Fuel": "OVER",
        "Operations/Maintenance": "OK",
        "Marketing/Digital Ads": "UNDER",
        "Marketing/Events": "OK",
        "HR/Training": "OVER",
        "IT/Software Licenses": "OK",
        "IT/Cloud Hosting": "UNBUDGETED",
    }
