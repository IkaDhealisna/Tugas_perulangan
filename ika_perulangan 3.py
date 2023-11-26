def hitung_tahun_investasi():
    nilai_investasi = 10000
    pertumbuhan_investasi = 0.06
    tahun = 0

    while nilai_investasi <= 20000:
        nilai_investasi += nilai_investasi * pertumbuhan_investasi
        tahun += 1

    return tahun

def main():
    tahun_dibutuhkan = hitung_tahun_investasi()
    print(f"Dibutuhkan {tahun_dibutuhkan} tahun agar nilai investasi melebihi 20.000 dollar.")

if __name__ == "__main__":
    main()
