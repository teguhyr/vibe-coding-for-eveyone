# Vibe Coding for Everyone

Learn to build small, useful business tools by **describing what you want to an AI assistant** (Claude Code). Each module takes a real problem from a business function, gives you the prompt to use, a working example, tests, and exercises.

No programming background needed. Start with [Module 00](modules/00-getting-started/).

## 🇮🇩 Materi Pelatihan: Zero to Hero (Bahasa Indonesia)

A step-by-step training path in Bahasa Indonesia that uses the modules below as case studies. Start at the [learning map](training/README.md).

| Level | Materi | Hasil |
|-------|--------|-------|
| 🟢 Dasar | [training/01-dasar.md](training/01-dasar.md) | Menyiapkan alat, menulis prompt, menjalankan & memverifikasi skrip, Git dasar |
| 🟡 Menengah | [training/02-menengah.md](training/02-menengah.md) | Tes, debugging, SQL, `CLAUDE.md`, branch & review, data aman |
| 🔴 Mahir | [training/03-mahir.md](training/03-mahir.md) | Aplikasi web (Flask + React), keamanan OWASP, fitur lanjutan Claude Code, Claude API, CI/CD, Docker |

## Modules

| # | Function | Use case | Key concept |
|---|----------|----------|-------------|
| 00 | [Getting Started](modules/00-getting-started/) | Tools, the vibe coding loop, prompt formula | R-C-T-C-O prompts |
| 01 | [Operations](modules/01-operations/) | Inventory reorder alerts | Reorder point, sorting |
| 02 | [Finance](modules/02-finance/) | Budget vs. actual variance | `Decimal` for money |
| 03 | [Human Resources](modules/03-hr/) | Leave balance tracker | Working days, joining data, privacy |
| 04 | [Marketing](modules/04-marketing/) | Campaign CTR / CPC / CPA / ROAS | Safe division, ranking |
| 05 | [IT](modules/05-it/) | Helpdesk ticket SLA monitor | Date/time arithmetic |
| 06 | [Accounting](modules/06-accounting/) | Bank reconciliation | Matching with tolerance |
| 07 | [Legal](modules/07-legal/) | Contract notice deadlines | Date boundaries |
| 08 | [Procurement](modules/08-procurement/) | Vendor quote scoring | Normalization, weighted scores |
| 09 | [Customer Service](modules/09-customer-service/) | Message triage | Keyword rules, regex |
| 10 | [General Affairs](modules/10-general-affairs/) | Meeting room double bookings | Interval overlap |

## Quick start

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

```bash
pip install -r requirements-dev.txt
```

```bash
pytest
```

```bash
python modules/01-operations/inventory_reorder.py
```

The example scripts use only the Python standard library. `pytest` and `ruff` are only needed for testing and linting.

## Data privacy

All sample data in this repository is **synthetic** (made up). Never paste or commit real personal data, employee records, ID numbers (KTP/NIK), salaries, customer details or confidential contracts. That data is protected by laws such as Indonesia's UU PDP (UU No. 27/2022) and the GDPR.
