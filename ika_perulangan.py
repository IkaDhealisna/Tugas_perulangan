def hitung_jumlah_ayam():
    jumlah_ayam = 100
    pertumbuhan_ayam = 0.05
    bulan = 0

    while jumlah_ayam <= 200:
        jumlah_ayam += jumlah_ayam * pertumbuhan_ayam
        bulan += 1

    return bulan

def main():
    bulan_dibutuhkan = hitung_jumlah_ayam()
    print(f"Dibutuhkan {bulan_dibutuhkan} bulan agar jumlah ayam melebihi 200.")

if __name__ == "__main__":
    main()
