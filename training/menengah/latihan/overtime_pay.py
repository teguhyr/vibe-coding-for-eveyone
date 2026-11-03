"""Latihan Modul 3: kalkulator upah lembur hari kerja. FILE INI SENGAJA BERISI BUG.

Aturan (disederhanakan dari PP 35/2021, hari kerja biasa):
- Upah per jam = upah bulanan / 173.
- Jam lembur pertama dibayar 1,5 x upah per jam.
- Jam lembur kedua dan seterusnya dibayar 2 x upah per jam.
- Lembur maksimal 4 jam per hari.
Hasil dibulatkan ke Rupiah terdekat. Data contoh fiktif.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

DEFAULT_DATA = Path(__file__).parent / "data" / "lembur_oktober.csv"
HOURS_PER_MONTH = 173
MAX_HOURS_PER_DAY = 4


@dataclass(frozen=True)
class OvertimeEntry:
    employee_id: str
    work_date: str
    monthly_wage: int
    hours: int


def overtime_pay(monthly_wage: int, hours: int) -> int:
    if hours > MAX_HOURS_PER_DAY:
        raise ValueError(f"overtime is limited to {MAX_HOURS_PER_DAY} hours a day, got {hours}")
    hourly = Decimal(monthly_wage) / HOURS_PER_MONTH
    first_hour = min(hours, 1)
    next_hours = hours - 1
    pay = hourly * Decimal("1.5") * first_hour + hourly * 2 * next_hours
    return int(pay.quantize(Decimal("1"), rounding=ROUND_HALF_UP))


def load_entries(path: Path) -> list[OvertimeEntry]:
    with path.open(newline="", encoding="utf-8") as f:
        return [
            OvertimeEntry(r["employee_id"], r["date"], int(r["monthly_wage"]), int(r["hours"]))
            for r in csv.DictReader(f)
        ]


def main() -> None:
    parser = argparse.ArgumentParser(description="Overtime pay calculator.")
    parser.add_argument("csv_file", nargs="?", type=Path, default=DEFAULT_DATA)
    args = parser.parse_args()

    print(f"{'Emp':<5} {'Date':<10} {'Hours':>5} {'Pay':>10}")
    for e in load_entries(args.csv_file):
        pay = overtime_pay(e.monthly_wage, e.hours)
        print(f"{e.employee_id:<5} {e.work_date:<10} {e.hours:>5} {pay:>10,}")


if __name__ == "__main__":
    main()
