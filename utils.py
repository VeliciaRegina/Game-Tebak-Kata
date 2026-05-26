def clear_screen():
    """Bersihkan layar dengan mencetak banyak baris kosong."""
    print("\n" * 40)

def tampilkan_data(judul, daftar_baris):
    """
    Tampilkan data dalam bentuk tabel sederhana.
    judul: string (misal "LEADERBOARD")
    daftar_baris: list of list (setiap list adalah satu baris data)
    """
    print("\n" + "=" * 40)
    print(judul.center(40))
    print("=" * 40)
    for baris in daftar_baris:
        print("   ".join(str(x) for x in baris))
    print("=" * 40)

def tekan_enter():
    """Tunggu user menekan Enter."""
    input("\nTekan Enter untuk melanjutkan...")