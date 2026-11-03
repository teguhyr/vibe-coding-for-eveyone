# Kunci latihan lanjutan Langkah 6: JOIN data HR dan GROUP BY data keuangan.
import csv
import sqlite3
from decimal import Decimal
from pathlib import Path

MODULES = Path(__file__).resolve().parents[4] / "modules"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


conn = sqlite3.connect(":memory:")
conn.execute("""
    CREATE TABLE employees (
        employee_id TEXT PRIMARY KEY,
        name        TEXT NOT NULL,
        department  TEXT NOT NULL
    )
""")
conn.execute("""
    CREATE TABLE leave_requests (
        employee_id TEXT NOT NULL REFERENCES employees (employee_id),
        start_date  TEXT NOT NULL,
        end_date    TEXT NOT NULL,
        status      TEXT NOT NULL
    )
""")
conn.executemany(
    "INSERT INTO employees VALUES (?, ?, ?)",
    [
        (r["employee_id"], r["name"], r["department"])
        for r in read_csv(MODULES / "03-hr/data/employees.csv")
    ],
)
conn.executemany(
    "INSERT INTO leave_requests VALUES (?, ?, ?, ?)",
    [
        (r["employee_id"], r["start_date"], r["end_date"], r["status"])
        for r in read_csv(MODULES / "03-hr/data/leave_requests.csv")
    ],
)

print("Jumlah pengajuan cuti per karyawan (JOIN):")
query = """
    SELECT e.name,
           COUNT(l.employee_id) AS requests,
           SUM(l.status = 'approved') AS approved
    FROM employees AS e
    LEFT JOIN leave_requests AS l ON l.employee_id = e.employee_id
    GROUP BY e.employee_id, e.name
    ORDER BY e.employee_id
"""
for row in conn.execute(query):
    print(row)

# Uang disimpan dalam sen (bilangan bulat) agar penjumlahan persis, tanpa selisih float.
conn.execute("CREATE TABLE budget (department TEXT, category TEXT, actual_cents INTEGER)")
conn.executemany(
    "INSERT INTO budget VALUES (?, ?, ?)",
    [
        (r["department"], r["category"], int(Decimal(r["actual"]) * 100))
        for r in read_csv(MODULES / "02-finance/data/budget_vs_actual.csv")
    ],
)
print("\nTotal realisasi anggaran per departemen (GROUP BY):")
query = """
    SELECT department, SUM(actual_cents) AS actual_cents
    FROM budget
    GROUP BY department
    ORDER BY department
"""
for department, cents in conn.execute(query):
    print(f"{department:<12} {cents / 100:>12,.2f}")
conn.close()
