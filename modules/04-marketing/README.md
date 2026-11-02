# Module 04: Marketing — Campaign Performance Report

## The business problem

Campaign results come from several platforms (Instagram, Google Ads, Email, TikTok) as different exports. The team wants one view: **which campaigns earn the most per unit spent, and which need review?**

## The concepts: four key metrics

| Metric | Formula | Question it answers |
|--------|---------|---------------------|
| **CTR** (click-through rate) | clicks / impressions | Do people notice and click? |
| **CPC** (cost per click) | spend / clicks | What does one visit cost? |
| **CPA** (cost per acquisition) | spend / conversions | What does one sale or sign-up cost? |
| **ROAS** (return on ad spend) | revenue / spend | How much revenue per 1 unit spent? |

A ROAS of 4.8 means every 1 rupiah (or dollar) spent brought back 4.8 in revenue.

## Step 1: The prompt

```
ROLE: You are a Python developer helping a marketing team. Explain your code simply.

CONTEXT: I have data/campaigns.csv with columns:
campaign, channel, spend, impressions, clicks, conversions, revenue

TASK: Calculate CTR, CPC, CPA and ROAS for each campaign and rank by ROAS.

CONSTRAINTS:
- Standard library only.
- If a denominator is zero, show "n/a" instead of crashing.
- Flag campaigns below a target ROAS (default 2.0, configurable with --target-roas).
- Campaigns with unknown ROAS go last in the ranking.
- Add pytest tests.

OUTPUT: A printed table sorted by ROAS, best first.
```

## Step 2: Run it

```bash
python modules/04-marketing/campaign_metrics.py
```

```bash
python modules/04-marketing/campaign_metrics.py --target-roas 3
```

```bash
pytest modules/04-marketing
```

## Step 3: How it works

- `safe_divide` returns `None` when dividing by zero. Every metric uses it, so the zero-handling lives in **one place**.
- Each metric is a `@property`, so it is always calculated from the latest numbers.
- `rank_by_roas` sorts by a **tuple** key: first "is ROAS missing?" (False sorts before True), then ROAS from highest to lowest.

## Verify by hand

Ramadan Promo: 24,000 revenue / 5,000 spend = **4.8 ROAS**. 5,000 clicks / 250,000 impressions = **2.0% CTR**. ✔

## Common mistakes

- **Judging every campaign by ROAS.** The City Billboard is an awareness campaign with no tracked sales, so a ROAS of 0 does not mean it failed. Ask Claude to add a `goal` column (awareness or sales) and only flag sales campaigns.
- **Mixing currencies or date ranges** from different platforms in one table.
- **Using averages of percentages.** To get total CTR, divide total clicks by total impressions. Do not average the CTR column.

## Exercises

1. Ask Claude: *"Add a summary per channel, calculated from totals, not averages."*
2. Ask Claude: *"Add a `goal` column and only flag low ROAS for sales campaigns."*
3. Challenge: *"Create a bar chart of ROAS per campaign with matplotlib and save it as a PNG."*
