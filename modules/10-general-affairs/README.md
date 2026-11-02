# Module 10: General Affairs — Meeting Room Double-Booking Checker

## The business problem

Meeting rooms are booked through a shared spreadsheet or form. Two teams often turn up for the same room at the same time. General Affairs wants to **catch double bookings in advance** and contact the teams before the meeting.

## The concept: overlapping time ranges

Two bookings of the same room overlap when:

```
A starts before B ends   AND   B starts before A ends
```

This one rule covers every case: partial overlap, one booking inside another, and identical times. Bookings that are **back to back** (A ends 11:00, B starts 11:00) do *not* overlap.

## Step 1: The prompt

```
ROLE: You are a Python developer helping a General Affairs team. Explain your code simply.

CONTEXT: I have data/bookings.csv with columns: booking_id, room, booked_by, start, end
(start and end look like 2026-11-03T09:00).

TASK: Find every pair of bookings that overlap in the same room.

CONSTRAINTS:
- Standard library only.
- Overlap rule: a.start < b.end and b.start < a.end. Back-to-back is not a conflict.
- Reject bookings whose end is not after the start.
- Group by room and sort by start time so the check is efficient.
- Add pytest tests for partial overlap, nested bookings, back-to-back, and different rooms.

OUTPUT: The number of conflicts, then one line per conflicting pair.
```

## Step 2: Run it

```bash
python modules/10-general-affairs/room_booking.py
```

```bash
pytest modules/10-general-affairs
```

## Step 3: How it works

- `Booking.__post_init__` **validates** each booking as it is created, so bad data never gets into the check.
- Bookings are grouped by room, then **sorted by start time**. For each booking, we only check the ones that start before it ends. As soon as one starts later, we `break`, because all the following ones start even later. This keeps the check fast even with thousands of bookings.

## Verify by hand

Room Bromo: Marketing 13:00-15:00, Legal 14:00-14:30, Operations 14:15-16:00. All three overlap each other, which gives **3 conflicts**. ✔ IT Team in Room Merapi (11:00-12:00) starts exactly when HR ends, so there is no conflict. ✔

## Common mistakes

- **Using `<=` in the overlap rule.** That would wrongly flag back-to-back meetings.
- **Only comparing neighbours.** A long booking can overlap several later ones. The test `test_long_booking_conflicts_with_all_later_overlaps` checks this.
- **Ignoring time zones** when offices in different cities share one booking system.

## Exercises

1. Ask Claude: *"Add room capacity and flag bookings with more attendees than seats."*
2. Ask Claude: *"Suggest a free room of similar size for each conflict."*
3. Challenge: *"Build a small web form with Flask (or PHP) that checks for conflicts before saving a booking to SQLite."*

## More support functions to try

Use the same pattern (R-C-T-C-O prompt, synthetic data, tests) for other support work:

| Function | Idea |
|----------|------|
| Facilities | Asset maintenance schedule: flag equipment overdue for service |
| Fleet | Vehicle fuel efficiency: litres per 100 km per vehicle, flag outliers |
| Health & Safety (HSE) | Incident log: count incidents per site per month |
| Internal Audit | Expense claims: flag duplicates and claims just under the approval limit |
| Corporate Communication | Press mentions: count mentions per topic per week |
