# Module 03: Human Resources — Leave Balance Tracker

> **Privacy first.** HR data is personal data. The names and IDs in `data/` are **made up**. Never paste real employee records, ID numbers (KTP/NIK), salaries or health information into an AI tool. Protecting this data is a legal duty under Indonesia's UU PDP (UU No. 27/2022) and the GDPR. Build and test with synthetic data, then run the finished script on real data **on your own computer**.

## The business problem

Employees ask HR "how many leave days do I have left?" and HR checks a spreadsheet by hand. Weekends and public holidays are often counted wrongly. We want a tracker that counts **working days only** and shows used, remaining, and pending leave for each employee.

## The concepts

- **Working days:** Monday to Friday, minus public holidays. Leave from Friday to Tuesday covers 5 calendar days but only **3 working days**.
- **Joining data:** employees and leave requests are in two separate files, linked by `employee_id`, just like a VLOOKUP in Excel.

## Step 1: The prompt

```
ROLE: You are a Python developer helping an HR team. Explain your code simply.

CONTEXT: I have three CSV files (synthetic data):
- employees.csv: employee_id, name, department, annual_entitlement
- leave_requests.csv: employee_id, start_date, end_date, status (approved/pending/rejected)
- holidays.csv: date, name

TASK: Calculate each employee's leave used, remaining, and pending.

CONSTRAINTS:
- Standard library only.
- Count only Monday-Friday, skip public holidays, include start and end dates.
- Only approved leave reduces the balance; show pending separately; ignore rejected.
- Raise a clear error for an unknown employee_id, an unknown status, or end before start.
- Flag employees who have used more than their entitlement.
- Add pytest tests.

OUTPUT: One row per employee in a printed table.
```

## Step 2: Run it

```bash
python modules/03-hr/leave_tracker.py
```

```bash
pytest modules/03-hr
```

## Step 3: How it works

- `working_days` walks day by day from start to end. `date.weekday()` returns 0 for Monday up to 6 for Sunday, so `< 5` means a weekday.
- Holidays are stored in a `set`, which makes "is this date a holiday?" an instant lookup.
- `calculate_balances` adds up days per employee in two dictionaries: `used` and `pending`.
- Bad data **raises an error** with a clear message instead of silently producing a wrong balance.

## Verify by hand

Budi (E001): 2-6 March is 5 days. 17-21 August is 5 days minus Independence Day = 4. Total 9 used, 12 - 9 = **3 left**. ✔

## Common mistakes

- **Counting calendar days** instead of working days.
- **Forgetting that end dates are inclusive.** Leave from Monday to Monday is 1 day, not 0.
- **Silently ignoring bad rows.** A typo like `aproved` should stop the report, not vanish.
- **Sharing real employee data with AI tools.** See the privacy note above.

## Exercises

1. Ask Claude: *"Support half-day leave with a `half_day` column (yes/no)."*
2. Ask Claude: *"Carry over up to 5 unused days from last year."*
3. Challenge: *"Show a monthly headcount-on-leave summary so managers can spot busy periods."*
