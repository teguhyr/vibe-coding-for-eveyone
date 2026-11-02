from datetime import date

import pytest
from contract_renewals import (
    ACT_NOW,
    DEFAULT_DATA,
    EXPIRED,
    NOTICE_PASSED,
    OK,
    Contract,
    contract_status,
    contracts_needing_attention,
    load_contracts,
    parse_yes_no,
)

TODAY = date(2026, 11, 2)


def contract(end: str, notice_days: int = 30) -> Contract:
    return Contract("C", "Counterparty", "Service", date.fromisoformat(end), notice_days, True)


def test_notice_deadline_is_end_date_minus_notice_days():
    assert contract("2027-01-31", 30).notice_deadline == date(2027, 1, 1)


def test_status_for_each_situation():
    assert contract_status(contract("2026-11-01"), TODAY) == EXPIRED
    assert contract_status(contract("2026-11-20", 30), TODAY) == NOTICE_PASSED
    assert contract_status(contract("2026-12-15", 30), TODAY) == ACT_NOW
    assert contract_status(contract("2027-12-31", 30), TODAY) == OK


def test_deadline_on_last_day_of_window_is_act_now():
    # Deadline 2027-01-01 is exactly 60 days after TODAY.
    assert contract_status(contract("2027-01-31", 30), TODAY, window_days=60) == ACT_NOW


def test_deadline_today_is_still_act_now():
    assert contract_status(contract("2026-12-02", 30), TODAY) == ACT_NOW


def test_parse_yes_no_rejects_unclear_values():
    assert parse_yes_no(" Yes ") is True
    assert parse_yes_no("no") is False
    with pytest.raises(ValueError):
        parse_yes_no("maybe")


def test_sample_data():
    flagged = contracts_needing_attention(load_contracts(DEFAULT_DATA), TODAY)
    assert [(c.contract_id, s) for c, s in flagged] == [
        ("CTR-003", EXPIRED),
        ("CTR-002", NOTICE_PASSED),
        ("CTR-001", ACT_NOW),
        ("CTR-005", ACT_NOW),
    ]
