# Module 00: Getting Started with Vibe Coding

**Goal:** Set up your tools and learn the basic loop you will repeat in every other module.

## What is vibe coding?

Vibe coding means building software by **describing what you want in plain language** to an AI assistant such as Claude Code. The AI writes the code. You stay in charge: you decide what to build, check that it works, and ask for changes.

You do not need to be a programmer to start. You do need to:

1. Know your business problem well (you already do; that is your job).
2. Describe it clearly.
3. **Check the result** instead of trusting it blindly.

## 1. Set up your tools

| Tool | Why you need it | Get it |
|------|-----------------|--------|
| **Python 3.10+** | Runs the example apps | https://www.python.org/downloads/ |
| **VS Code** | Editor to view and run code | https://code.visualstudio.com/ |
| **Claude Code** | The AI assistant (CLI or VS Code extension) | https://code.claude.com/docs |
| **Git** | Saves versions of your work | https://git-scm.com/ |

Then, from the repository root:

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

On Windows, use `.venv\Scripts\activate` instead.

```bash
pip install -r requirements-dev.txt
```

Check everything works:

```bash
pytest
```

## 2. The vibe coding loop

```
  Describe  ->  Generate  ->  Run  ->  Verify  ->  Refine
     ^                                               |
     +-----------------------------------------------+
```

1. **Describe** the problem, the input data, and the output you want.
2. **Generate**: let Claude write the code.
3. **Run** it on sample data.
4. **Verify**: check a few results by hand. Does the number match what you would calculate in Excel?
5. **Refine**: ask for changes ("also sort by department", "export to CSV").

## 3. The prompt formula: R-C-T-C-O

Good prompts have five parts. Copy [`prompt-template.md`](prompt-template.md) and fill it in.

| Part | Question it answers | Example (Finance) |
|------|---------------------|-------------------|
| **R**ole | Who should the AI act as? | "You are a Python developer helping a finance team." |
| **C**ontext | What is the situation and data? | "I have a CSV with department, category, budget, actual." |
| **T**ask | What exactly should it build? | "Calculate variance and variance % for each line." |
| **C**onstraints | Rules and limits? | "Standard library only. Use Decimal for money. Flag lines over 10%." |
| **O**utput | What should the result look like? | "Print a table, then totals per department." |

## 4. Golden rules for business users

1. **Never paste real personal or confidential data** into an AI tool. Use made-up sample data like the files in each module's `data/` folder. Personal data such as employee records, ID numbers (KTP/NIK) and salaries is protected by laws like Indonesia's UU PDP (UU No. 27/2022) and the GDPR.
2. **Verify the numbers.** Check at least 2 or 3 results by hand before you trust a report.
3. **Start small.** Get one simple version working, then add features one at a time.
4. **Ask "why".** If you do not understand a line of code, ask Claude to explain it simply.
5. **Save your work** with Git after each working step.

## 5. How every module is organized

| File | What it is |
|------|------------|
| `README.md` | The business problem, the prompt to use, how it works, mistakes to avoid, exercises |
| `data/*.csv` | Synthetic (made-up) sample data |
| `<name>.py` | A working example of what Claude might generate |
| `test_<name>.py` | Automated checks that prove the logic is correct |

Try the prompt yourself first, then compare your result with the example.

## Modules

| # | Function | Use case |
|---|----------|----------|
| 01 | [Operations](../01-operations/) | Inventory reorder alerts |
| 02 | [Finance](../02-finance/) | Budget vs. actual variance report |
| 03 | [Human Resources](../03-hr/) | Leave balance tracker |
| 04 | [Marketing](../04-marketing/) | Campaign performance (CTR, CPA, ROAS) |
| 05 | [IT](../05-it/) | Helpdesk ticket SLA monitor |
| 06 | [Accounting](../06-accounting/) | Bank reconciliation |
| 07 | [Legal](../07-legal/) | Contract renewal and notice deadline tracker |
| 08 | [Procurement](../08-procurement/) | Vendor quote scoring |
| 09 | [Customer Service](../09-customer-service/) | Ticket triage by keyword |
| 10 | [General Affairs](../10-general-affairs/) | Meeting room booking conflicts |

## Exercise

Write an R-C-T-C-O prompt for one small, repetitive task from **your own job**. Do not run it yet. You will improve it after finishing a few modules.
