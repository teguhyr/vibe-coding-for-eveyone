from datetime import datetime

import pytest
from room_booking import DEFAULT_DATA, Booking, find_conflicts, load_bookings, overlaps


def booking(bid: str, start: str, end: str, room: str = "R1") -> Booking:
    day = "2026-11-03T"
    return Booking(
        bid, room, "Team", datetime.fromisoformat(day + start), datetime.fromisoformat(day + end)
    )


def test_overlapping_times_conflict():
    assert overlaps(booking("A", "09:00", "10:00"), booking("B", "09:30", "11:00"))


def test_back_to_back_bookings_do_not_conflict():
    assert not overlaps(booking("A", "09:00", "10:00"), booking("B", "10:00", "11:00"))


def test_booking_inside_another_conflicts():
    assert overlaps(booking("A", "09:00", "12:00"), booking("B", "10:00", "10:30"))


def test_different_rooms_never_conflict():
    assert not overlaps(booking("A", "09:00", "10:00", "R1"), booking("B", "09:00", "10:00", "R2"))


def test_end_before_start_is_rejected():
    with pytest.raises(ValueError):
        booking("A", "10:00", "09:00")


def test_long_booking_conflicts_with_all_later_overlaps():
    long = booking("LONG", "09:00", "17:00")
    pairs = find_conflicts([long, booking("X", "10:00", "11:00"), booking("Y", "15:00", "16:00")])
    assert [(a.booking_id, b.booking_id) for a, b in pairs] == [("LONG", "X"), ("LONG", "Y")]


def test_sample_data():
    pairs = {(a.booking_id, b.booking_id) for a, b in find_conflicts(load_bookings(DEFAULT_DATA))}
    assert pairs == {("B-01", "B-02"), ("B-04", "B-05"), ("B-04", "B-06"), ("B-05", "B-06")}
