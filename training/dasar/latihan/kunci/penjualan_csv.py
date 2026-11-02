# Kunci Latihan 6.4: membaca data dari file CSV, menghitung total dan cabang terbaik.
import csv
from pathlib import Path

DATA = Path(__file__).parent.parent / "data" / "penjualan_cabang.csv"
TARGET = 80_000_000


def baca_penjualan(path: Path) -> dict[str, int]:
    with path.open(newline="", encoding="utf-8") as f:
        return {baris["cabang"]: int(baris["penjualan"]) for baris in csv.DictReader(f)}


penjualan = baca_penjualan(DATA)
for cabang, nilai in penjualan.items():
    status = "TERCAPAI" if nilai >= TARGET else "BELUM"
    print(f"{cabang:<10} Rp{nilai:>13,}  {status}")

terbaik = max(penjualan, key=penjualan.get)
print(f"\nTotal penjualan : Rp{sum(penjualan.values()):,}")
print(f"Cabang terbaik  : {terbaik} (Rp{penjualan[terbaik]:,})")
jumlah_tercapai = sum(1 for nilai in penjualan.values() if nilai >= TARGET)
print(f"Target tercapai : {jumlah_tercapai} dari {len(penjualan)} cabang")
