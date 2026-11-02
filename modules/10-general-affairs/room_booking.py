"""General Affairs: find double-booked meeting rooms.

Two bookings of the same room conflict when their times overlap:
    a.start < b.end  and  b.start < a.end
Back-to-back bookings (one ends at 11:00, the next starts at 11:00) are fine.
"""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

DEFAULT_DATA = Path(__file__).parent / "data" / "bookings.csv"


@dataclass(frozen=True)
class Booking:
    booking_id: str
    room: str
    booked_by: str
    start: datetime
    end: datetime

    def __post_init__(self) -> None:
        if self.end <= self.start:
            raise ValueError(f"{self.booking_id}: end time must be after start time")


def overlaps(a: Booking, b: Booking) -> bool:
    return a.room == b.room and a.start < b.end and b.start < a.end


def find_conflicts(bookings: list[Booking]) -> list[tuple[Booking, Booking]]:
    by_room: dict[str, list[Booking]] = defaultdict(list)
    for booking in bookings:
        by_room[booking.room].append(booking)

    conflicts = []
    for room_bookings in by_room.values():
        room_bookings.sort(key=lambda b: b.start)
        for i, first in enumerate(room_bookings):
            for second in room_bookings[i + 1 :]:
                # Sorted by start: once one starts after `first` ends, later ones do too.
                if second.start >= first.end:
                    break
                conflicts.append((first, second))
    return conflicts


def load_bookings(path: Path) -> list[Booking]:
    with path.open(newline="", encoding="utf-8") as f:
        return [
            Booking(
                r["booking_id"],
                r["room"],
                r["booked_by"],
                datetime.fromisoformat(r["start"]),
                datetime.fromisoformat(r["end"]),
            )
            for r in csv.DictReader(f)
        ]


def main() -> None:
    parser = argparse.ArgumentParser(description="Find double-booked meeting rooms.")
    parser.add_argument("csv_file", nargs="?", type=Path, default=DEFAULT_DATA)
    args = parser.parse_args()

    conflicts = find_conflicts(load_bookings(args.csv_file))
    if not conflicts:
        print("No double bookings found.")
        return
    print(f"{len(conflicts)} conflict(s) found")
    for a, b in conflicts:
        print(
            f"  {a.room}: {a.booking_id} {a.booked_by} ({a.start:%d %b %H:%M}-{a.end:%H:%M}) "
            f"overlaps {b.booking_id} {b.booked_by} ({b.start:%H:%M}-{b.end:%H:%M})"
        )


if __name__ == "__main__":
    main()
