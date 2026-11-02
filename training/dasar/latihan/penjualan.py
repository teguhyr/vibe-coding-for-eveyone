# Latihan Modul 6: membaca dan mengubah kode sederhana.
# Data contoh (fiktif): penjualan per cabang dalam Rupiah.
penjualan = {"Jakarta": 120_000_000, "Surabaya": 85_000_000, "Medan": 40_000_000}
target = 80_000_000


def status_cabang(nilai: int, target: int) -> str:
    if nilai >= target:
        return "TERCAPAI"
    return "BELUM"


for cabang, nilai in penjualan.items():
    print(f"{cabang:<10} Rp{nilai:>13,}  {status_cabang(nilai, target)}")
