# Module 06: Accounting — Bank Reconciliation

## The business problem

At month end, accountants tick off every bank statement line against the general ledger (the books) by hand. With hundreds of lines, this takes hours. We want the computer to **match the obvious lines automatically** so people only review the exceptions.

## The concept: reconciliation

A bank line and a ledger entry **match** when:

1. the amount is exactly the same, and
2. the dates are within a few days of each other (default 3), because payments take time to clear.

What is left unmatched is the useful part:

| Unmatched in... | Typical cause | Action |
|-----------------|---------------|--------|
| **Bank only** | Bank fees, interest, direct debits | Record them in the books |
| **Ledger only** | Uncleared cheques, deposits in transit, errors | Check timing, or investigate |

## Step 1: The prompt

```
ROLE: You are a Python developer helping an accounting team. Explain your code simply.

CONTEXT: I have two CSV files:
- bank_statement.csv: date, description, amount
- ledger.csv: date, reference, amount
Positive amounts are money in, negative amounts are money out.

TASK: Reconcile the bank statement against the ledger.

CONSTRAINTS:
- Standard library only. Use Decimal for amounts.
- Match on exact amount and a date difference of at most 3 days (configurable).
- Each ledger entry can be matched only once. If several qualify, use the closest date.
- Add pytest tests, including duplicate amounts.

OUTPUT: Number matched, then two lists with totals: "bank only" and "ledger only".
```

## Step 2: Run it

```bash
python modules/06-accounting/bank_reconciliation.py
```

```bash
pytest modules/06-accounting
```

## Step 3: How it works

- `reconcile` loops through bank lines in date order. For each one it collects **candidates**: ledger entries with the same amount and a close date.
- The chosen entry is **removed** from `unmatched_ledger`, so it cannot be matched twice. A test checks this, because duplicate amounts (such as two identical supplier payments) are common.
- Whatever remains in `unmatched_ledger` at the end is "ledger only".

## Verify by hand

Rent: the bank shows -8,000.00 on 3 Oct and the ledger shows -8,000.00 on 2 Oct. Same amount, 1 day apart, so it matches. ✔ The bank admin fee (-25.00) has no ledger entry, so it shows as "record in the books". ✔

## Common mistakes

- **Matching on amount only.** Two payments of 1,000 in different months would be wrongly paired.
- **Matching a ledger entry twice.** This hides a missing transaction.
- **Using float.** `Decimal("4250.50")` is exact. A float might not be.
- **Fully trusting automation.** This is a first pass. An accountant still reviews and signs off.

## Exercises

1. Ask Claude: *"Also show possible matches: same amount but 4-10 days apart."*
2. Ask Claude: *"Produce a reconciliation statement: bank balance + deposits in transit - outstanding cheques = book balance."*
3. Challenge: *"Load both files into SQLite and do the matching with a SQL JOIN."*
