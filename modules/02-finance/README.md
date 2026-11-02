# Module 02: Finance — Budget vs. Actual Variance Report

## The business problem

Every month, finance compares each department's spending with its budget, line by line, in a spreadsheet. It is slow, and it is easy to miss the lines that matter. We want a report that **flags lines that are off budget by more than 10%** and shows totals per department.

## The concept: variance

```
variance   = actual - budget          (positive = overspent)
variance % = variance / budget x 100
```

Spending 58,000 against a 50,000 budget is a variance of +8,000, or **+16%**. That is beyond the 10% threshold, so the line is flagged **OVER**.

## Step 1: The prompt

```
ROLE: You are a Python developer helping a finance team. Explain your code simply.

CONTEXT: I have data/budget_vs_actual.csv with columns:
department, category, budget, actual

TASK: Build a variance report.

CONSTRAINTS:
- Standard library only. Use Decimal (not float) for money.
- variance = actual - budget; variance % = variance / budget * 100.
- Status: OVER if variance % > threshold, UNDER if < -threshold, otherwise OK.
  Default threshold is 10%, configurable with --threshold.
- If budget is 0 and there is spending, status is UNBUDGETED (do not divide by zero).
- Add totals per department and pytest tests.

OUTPUT: A printed table, then totals by department.
```

## Step 2: Run it

```bash
python modules/02-finance/budget_variance.py
```

Try a stricter threshold:

```bash
python modules/02-finance/budget_variance.py --threshold 5
```

```bash
pytest modules/02-finance
```

## Step 3: How it works

- **`Decimal` instead of `float`.** Computers store `float` numbers in binary, so `0.1 + 0.2` gives `0.30000000000000004`. For money, always use `Decimal`. A test proves it.
- `variance_pct` returns `None` when the budget is zero, so the report shows `n/a` instead of crashing.
- `department_totals` uses a `defaultdict`, a dictionary that starts every new key at zero, so you can add to it without checking first.

## Verify by hand

HR Training: 18,000 - 15,000 = 3,000. 3,000 / 15,000 = 20%. That is more than 10%, so **OVER**. ✔

## Common mistakes

- **Using float for money.** Small rounding errors add up across thousands of lines.
- **Sign confusion.** Decide once whether positive means "overspent" or "favourable", and write it down. For revenue lines, the meaning flips.
- **Dividing by a zero budget.** Unbudgeted spending is often the most important thing to catch.

## Exercises

1. Ask Claude: *"Add a `type` column (expense or revenue) and flip the OVER/UNDER logic for revenue."*
2. Ask Claude: *"Export only the flagged lines to flagged.csv."*
3. Challenge: *"Read two months of data and show the month-over-month trend."*
