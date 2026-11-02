from datetime import datetime

import pytest
from ticket_sla import DEFAULT_DATA, Ticket, compliance_by_priority, is_breached, load_tickets

NOW = datetime(2026, 11, 2, 12, 0)


def ticket(priority="P1", opened="2026-11-02T08:00", resolved=None) -> Ticket:
    return Ticket(
        "T",
        priority,
        "Test",
        datetime.fromisoformat(opened),
        datetime.fromisoformat(resolved) if resolved else None,
    )


def test_resolved_exactly_at_sla_is_not_a_breach():
    assert not is_breached(ticket("P1", resolved="2026-11-02T12:00"), NOW)


def test_resolved_after_sla_is_a_breach():
    assert is_breached(ticket("P1", resolved="2026-11-02T12:01"), NOW)


def test_open_ticket_is_measured_against_now():
    assert not is_breached(ticket("P2"), NOW)  # open 4h, SLA 8h
    assert is_breached(ticket("P1", opened="2026-11-02T07:00"), NOW)  # open 5h, SLA 4h


def test_compliance_is_share_within_sla():
    ok = ticket("P1", resolved="2026-11-02T09:00")
    late = ticket("P1", resolved="2026-11-02T13:00")
    assert compliance_by_priority([ok, late], NOW) == {"P1": 0.5}


def test_unknown_priority_is_rejected(tmp_path):
    bad = tmp_path / "bad.csv"
    bad.write_text(
        "ticket_id,priority,category,opened_at,resolved_at\nX,P9,Test,2026-11-02T08:00,\n"
    )
    with pytest.raises(ValueError, match="P9"):
        load_tickets(bad)


def test_sample_data():
    tickets = load_tickets(DEFAULT_DATA)
    assert [t.ticket_id for t in tickets if is_breached(t, NOW)] == [
        "INC-1002",
        "INC-1004",
        "INC-1006",
    ]
    assert compliance_by_priority(tickets, NOW) == {"P1": 0.5, "P2": 1.0, "P3": 0.5, "P4": 0.0}
