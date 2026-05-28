from algoritma import merge_sort, binary_search

class Leaderboard:
    '''Digunakan untuk mengatur leaderboard permainan.'''
    def __init__(self, nama_file='leaderboard.txt'):
        self.nama_file = nama_file
        self.data = []
        self._muat_dari_file()

    def _muat_dari_file(self):
        """Baca data dari file jika ada"""
        self.data = []
        try:
            with open(self.nama_file, 'r', encoding='utf-8') as f:
                for baris in f:
                    baris = baris.strip()
                    if baris:
                        potongan = baris.split(',')
                        if len(potongan) == 3:
                            nama, skor_str, tema = potongan
                            try:
                                skor = int(skor_str)
                                self.data.append([nama, skor, tema])
                            except:
                                pass
        except FileNotFoundError: # File belum ada
            return
        except:
            print("Tidak dapat membaca file. Data baru akan dibuat.")

    def _simpan_ke_file(self):
        """Simpan data ke file"""
        try:
            with open(self.nama_file, 'w', encoding='utf-8') as f:
                for item in self.data:
                    f.write(f"{item[0]},{item[1]},{item[2]}\n")
        except:
            print("Terjadi kesalahan saat menyimpan leaderboard. Data skor sementara tidak bisa disimpan.")

    def tambah_skor(self, nama, skor, tema):
        """Menambahkan skor baru."""
        self.data.append((nama, skor, tema))
        self._simpan_ke_file()

    def tampilkan(self, batas=10):
        """Tampilkan leaderboard ke layar."""
        if not self.data:
            print("\nLeaderboard masih kosong.")
            return
        terurut = merge_sort(self.data)
        print("\n" + "=" * 40)
        print("        L E A D E R B O A R D")
        print("=" * 40)
        print("No.  Nama           Skor   Tema")
        print("-" * 40)
        for i in range(min(batas, len(terurut))):
            nama, skor, tema = terurut[i]
            tema_bersih = tema.replace('.txt', '').capitalize()
            print(f"{i+1:<4} {nama:<14} {skor:<6} {tema_bersih}")
        print("=" * 40)

    def bersihkan(self):
        """Hapus semua data leaderboard."""
        self.data = []
        self._simpan_ke_file()
        print("Leaderboard sudah dikosongkan.")