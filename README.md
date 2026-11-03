# Vibe Coding for Everyone

Learn to build small, useful business tools by **describing what you want to an AI assistant** (Claude Code). Each module takes a real problem from a business function, gives you the prompt to use, a working example, tests, and exercises.

No programming background needed. There are two ways in:

- **Self-study in English:** start with [Module 00](modules/00-getting-started/), then pick the module for your business function.
- **Structured course in Bahasa Indonesia:** follow the three-level training path below, from first terminal command to a secured web app your team uses.

## 🇮🇩 Materi Pelatihan: Zero to Hero (Bahasa Indonesia)

A step-by-step training path in Bahasa Indonesia that uses the modules below as case studies. Start at the [learning map](training/README.md).

| Level | Rencana | Paket modul | Durasi | Hasil |
|-------|---------|-------------|--------|-------|
| 🟢 Dasar | [01-dasar.md](training/01-dasar.md) | [training/dasar/](training/dasar/README.md) | ± 12 jam, 2 minggu (4 sesi) | Menyiapkan alat, menulis prompt R-C-T-C-O, menjalankan & memverifikasi skrip, Git dasar |
| 🟡 Menengah | [02-menengah.md](training/02-menengah.md) | [training/menengah/](training/menengah/README.md) | ± 25 jam, 4 minggu (8 sesi) | Tes, debugging, SQL, `CLAUDE.md`, branch & review, data aman |
| 🔴 Mahir | [03-mahir.md](training/03-mahir.md) | [training/mahir/](training/mahir/README.md) | ± 45 jam, 6–8 minggu (12 sesi) | Aplikasi web (Flask + React), keamanan OWASP, fitur lanjutan Claude Code, Claude API, CI/CD, Docker |

Each level has a **plan** (`0N-<level>.md`, one "Langkah" per step) and a **module pack** with:

- 10 modules, one per Langkah: material, guided practice, graded exercises (⭐ to ⭐⭐⭐), a quiz and an answer key
- a final project with a grading rubric and a reference answer
- a 15-question pre/post test and graduation criteria
- a facilitator guide with a minute-by-minute session rundown: [Dasar](training/dasar/panduan-fasilitator.md), [Menengah](training/menengah/panduan-fasilitator.md), [Mahir](training/mahir/panduan-fasilitator.md)
- a `latihan/` folder with tested practice code and answer keys

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

On Windows, activate with `.venv\Scripts\Activate.ps1` (PowerShell) or `.venv\Scripts\activate.bat` (Command Prompt).

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

Check that the code is tidy (the same checks run before every change):

```bash
ruff check . && ruff format --check .
```

### Training practice files

`pytest` on its own runs only `modules/`. The practice code in `training/` has its own tests; run each folder separately:

```bash
pytest training/menengah/latihan/test_expense_claims.py training/menengah/latihan/kunci
```

```bash
pip install -r training/mahir/latihan/ruang-rapat/backend/requirements.txt
```

```bash
pytest training/mahir/latihan/ruang-rapat/backend
```

```bash
pytest training/mahir/latihan/kunci/backend-lengkap
```

```bash
pytest training/mahir/latihan/klasifikasi
```

`training/menengah/latihan/test_overtime_pay.py` is **meant to fail 1 of 4 tests**: it holds a planted bug for the Level 2 debugging lesson. The Level 3 Claude API tests use a fake client, so they need no API key.

## Repository layout

```
modules/            10 business-function lessons (English): script, tests, synthetic CSV, README
  00-getting-started/   tools, the vibe coding loop, the R-C-T-C-O prompt template
training/           Zero-to-hero course (Bahasa Indonesia)
  README.md             learning map, glossary, data safety rules
  01-dasar.md ...       level plans (one "Langkah" per step)
  dasar/ menengah/ mahir/   module packs: modules, practice code, final project, tests, facilitator guide
CLAUDE.md           Instructions Claude Code follows in this repo (conventions, commands, gotchas)
pyproject.toml      pytest and ruff settings (not an installable package)
```

Working on this repo with Claude Code? [CLAUDE.md](CLAUDE.md) explains the module contract, why file names must be unique, and which training text quotes which program output.

## Data privacy

All sample data in this repository is **synthetic** (made up). Never paste or commit real personal data, employee records, ID numbers (KTP/NIK), salaries, customer details or confidential contracts. That data is protected by laws such as Indonesia's UU PDP (UU No. 27/2022) and the GDPR.
