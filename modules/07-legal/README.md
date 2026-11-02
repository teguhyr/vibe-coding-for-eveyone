# Module 07: Legal — Contract Renewal & Notice Deadline Tracker

> **Disclaimer:** this tool tracks dates. It is not legal advice. Always check the actual contract wording. Contracts are often confidential, so give the AI tool only made-up examples, never real contract text.

## The business problem

Many contracts **renew automatically** unless you give written notice by a deadline, for example "90 days before the end date". When that deadline is missed, the company is locked into another year of a service it may not want. Legal teams usually track this in a spreadsheet and calendar reminders. We want a list of **contracts that need action soon**.

## The concept: notice deadline

```
notice deadline = end date - notice period (days)
```

A contract ending on 15 Jan 2027 with 30 days' notice must be cancelled by **16 Dec 2026**.

| Status | Meaning |
|--------|---------|
| `EXPIRED` | The end date has passed |
| `NOTICE PERIOD PASSED` | Too late to give notice; it renews if auto-renew is on |
| `ACT NOW` | The notice deadline is within the next 60 days (configurable) |
| `OK` | No action needed yet |

## Step 1: The prompt

```
ROLE: You are a Python developer helping a legal team. Explain your code simply.

CONTEXT: I have data/contracts.csv (synthetic data) with columns:
contract_id, counterparty, contract_type, end_date, notice_days, auto_renew (yes/no)

TASK: List contracts that need attention, sorted by notice deadline.

CONSTRAINTS:
- Standard library only.
- notice deadline = end_date - notice_days.
- Statuses: EXPIRED, NOTICE PERIOD PASSED, ACT NOW (deadline within 60 days), OK.
- Allow --today and --window options so results can be tested for any date.
- Reject auto_renew values other than yes/no with a clear error.
- Add pytest tests, including the exact boundary days.

OUTPUT: A printed table of contracts that are not OK.
```

## Step 2: Run it

```bash
python modules/07-legal/contract_renewals.py --today 2026-11-02
```

```bash
python modules/07-legal/contract_renewals.py --today 2026-11-02 --window 90
```

```bash
pytest modules/07-legal
```

## Step 3: How it works

- `notice_deadline` is a property calculated with `timedelta`, Python's way to add or subtract days.
- `contract_status` checks the most serious situation first (expired), then works down. **The order of the `if` checks matters.**
- The `--today` option lets you "time travel". Tests always use a fixed date, so they give the same result every day.

## Verify by hand

CTR-005 ends 31 Dec 2026 with 14 days' notice, so the deadline is 17 Dec 2026. That is 45 days after 2 Nov, which is inside the 60-day window: **ACT NOW**. ✔

## Common mistakes

- **Using `date.today()` inside tests.** The test passes today and fails next month. Always pass the date in.
- **Off-by-one at the boundaries.** Is a deadline *today* still actionable? (Yes.) Tests check both edges.
- **Business days vs. calendar days.** Some contracts say "business days". Check the wording.

## Exercises

1. Ask Claude: *"Add an owner column and group the report by owner."*
2. Ask Claude: *"Generate an .ics calendar file with a reminder 14 days before each notice deadline."*
3. Challenge: *"Store contracts in SQLite and add a command to mark a contract as 'notice sent'."*
