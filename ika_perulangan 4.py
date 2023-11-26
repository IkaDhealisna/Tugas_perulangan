def hitung_hari_apel():
    jumlah_apel = 100
    penjualan_harian = 0.10
    hari = 0

    while jumlah_apel >= 20:
        jumlah_apel -= jumlah_apel * penjualan_harian
        hari += 1

    return hari

def main():
    hari_dibutuhkan = hitung_hari_apel()
    print(f"Dibutuhkan {hari_dibutuhkan} hari agar sisa apel kurang dari 20 buah.")

if __name__ == "__main__":
    main()
