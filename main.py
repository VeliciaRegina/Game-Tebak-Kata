from models import GameSession


# Tampilan awal/judul game
print('='*45)
print("         GAME TEBAK KATA BERANTAI")
print("      ULAR -> RUSA -> AYAM -> MONYET")
print('=' *45)

def peraturan():
   """Menu Peraturan Cara Bermain"""

   print('=' *45)
   print("           PERATURAN CARA BERMAIN")
   print('=' *45)

   print("| 1 | Game dimainkan 2 pemain               |")
   print("| 2 | Pilih tema : Hewan / Negara / Buah    |")
   print("| 3 | Kata harus sambung huruf terakhir     |")
   print("| 4 | Jawaban salah = nyawa berkurang       |")
   print("| 5 | Hint mengurangi skor                  |")
   print("| 6 | Setiap jawaban benar +10 poin         |")

   print('=' *45)

   # Menunggu pemain menekan ENTER
   input("Tekan ENTER untuk kembali...")


def mulai_game():
   """Memulai permainan"""

   sesi = GameSession()

   # mulai game
   sesi.start_game()


def menu_utama():
   """Menampilkan menu utama game"""

   jalan = True

   # Perulangan menu selama pemain belum keluar
   while jalan:
      print(" ")
      print("┌──────────────────────────────┐")
      print("│ 1. PERATURAN                 │")
      print("│ 2. MULAI GAME                │")
      print("│ 3. LEADERBOARD               │")
      print("│ 4. KELUAR                    │")
      print("└──────────────────────────────┘")

      # Input pilihan menu
      pilih = input("Pilih menu : ")

      # peraturan
      if pilih == "1":
         peraturan()

      # mulai game
      elif pilih == "2":
         mulai_game()

      # keluar
      elif pilih == "4":

         print('=' *45)
         print("         TERIMA KASIH TELAH BERMAIN")
         print('=' *45)

         # Menghentikan perulangan menu
         jalan = False

      # Jika input tidak sesuai
      else:
         print("\nPilihan tidak tersedia\n")


# Menjalankan program utama
menu_utama()
