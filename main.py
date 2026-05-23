from models import Player, GameSession
from struktur_data import Queue

def main_menu():
   print('==============================')
   print('   GAME TEBAK KATA BERANTAI')
   print('==============================')
   print('1. Mulai Game')
   print('2. Leaderboard')
   print('3. Bantuan')
   print('4. Keluar')

   # Membuat class Player
   nama1 = input('Masukkan nama player 1: ')
   nama2 = input('Masukkan nama player 1: ')
   player1 = Player(nama1)
   player2 = Player(nama2)

   # Membuat lobby menggunakan Queue
   lobby = Queue()
   lobby.enqueue(player1)
   lobby.enqueue(player2)

   sesi = GameSession([player1, player2])
   sesi.start_game()

   while sesi.game_running:
      pass