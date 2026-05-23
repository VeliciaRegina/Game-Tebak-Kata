from struktur_data import WordTree, HashTable, Graph

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
   def __init__(self, players):
      self.players = players
      self.turn_index = 0
      self.tema = None
      self.game_over = False
      #self.cur_word = current_word
      self.word_tree = WordTree
      self.word_database = HashTable()
      self.used_word = HashTable()
      self.word_graph = Graph()

   def start_game(self):
      '''Memulai permainan'''
      
      print('========= Pilih Tema =========')
      print('1. Hewan')
      print('2. Negara')
      print('------------------------------')
      while True:
         try:
            tema = int(input('Pilih tema: '))
            if tema == 1:
               file_name = 'words_animal.txt'
               with open(file_name, 'r') as file:
                  for line in file:
                     word = line.upper()
                     self.word_tree.insert(word)
                     self.word_database.insert(word)

            elif tema == 2: 
               file_name = 'words_country.txt'
               with open(file_name, 'r') as file:
                  for line in file:
                     word = line.upper()

            else:print('Opsi tidak valid.')
         except:
            print('Opsi tidak valid.')


   def next_turn(self):
      current_player = self.players[self.turn_index]
      print(f'Giliran {current_player.name}')

      word = input('Masukkan kata: ')

      # Validasi kata
      self.validate_word(word)
      #if valid: lanjut
      #else: kurangi nyawa

      # Mengudate kata aktif berikutnya
      self.update_word(word)

      # Ganti giliran
      self.turn_index = (self.turn_index + 1) % len(self.players)


   def validate_word(self, word):
      pass

   def update_word(self, word):
      '''Mengubah kata terakhir permainan'''
      pass

   def end_game(self):
      pass

class WordNode:
   '''Node menyimpan kata'''
   def __init__(self, word):
      self.word = word
      self.next = None
      self.prev = None

p1 = Player('wawa')
p2 = Player('wowo')
main = GameSession([p1, p2], )

main.start_game()