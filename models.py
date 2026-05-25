import random #JANGAN LUPAAAAA
from struktur_data.tree import WordTree
from struktur_data.hash_table import HashTable
from struktur_data.graph import Graph
from struktur_data.queue import Queue
from struktur_data.single_linked_list import SingleLinkedList
from struktur_data.double_linked_list import DoubleLinkedList
from struktur_data.circular_linked_list import CircularLinkedList
from game_logic import read_words_from_file, build_graph, generate_hint


class Player:
   '''Digunakan untuk menyimpan info yang berkaitan dengan data pemain (nama, skor, nyawa)'''
   def __init__(self, name):
      self.name = name
      self.score = 0
      self.lives = 3

   def is_alive(self):
      return self.lives > 0

   def add_score(self, poin):
      if self.is_alive():
         self.score += poin

   def reduce_live(self):
      if self.is_alive():
         self.lives -= 1
   
   def display_player(self):
      print(f'Nama   :{self.name}')
      print(f'Skor   :{self.score}')
      print(f'Nyawa  :{self.lives}')

class GameSession:
   '''Mengatur jalannya alur permainan'''
   def __init__(self):
      self.current_word = None
      self.game_status = True
      #Struktur Data
      self.word_tree = WordTree() #Pencarian dan kategori kata
      self.word_graph = Graph() #Hubungan antar kata
      self.word_database = HashTable() #Menyimpan semua kata
      self.used_word = HashTable() #Menyimpan kata yang sudah dipakai
      
      self.hint_queue = Queue() #Menyimpan antrian petunjuk
      
      self.score_history = SingleLinkedList() #Menyimpan score permainan
      self.word_path = DoubleLinkedList() #Menyimpan perjalanan kata
      self.player_turn = CircularLinkedList() #Mengatur giliran pemain

   def setup_player(self):
      '''Menyiapkan data pemain'''
      for i in range(2):
         name = input(f'Masukkan nama player {i+1}: ')
         player = Player(name) #Memanggil class Player
         self.player_turn.append(player)
   
   def choose_theme(self):
      '''Player memilih tema permainan'''

      print('\n=========================')
      print('        PILIH TEMA')
      print('=========================')
      print('1. Hewan')
      print('2. Negara')
      print('-------------------------')
      while True:
         try:
            tema = int(input('Pilih tema: '))
            if tema == 1: return 'hewan.txt'
            elif tema == 2: return 'negara.txt'
            else: print('Opsi tidak valid.')
         except ValueError:
            print('Opsi tidak valid.')
   
   def load_words(self, filename):
      '''Menambahkan kata-kata ke struktur data'''
      words = read_words_from_file(filename)
      for x in words:
         self.word_tree.insert(x) #Tree
         self.word_database.insert(x, True) #Hash table database
         self.word_graph.add_vertex(x) #Menambah node/kata ke graph
      build_graph(self.word_graph, words) #Menghubungkan edge

   def setup_game(self):
      '''Menentukan kata random di awal permainan'''
      #Ambil semua kata adri hashtable
      all_words = self.word_database.get_all_data()

      #Pilih kata random
      if all_words:
         self.current_word = random.choice(all_words)
      else:
         return 'Tidak ada kata dalam database'

      #Tandai kata sudah dipakai
      self.used_word.insert(self.current_word, True)

      #Simpan ke history
      self.word_history.push(self.current_word)

      #Simpan perjalanan kata
      self.word_path.append(self.current_word)

      #Buat hint
      hint = generate_hint(self.current_word, self.word_graph)
      self.hint_queue.enqueue(hint)

   def next_turn(self):
      '''Menjalankan turn permainan (user input kata)'''
      current_player = self.player_turn.get_current()
      print(f'\nGiliran: {current_player.name} ({current_player.lives} nyawa)  |  Skor: {current_player.score}')
      print(f'Kata sekarang: {self.current_word}')

      #Tanya apakah player ingin menggunakan hint
      choice = input('Gunakan hint (score -5)? y/n: ').upper()
      if choice == 'Y':
         hints = generate_hint(self.current_word, self.word_graph)
         print(f'\nHint: ')
         if hints:
            current_player.score -= 5
            for word in hints:
               print('-', word)
         else: print ('Tidak ada petunjuk yang tersedia!')
      
      print('-' *35)
      answer = input('Masukkan kata: ').upper()
      valid = self.validate_answer(answer)

      if valid:
         print('Jawaban benar!')
         self.update_word(answer)
         self.update_score(current_player, 10)
      elif valid == 'Used':
         print('Kata sudah digunakan.')
      else:
         print('Jawaban salah')
         current_player.reduce_live()
      self.player_turn.next_turn()

   def validate_answer(self, answer):
      '''Mengecek apakah jawaban pemain benar. mengembalikan True/False/Used'''
      answer_upper = answer.upper()
      # Cek ada di database
      if not self.word_database.get(answer_upper):
         return False
      
      # Cek sudah dipakai
      if self.used_word.get(answer_upper):
         return 'Used'
      
      # Cek sambungan huruf
      if answer_upper[0] != self.current_word[-1]:
         return False
      return True

   def update_score(self, player, score):
      '''Mengubah skor pemain'''
      player.score += score

      self.score_history.append(
         f'{player.name}: {player.score}')

   def update_word(self, word):
      '''Mengubah kata terakhir permainan'''
      new_word = word.upper()
      # Update kata sekarang
      self.current_word = new_word

      # simpan ke used word
      self.used_word.insert(new_word, True)

      # simpan perjalanan
      self.word_path.append(new_word)

      # buat hint baru
      hint = f'Kata berikutnya dimulai huruf {new_word[-1]}'
      self.hint_queue.enqueue(hint)

   def end_game(self):
      print('\n======== GAME SELESAI ========')

      # Tampilkan score
      current = self.player_turn.head
      player = current.data

      while True:
         # Ambil data dari player aktif saat ini
         player = current.data
         print(f'{player.name} : {player.score}')

         # Geser ke node berikutnya
         current = current.next

         if current == self.player_turn.head: #Mencegah endless loop
            break

      # Perjalanan kata
      print('\nPerjalanan kata:')
      self.word_path.display_forward()
      self.game_status = False

   def start_game(self):
      '''Memulai permainan'''
      print('======= GAME DIMULAI! =======')
      self.setup_player() #Menyiapkan data player
      tema = self.choose_theme() #Memilih tema permainan
      self.load_words(tema) #Memuat data ke database
      self.setup_game() #Meyiapkan kata pertama secara acak

      while self.game_status:
         #Mengambi data player yang sedang aktif sebelum turn berjalan
         current = self.player_turn.get_current()
         self.next_turn()
         if not current.is_alive():
            print(f'\n[GAME OVER] {current.name} telah kehabisan nyawa!')
            self.end_game()

   def display_dictionary(self):
         '''Menampilkan seluruh kosakata yang dikelompokkan berdasarkan huruf abjad'''
         print('\n=====================================')
         print('       DICTIONARY GAME (A-Z)')
         print('=====================================')

         # Menggunakan fungsi display() dari WordTree
         self.word_tree.display()
         print('=====================================')