# Kunci Latihan 10 (Akuntansi): rekonsiliasi bank dengan JOIN di SQLite.
import csv
import sqlite3
from decimal import Decimal
from pathlib import Path

DATA = Path(__file__).resolve().parents[4] / "modules" / "06-accounting" / "data"
TOLERANCE_DAYS = 3

conn = sqlite3.connect(":memory:")
# Nama tabel berasal dari daftar tetap di bawah ini, bukan dari input pengguna,
# jadi aman disisipkan ke teks SQL. Nilai data tetap lewat parameter ?.
for table, description_column, file_name in [
    ("bank", "description", "bank_statement.csv"),
    ("ledger", "reference", "ledger.csv"),
]:
    conn.execute(
        f"CREATE TABLE {table} (id INTEGER PRIMARY KEY, txn_date TEXT, description TEXT, "
        "amount_cents INTEGER)"
    )
    with (DATA / file_name).open(newline="", encoding="utf-8") as f:
        rows = [
            (r["date"], r[description_column], int(Decimal(r["amount"]) * 100))
            for r in csv.DictReader(f)
        ]
    conn.executemany(
        f"INSERT INTO {table} (txn_date, description, amount_cents) VALUES (?, ?, ?)", rows
    )

# Pasangan kandidat: nominal sama dan selisih tanggal paling banyak TOLERANCE_DAYS hari.
MATCH_CONDITION = """
    l.amount_cents = b.amount_cents
    AND ABS(julianday(l.txn_date) - julianday(b.txn_date)) <= ?
"""

print("Cocok:")
query = f"""
    SELECT b.txn_date, b.description, l.txn_date, l.description, b.amount_cents
    FROM bank AS b
    JOIN ledger AS l ON {MATCH_CONDITION}
    ORDER BY b.txn_date
"""
for bank_date, bank_desc, ledger_date, ledger_desc, cents in conn.execute(query, (TOLERANCE_DAYS,)):
    print(f"  {bank_date} {bank_desc:<26} = {ledger_date} {ledger_desc:<18} {cents / 100:>10,.2f}")

ONLY_IN_BANK = f"""
    SELECT b.txn_date, b.description, b.amount_cents
    FROM bank AS b
    WHERE NOT EXISTS (SELECT 1 FROM ledger AS l WHERE {MATCH_CONDITION})
    ORDER BY b.txn_date
"""
ONLY_IN_LEDGER = f"""
    SELECT l.txn_date, l.description, l.amount_cents
    FROM ledger AS l
    WHERE NOT EXISTS (SELECT 1 FROM bank AS b WHERE {MATCH_CONDITION})
    ORDER BY l.txn_date
"""
for title, query in [
    ("Hanya di bank (catat di pembukuan):", ONLY_IN_BANK),
    ("Hanya di ledger (cek waktu/kesalahan):", ONLY_IN_LEDGER),
]:
    print(f"\n{title}")
    for txn_date, description, cents in conn.execute(query, (TOLERANCE_DAYS,)):
        print(f"  {txn_date} {description:<26} {cents / 100:>10,.2f}")
conn.close()
