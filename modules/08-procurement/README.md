# Module 08: Procurement — Vendor Quote Scoring

## The business problem

Procurement collects quotes from several vendors for each item. The cheapest is not always the best: a slow or low-quality vendor can cost more in the end. We want a **fair, repeatable score** that balances price, delivery time and quality, so every decision is explainable to auditors.

## The concepts: normalization and weighted scoring

1. **Normalize** each criterion to a 0-1 scale *among the quotes for the same item*:
   `(value - lowest) / (highest - lowest)`. For price and lead time, lower is better, so the scale is flipped.
2. **Weight** the criteria by company priority (default: price 50%, lead time 30%, quality 20%) and add them up.

Example (Office Chair): Vendor B is the cheapest (price score 1.0), the slowest (lead score 0.0) and middle on quality (0.5):
`0.5 x 1.0 + 0.3 x 0.0 + 0.2 x 0.5 = 0.60`

## Step 1: The prompt

```
ROLE: You are a Python developer helping a procurement team. Explain your code simply.

CONTEXT: I have data/quotes.csv with columns:
item, vendor, unit_price, lead_time_days, quality_rating (1-5)

TASK: For each item, score every vendor quote and recommend the best one.

CONSTRAINTS:
- Standard library only.
- Use min-max normalization per item. Lower price and lead time are better; higher quality is better.
- If all quotes are equal on a criterion, give each a score of 1 (no divide-by-zero).
- Weights: price 0.5, lead time 0.3, quality 0.2. Raise an error if they do not add up to 1.
- Add pytest tests.

OUTPUT: For each item, vendors ranked by score with the winner marked.
```

## Step 2: Run it

```bash
python modules/08-procurement/vendor_selection.py
```

```bash
pytest modules/08-procurement
```

## Step 3: How it works

- `group_by_item` puts quotes in buckets per item, because vendors are only compared with others quoting the **same** item.
- `normalize` is a small reusable function. The `higher_is_better` flag handles "cheaper is better" and "higher rating is better" with the same code.
- `score_quotes` checks the weights first. Weights that add up to 1.2 would quietly distort every score.

## Verify by hand

Laptop: both vendors have a 10-day lead time, so both get 1.0 for lead time. Vendor D is cheaper (price 1.0) but lower quality (0.0): `0.5 + 0.3 + 0 = 0.80`. Vendor A: `0 + 0.3 + 0.2 = 0.50`. **D wins.** ✔

## Common mistakes

- **Comparing across items.** A laptop and a chair should never be on the same price scale.
- **Hidden weights.** Write the weights down and get them agreed. They are a business decision, not a technical one.
- **Small differences on a 0-1 scale look big.** With two vendors, one always scores 0 and the other 1, even if prices differ by only 1%. Show the raw numbers next to the score (the report does).

## Exercises

1. Ask Claude: *"Let me pass the weights on the command line, e.g. --weights 0.6,0.2,0.2."*
2. Ask Claude: *"Exclude vendors whose lead time is above a maximum I set per item."*
3. Challenge: *"Add total cost = unit price x quantity + shipping, and score on total cost."*
