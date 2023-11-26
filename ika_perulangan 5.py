def hitung_pembelahan_bakteri(waktu):
    interval_pembelahan = 20
    jumlah_pembelahan = waktu // interval_pembelahan
    return jumlah_pembelahan

def main():
    waktu_total = 120  # dalam menit
    jumlah_pembelahan = hitung_pembelahan_bakteri(waktu_total)
    print(f"Selama 2 jam, bakteri mengalami pembelahan sebanyak {jumlah_pembelahan} kali.")

if __name__ == "__main__":
    main()
