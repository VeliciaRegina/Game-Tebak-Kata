from models import GameSession, WordDictionary
from leaderboard import Leaderboard
from utils import clear_screen, enter_and_clear

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
   enter_and_clear()

def mulai_game():
   """Memulai permainan"""

   sesi = GameSession()

   # mulai game
   sesi.start_game()

def menu_leaderboard():
   '''Menampilkan menu yang berkaitan dengan leaderboard'''
   board = Leaderboard()

   while True:
      print('\n+========================+')
      print('|    MENU LEADERBOARD    |')
      print('+========================+')
      print('|1. Lihat Leaderboard    |')
      print('|2. Hapus Leaderboard    |')
      print('|3. Kembali              |')
      print('+========================+')

      opsi = input('Pilih : ')

      match opsi:
         case "1":  # Tampilkan Leaderboard
            board.tampilkan()
            enter_and_clear()

         case "2": # Menghapus Leaderboard
            konfirmasi = input('Yakin hapus semua data? (Y/N): ').upper()
            if konfirmasi == 'Y':
               board.bersihkan()
            enter_and_clear()

         case "3": clear_screen(); break # kembali
         case _: print('Pilihan tidak valid.')

def tampilkan_dictionary():
   '''Menampilkan semua kata dan mencari kata'''
   dictionary = WordDictionary()
   dictionary.display_dictionary()
   print('\n---------------------------------------------------------------------------------------------------------------------------------')
   search = input('Masukkan kata yang ingin anda cari (jika ada): ')
   search = dictionary.search_words(search)

   if search == 1: print ('Ditemukan.')
   else: print('Tidak ditemukan.')
   enter_and_clear()

def menu_utama():
   """Menampilkan menu utama game"""

   jalan = True

   # Perulangan menu selama pemain belum keluar
   while jalan:
      # Tampilan awal/judul game
      print('='*45)
      print("         GAME TEBAK KATA BERANTAI")
      print('=' *45)

      print(" ")
      print("┌─────────────────────────────────┐")
      print("│ 1. PERATURAN                    │")
      print("│ 2. MULAI GAME                   │")
      print("│ 3. LEADERBOARD                  │")
      print("│ 4. MENAMPILKAN DICTIONARY KATA  │")
      print("│ 5. KELUAR                       │")
      print("└─────────────────────────────────┘")

      # Input pilihan menu
      pilih = input("Pilih menu : ")

      
      match pilih:
         case "1": # peraturan
            clear_screen()
            peraturan()
      
         case "2": # mulai game
            clear_screen()
            mulai_game()

         case "3": # menampilkan menu leaderboard
            clear_screen()
            menu_leaderboard()

         case '4': #Menampilkan dictionary
            clear_screen()
            tampilkan_dictionary()

         case '5': # keluar
            print()
            print('=' *45)
            print("         TERIMA KASIH TELAH BERMAIN")
            print('=' *45)
            jalan = False

         case _: # jika tidak meilih 1/2/3
            print('Pilihan tidak valid.')
            enter_and_clear()


# Menjalankan program utama
menu_utama()
