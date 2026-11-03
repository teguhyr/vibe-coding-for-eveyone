# Kunci Latihan 6.2-6.3: muat klaim reimburse ke SQLite, lalu jawab pertanyaan dengan SQL.
import csv
import sqlite3
from pathlib import Path

CSV_FILE = Path(__file__).parent.parent / "data" / "klaim_reimburse.csv"

# ":memory:" = database sementara di memori; tidak ada file .db yang tertinggal.
conn = sqlite3.connect(":memory:")
conn.execute("""
    CREATE TABLE claims (
        claim_id       TEXT PRIMARY KEY,
        employee_id    TEXT NOT NULL,
        department     TEXT NOT NULL,
        category       TEXT NOT NULL,
        expense_date   TEXT NOT NULL,
        submitted_date TEXT NOT NULL,
        amount         INTEGER NOT NULL CHECK (amount > 0),
        receipt        TEXT NOT NULL CHECK (receipt IN ('yes', 'no'))
    )
""")
with CSV_FILE.open(newline="", encoding="utf-8") as f:
    rows = [
        (
            r["claim_id"],
            r["employee_id"],
            r["department"],
            r["category"],
            r["expense_date"],
            r["submitted_date"],
            int(r["amount"]),
            r["receipt"],
        )
        for r in csv.DictReader(f)
    ]
conn.executemany("INSERT INTO claims VALUES (?, ?, ?, ?, ?, ?, ?, ?)", rows)
conn.commit()

print("Total klaim per departemen (sebelum aturan):")
query = """
    SELECT department, COUNT(*) AS claims, SUM(amount) AS total
    FROM claims
    GROUP BY department
    ORDER BY total DESC
"""
for row in conn.execute(query):
    print(row)

print("\nKlaim tanpa bukti dengan nilai minimal Rp100.000:")
min_amount = 100_000  # nilai dari luar selalu lewat parameter ?, bukan digabung ke teks SQL
query = "SELECT claim_id, amount FROM claims WHERE receipt = 'no' AND amount >= ?"
for row in conn.execute(query, (min_amount,)):
    print(row)

print("\nKlaim yang diajukan lebih dari 30 hari setelah tanggal biaya:")
query = """
    SELECT claim_id,
           CAST(julianday(submitted_date) - julianday(expense_date) AS INTEGER) AS days
    FROM claims
    WHERE julianday(submitted_date) - julianday(expense_date) > 30
"""
for row in conn.execute(query):
    print(row)
conn.close()
