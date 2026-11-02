# Kunci Latihan 6.2 dan 6.3: format ribuan dengan titik + status "HAMPIR".
penjualan = {"Jakarta": 120_000_000, "Surabaya": 85_000_000, "Medan": 40_000_000}
target = 80_000_000


def format_rupiah(nilai: int) -> str:
    # Python memakai koma sebagai pemisah ribuan; ganti dengan titik ala Indonesia.
    return "Rp" + f"{nilai:,}".replace(",", ".")


def status_cabang(nilai: int, target: int) -> str:
    if nilai >= target:
        return "TERCAPAI"
    elif nilai >= target * 0.9:
        return "HAMPIR"
    return "BELUM"


for cabang, nilai in penjualan.items():
    print(f"{cabang:<10} {format_rupiah(nilai):>15}  {status_cabang(nilai, target)}")
