from algoritma import merge_sort

class TreeNode:
   def __init__(self, letter =''):
      self.letter = letter
      self.children = {}
      self.words = []

class WordTree:
   '''Digunakan untuk penyimpanan struktur kata untuk fitur petunjuk'''
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

#tree = WordTree()
#tree.insert("ULAR")
#tree.insert("UDANG")
#tree.insert("UNTA")
#tree.insert("HARIMAU")
#tree.insert("HIU")
#tree.insert('Ayam')
#tree.display()
#h = tree.get_words_by_letter('h')
#print(f'H: {h}')
#word_tree = WordTree()
#for words in animal_words:
#   word_tree.insert(words)
#word_tree.display()