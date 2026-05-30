from algoritma import merge_sort

class TreeNode:
   def __init__(self, letter =''):
      self.letter = letter
      self.children = {}
      self.words = []

class WordTree:
   '''Digunakan untuk penyimpanan struktur kata untuk fitur menampilkan kamus'''
   def __init__(self):
      self.root = TreeNode('ROOT')

   def insert(self, word):
      '''Menambahkan kata ke tree'''
      word = word.upper()
      first_letter = word[0]

      # Jika huruf belum ada
      if first_letter not in self.root.children:
         self.root.children[first_letter] = TreeNode(first_letter)

      # Tambahkan kata
      self.root.children[first_letter].words.append(word)
   
   def get_words_by_letter(self, letter):
      '''Mengembalikan list kata berdasarkan huruf awal'''

      letter = letter.upper()
      if letter in self.root.children:
         return self.root.children[letter].words
      return []
   
   def display(self):
      '''Menampilkan isi tree'''
      sorted_letter = merge_sort(list(self.root.children.keys()))

      for letter in sorted_letter:
         words_list = self.root.children[letter].words
         print(f'[{letter}] : ', ', '.join(words_list))
         print()