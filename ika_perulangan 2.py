def hitung_jarak_minggu():
    jarak = 5
    pertumbuhan_jarak = 0.10
    minggu = 0

    while jarak <= 10:
        jarak += jarak * pertumbuhan_jarak
        minggu += 1

    return minggu

def main():
    minggu_dibutuhkan = hitung_jarak_minggu()
    print(f"Dibutuhkan {minggu_dibutuhkan} minggu agar pelari dapat berlari lebih dari 10 kilometer.")

if __name__ == "__main__":
    main()
