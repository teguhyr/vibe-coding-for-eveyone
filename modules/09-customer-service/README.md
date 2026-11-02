# Module 09: Customer Service — Ticket Triage by Keyword

## The business problem

Messages arrive by email, chat and WhatsApp. An agent reads each one just to decide who should handle it. We want to **sort messages into categories automatically** and **put urgent ones first**, so agents spend their time solving problems instead of sorting them.

## The concept: rule-based classification

Each category has a list of keywords. A message goes to the category with the **most keyword hits**. No hits means `other`. This is simple, fast, and fully explainable: you can always say *why* a message was put in a category.

Start with rules. Once you have a few hundred correctly labelled messages, you can compare the rules with an AI model (see the exercises).

## Step 1: The prompt

```
ROLE: You are a Python developer helping a customer service team. Explain your code simply.

CONTEXT: I have data/messages.csv with columns: ticket_id, channel, message

TASK: Give each message a category (billing, delivery, technical, account, or other)
and an urgency flag.

CONSTRAINTS:
- Standard library only.
- Keep the keyword lists in one dictionary at the top so the team can edit them.
- Match whole words only, ignore upper/lower case, support phrases like "not working".
- The category with the most hits wins; on a tie, the first listed wins; no hits = "other".
- Urgent if the message contains: urgent, asap, immediately, emergency.
- Add pytest tests.

OUTPUT: Urgent messages first, then a count per category.
```

## Step 2: Run it

```bash
python modules/09-customer-service/ticket_triage.py
```

```bash
pytest modules/09-customer-service
```

## Step 3: How it works

- `CATEGORY_KEYWORDS` is the **business rulebook**. Non-programmers can edit it without touching the logic.
- `re.search(rf"\b{kw}\b", ...)` uses a **regular expression** with word boundaries (`\b`), so `late` matches "was late" but not "translate".
- `max(hits, key=...)` picks the category with the most hits. Python's `max` keeps the first one on a tie, so the dictionary order decides ties.
- `Counter(...).most_common()` counts categories in one line.

## Verify by hand

T-004: "I forgot my **password** and cannot **log in** to my **account**" has 3 account hits and nothing else, so it goes to **account**. ✔

## Common mistakes

- **Substring matching.** Without word boundaries, "bill" matches "Bill Gates" and "late" matches "chocolate".
- **Ignoring ties.** T-007 ("payment page is not working") hits billing *and* technical. Decide which team should get it, and write that down.
- **Never reviewing the rules.** Check a sample of the `other` category every week and add keywords.
- **Language mix.** Customers may write in Bahasa Indonesia. Add keywords such as `tagihan`, `pengiriman`, `kata sandi`.

## Exercises

1. Ask Claude: *"Add Indonesian keywords for every category and tests for them."*
2. Ask Claude: *"Write the results to triaged.csv with a suggested team per category."*
3. Challenge: *"Use the Claude API to classify the messages that the rules put in 'other', and compare the results."*
