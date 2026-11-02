# Module 05: IT — Helpdesk Ticket SLA Monitor

## The business problem

The IT helpdesk promises resolution times by priority, called the **SLA** (Service Level Agreement). Managers only find out about breaches at the end of the month, when it is too late to act. We want a report of **which tickets broke the SLA, including open tickets that are already late**, plus the compliance rate per priority.

## The concept: SLA targets

| Priority | Example | Resolve within |
|----------|---------|----------------|
| P1 | Email or VPN down for everyone | 4 hours |
| P2 | A department cannot work normally | 8 hours |
| P3 | One user has a problem | 24 hours |
| P4 | Requests (new software, access) | 72 hours |

A ticket **breaches** if it took longer than its target, *or* it is still open and the target time has already passed.

```
elapsed hours = (resolved time, or now if still open) - opened time
```

## Step 1: The prompt

```
ROLE: You are a Python developer helping an IT helpdesk team. Explain your code simply.

CONTEXT: I have data/tickets.csv with columns:
ticket_id, priority (P1-P4), category, opened_at, resolved_at (empty if still open).
Times look like 2026-10-28T08:00.

TASK: List tickets that breached their SLA and show the compliance % per priority.

CONSTRAINTS:
- Standard library only.
- SLA hours: P1=4, P2=8, P3=24, P4=72. Calendar hours (24/7).
- Open tickets are measured up to "now". Add a --now option so I can test any time.
- Finishing exactly at the SLA limit is NOT a breach.
- Reject unknown priorities with a clear error.
- Add pytest tests.

OUTPUT: A table of breached tickets (open or resolved late), then compliance % by priority.
```

## Step 2: Run it

```bash
python modules/05-it/ticket_sla.py --now 2026-11-02T12:00
```

Expected output:

```
SLA breaches as of 2026-11-02 12:00
Ticket    Pri  Category            Hours  SLA  State
INC-1002  P1   VPN down              6.0    4  resolved late
INC-1004  P3   New laptop setup     48.0   24  resolved late
INC-1006  P4   Software request     75.0   72  OPEN

SLA compliance by priority
P1: 50%
P2: 100%
P3: 50%
P4: 0%
```

```bash
pytest modules/05-it
```

## Step 3: How it works

- `datetime.fromisoformat` turns text like `2026-10-28T08:00` into a real date and time that Python can subtract.
- Subtracting two datetimes gives a `timedelta`. `.total_seconds() / 3600` turns it into hours.
- `ticket.resolved_at or now` means "use the resolved time if there is one, otherwise use now". This one line handles open tickets.
- `--now` lets you freeze time. Without it, the report would change every minute and the tests could not check exact results.

## Verify by hand

INC-1006 (P4) opened 30 Oct at 09:00 and is still open. By 2 Nov 12:00 that is 3 days and 3 hours = **75 hours**, which is more than 72, so it is a breach. ✔

> **Lesson from building this module:** the first version of the sample data had INC-1006 opened at 13:00, which is only 71 hours, so it was *not* a breach. The `test_sample_data` test caught the mistake. Tests check *your* assumptions too, not just the code.

## Common mistakes

- **Forgetting open tickets.** The most important breaches are the ones still happening.
- **Using `>=` instead of `>`.** Resolving exactly on time meets the SLA.
- **Calendar hours vs. business hours.** Many SLAs only count office hours. This module uses 24/7 to keep it simple. See the exercises.

## Exercises

1. Ask Claude: *"Also show open tickets that will breach within the next 2 hours, as an early warning."*
2. Ask Claude: *"Calculate the average resolution time per category."*
3. Challenge: *"Count only business hours (Mon-Fri, 08:00-17:00) when measuring the SLA."*
