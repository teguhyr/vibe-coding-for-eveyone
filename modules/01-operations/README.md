# Module 01: Operations — Inventory Reorder Alerts

## The business problem

The warehouse team checks stock levels by hand in a spreadsheet. Sometimes items run out because nobody noticed in time, and sometimes too much is ordered "just in case". We want a daily list of **what to reorder now**, most urgent first.

## The concept: reorder point

```
reorder point = (average daily usage x supplier lead time in days) + safety stock
```

If you use 2 boxes a day and the supplier needs 6 days to deliver, you need 12 boxes to last until the delivery arrives. The safety stock (say 4) covers surprises. So you reorder when stock reaches **16**.

## Step 1: The prompt

```
ROLE: You are a Python developer helping an operations team. Explain your code simply.

CONTEXT: I have data/inventory.csv with columns:
sku, name, on_hand, avg_daily_usage, lead_time_days, safety_stock

TASK: Build a script that lists items that need reordering.

CONSTRAINTS:
- Standard library only.
- Reorder point = avg_daily_usage * lead_time_days + safety_stock.
- An item is due when on_hand <= reorder point.
- Sort by "days of cover" (on_hand / avg_daily_usage), fewest first.
- Do not crash if avg_daily_usage is 0.
- Add pytest tests.

OUTPUT: A printed table with SKU, item, on hand, reorder point, days left.
```

## Step 2: Run it

```bash
python modules/01-operations/inventory_reorder.py
```

Expected output:

```
SKU      Item                  On hand Reorder pt Days left
SKU-006  Pallet Wrap                 3         16       1.5
SKU-004  Cardboard Box M            55         68       4.6
SKU-002  Printer Toner               8         16       5.3
```

Run the tests:

```bash
pytest modules/01-operations
```

## Step 3: How it works

- `Item` is a **dataclass**: a simple container for one row of data with named fields.
- `reorder_point` and `days_of_cover` are **properties**: values calculated from the other fields, so they can never be out of date.
- `items_to_reorder` filters with a **list comprehension** and sorts with `key=`, which tells Python *what* to sort by.

## Verify by hand

Pallet Wrap: 2 a day x 6 days + 4 safety = 16. We have 3, so it is due, and 3 / 2 = 1.5 days left. ✔

## Common mistakes

- **Using `<` instead of `<=`.** An item exactly at the reorder point should be ordered. The tests check this.
- **Dividing by zero** for items nobody uses. Always ask Claude to handle zeros.
- **Trusting the averages.** If usage is seasonal, a 12-month average will be wrong in peak season.

## Exercises

1. Ask Claude: *"Add a column with the suggested order quantity so stock goes back to 30 days of cover."*
2. Ask Claude: *"Save the result as reorder_list.csv so purchasing can open it in Excel."*
3. Challenge: load the CSV into **SQLite** and write the same logic as a SQL query.
