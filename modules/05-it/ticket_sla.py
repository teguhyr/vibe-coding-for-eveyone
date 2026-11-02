"""IT: helpdesk ticket SLA monitor.

Each priority has a target resolution time (the SLA). A ticket breaches its SLA
when it took longer than the target, or is still open past the target.
Times are calendar hours (24/7 support).
"""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

DEFAULT_DATA = Path(__file__).parent / "data" / "tickets.csv"
SLA_HOURS = {"P1": 4, "P2": 8, "P3": 24, "P4": 72}


@dataclass(frozen=True)
class Ticket:
    ticket_id: str
    priority: str
    category: str
    opened_at: datetime
    resolved_at: datetime | None

    @property
    def is_open(self) -> bool:
        return self.resolved_at is None


def hours_elapsed(ticket: Ticket, now: datetime) -> float:
    end = ticket.resolved_at or now
    return (end - ticket.opened_at).total_seconds() / 3600


def is_breached(ticket: Ticket, now: datetime) -> bool:
    return hours_elapsed(ticket, now) > SLA_HOURS[ticket.priority]


def compliance_by_priority(tickets: list[Ticket], now: datetime) -> dict[str, float]:
    """Share of tickets per priority that are within SLA (0.0 to 1.0)."""
    totals: dict[str, int] = defaultdict(int)
    within: dict[str, int] = defaultdict(int)
    for t in tickets:
        totals[t.priority] += 1
        if not is_breached(t, now):
            within[t.priority] += 1
    return {p: within[p] / totals[p] for p in sorted(totals)}


def load_tickets(path: Path) -> list[Ticket]:
    tickets = []
    with path.open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["priority"] not in SLA_HOURS:
                raise ValueError(f"{r['ticket_id']}: unknown priority {r['priority']!r}")
            resolved = r["resolved_at"].strip()
            tickets.append(
                Ticket(
                    r["ticket_id"],
                    r["priority"],
                    r["category"],
                    datetime.fromisoformat(r["opened_at"]),
                    datetime.fromisoformat(resolved) if resolved else None,
                )
            )
    return tickets


def main() -> None:
    parser = argparse.ArgumentParser(description="Helpdesk ticket SLA monitor.")
    parser.add_argument("csv_file", nargs="?", type=Path, default=DEFAULT_DATA)
    parser.add_argument(
        "--now",
        type=datetime.fromisoformat,
        default=datetime.now(),
        help="Pretend the current time is this (e.g. 2026-11-02T12:00). Default: now.",
    )
    args = parser.parse_args()
    tickets = load_tickets(args.csv_file)

    print(f"SLA breaches as of {args.now:%Y-%m-%d %H:%M}")
    print(f"{'Ticket':<9} {'Pri':<4} {'Category':<18} {'Hours':>6} {'SLA':>4}  State")
    for t in tickets:
        if is_breached(t, args.now):
            state = "OPEN" if t.is_open else "resolved late"
            print(
                f"{t.ticket_id:<9} {t.priority:<4} {t.category:<18} "
                f"{hours_elapsed(t, args.now):>6.1f} {SLA_HOURS[t.priority]:>4}  {state}"
            )

    print("\nSLA compliance by priority")
    for priority, share in compliance_by_priority(tickets, args.now).items():
        print(f"{priority}: {share:.0%}")


if __name__ == "__main__":
    main()
