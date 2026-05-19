from algoritma import merge_sort

class Stack:
   '''Digunakan untuk membatalkan kata terakhir yang diinput (undo)
'''
   def __init__(self):
      self.stack = [] #Menginisialisasi list bernama stack

   def is_empty(self):
      '''Mengecek apakah stack kosong'''
      return len(self.stack) == 0
   
   def push(self, data):
      '''Menambahkan data baru di akhir'''
      self.stack.append(data)

   def undo(self):
      '''Menghapus dan mengembalikan data paling belakang'''
      if self.is_empty():
         return 'Antrian kosong.'
      return self.stack.pop()
   
   def peek(self):
      '''Mengembalikan data terakhir dari stack'''
      if self.is_empty():
         return 'Antrian kosong.'
      return self.stack[-1]

   def size(self):
      '''Mengembalikan ukuran stack'''
      return len(self.stack)
   
   def display(self):
      '''Menampilkan data-data dalam stack'''
      print(self.stack)


#----------------------------------------------------------------
class Queque:
   '''Digunakan untuk antrean pemain di ruang tunggu sebelum mulai
'''
   def __init__(self):
      self.queue = [] #Menginisialisasi list bernama queuqe

   def is_empty(self):
      '''mengecek apakah queque kosong'''
      return len(self.queue) == 0

   def enqueue(self, data):
      '''Menambahkan data baru di akhir'''
      self.queue.append(data)
   
   def dequeue(self):
      '''Menghapus dan mengembalikan data paling depan'''
      if self.is_empty():
         return 'Antrian kosong.'
      return self.queue.pop(0)
   
   def peek(self):
      '''Mengembalikan elemen pertama di queue'''
      if self.is_empty():
         return 'Antrian kosong.'
      return self.queue[0]
   
   def size(self):
      '''Mengembalikan ukuran queue'''
      return len(self.queue)
   
   def display(self):
      '''Menampilkan data-data dalam queue'''
      print(self.queue)


#----------------------------------------------------------------
class NodeSingle:
   def __init__(self, data):
      self.data = data.upper()
      self.next = None

class SingleLinkedList:
   '''Digunakan untuk menyimpan rantai utama kata yang berhasil dijawab
   selama permainan berlangsung secara berurutan.'''
   def __init__(self):
      self.head = None

   def size(self):
      '''Mengembalikan ukura linked list'''
      current = self.head
      total = 0
      while current:
         total += 1
         current = current.next
      return total

   def insert (self, data):
      '''Menambahkan data ke akhir linked list'''
      new_node = NodeSingle(data)

      #Jika list kosong
      if self.head == None:
         self.head = new_node
         return
      
      #Jika list tidak kosong
      current = self.head
      while current.next:
         current = current.next
      current.next = new_node

   def delete(self, data):
      '''Menghapus data dari linked list'''
      target = data.upper()
      current = self.head
      prev = None

      #kondisi 1: target di posisi pertama
      if current.data == target:
         self.head = current.next
         return
      
      #kondisi 2: target di tengah atau akhir
      while current and current.data != target:
         prev = current
         current = current.next

      #kondisi 3: target tidak ditemukan
      while not current: 
         print(f'Data "{target}" tidak ditemukan.')
         return
      
      prev.next = current.next

   def traversal(self):
      '''Menampilkan data-data dalam linked list'''
      #jika linked list kosong
      if self.head == None:
         print('Antrian kosong')
         return
      
      #Jika linked list tidak kosong
      current = self.head
      count = 1
      while current:
         print(f'{count}. {current.data}')
         count += 1
         current = current.next
      print('-' *20)
      print(f'Jumlah: {self.size()}')


#----------------------------------------------------------------
class NodeDouble:
   def __init__(self, data):
      self.data = data.upper()
      self.prev = None
      self.next = None

class DoubleLinkedList:
   '''Digunakan pada fitur review history agar pemain dapat menelusuri
   riwayat kata sebelumnya maupun berikutnya secara dua arah.'''
   def __init__(self):
      self.head = None

   def append(self, data):
      '''Menambahkan data di akhir'''
      new_node = NodeDouble(data)

      # Jika linked list kosong
      if self.head == None:
         self.head = new_node
         return
      
      # Jika linked list tidak kosong
      current = self.head
      while current.next:
         current = current.next
      
      current.next = new_node
      new_node.prev = current

   def prepend(self, data):
      '''Menambahkan data di awal'''
      new_node = NodeDouble(data)

      if self.head != None:
         self.head.prev = new_node
         new_node.next = self.head

      self.head = new_node

   def delete(self, data):
      '''Menghapus data dari linked list'''
      target = data.upper()
      current = self.head

      while current:
         if current.data == target:
            #kondisi 1: posisi target di awal
            if current.prev == None:
               self.head = current.next
               if self.head:
                  self.head.prev = None
            else:
               # Menghubungkan node sebelumnya dengan node berikutnya
               current.prev.next = current.next

               if current.next:
                  # Menghubungkan node berikutnya dengan node sebelumnya
                  current.next.prev = current.prev
            return
         current = current.next

   def display_forward(self):
      current = self.head
      count = 1
      while current:
         print(f'{count}. {current.data}')
         count += 1
         current = current.next

   def display_backward(self):
      current = self.head
      count = 1

      # Menelusuri ke node terakhir
      while current.next :
         current = current.next

      # Tampilkan mundur
      while current:
         print(f'{count}. {current.data}')
         count += 1
         current = current.prev


#----------------------------------------------------------------
class NodeCircular:
   def __init__(self, data):
      self.data = data
      self.next = None

class CircularLinkedList:
   '''Digunakna untuk rotasi giliran pemain secara berputar'''
   def __init__(self):
      self.head = None
      self.current = None

   def get_current(self):
      return self.current.data

   def append(self, data):
      '''Menambahkan data di akhir'''
      new_node = NodeCircular(data)

      # Jika linked list kosong
      if self.head == None:
         self.head = new_node
         new_node.next = self.head
         self.current = self.head
         return

      # Jika linked list tidak kosong
      temp = self.head
      while temp.next != self.head:
         temp = temp.data
      
      # Menyambungkan node terakhir ke node baru
      temp.next = new_node
      new_node.next = self.head

   def display(self):
      '''Menampilkan giliran pemain'''
      if self.head == None:
         return 'Tidak ada pemain.'
      
      temp = self.head
      while True:
         print(temp.data, end=" -> ")
         temp = temp.next

         if temp == self.head:
            break
      print('(kembali ke head)')

   def next_turn(self):
      if self.current == None:
         return 'Tidak ada pemain'
      
      self.current = self.current.next #pindah ke pemain berikutnya
      return self.current.data #kembalian pemain yang mendapat giliran


#----------------------------------------------------------------
class HashTable:
   '''Digunakan untuk pengecekan instan kata baku dan kata duplikat'''
   def __init__(self):
      self.size = 15
      self.table = [[] for _ in range(self.size)]

   def hash_function(self, key):
      '''Megembalikan  unicode karakter modulo ukuran table'''
      total = 0

      #jumlah unicode tiap karakter
      for char in str(key):
         total += ord(char)
      return total % self.size

   def insert(self, key, value):
      '''Menambahkan pasangan key:value'''
      #cari indeks bucket
      index = self.hash_function(key)

      #ambil bucket di indekx tersebut
      bucket = self.table[index]

      #cek apakah value sudah ada
      for i, (k, v) in enumerate(bucket):
         #jika key ditemukan
         if k == key:
            bucket[i] = (key, value) #update value lama
            return
         
      #jika key belum ada
      bucket.append((key, value))

   def get(self, key):
      '''Mengembalikan vakue berdasarkan key'''
      #cari indeks bucket
      index = self.hash_function(key)

      #ambil bucket
      bucket = self.table[index]

      #cari key di bucket
      for k, v in bucket:
         if k == key:
            return v
      return None

   def delete(self, key):
      '''Menghapus data berdasarkan key'''
      index = self.hash_function(key)
      bucket = self.table[index]

      for i, (k, v) in enumerate(bucket):
         if k == key:
            del bucket[i]
            return True
      return False

   def display(self):
      print('\n===== ISI HASH TABLE =====')

      for i, bucket in enumerate(self.table):
         print(f'Indeks {i}: {bucket}')


#----------------------------------------------------------------
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
      print('\n===== ISI TREE =====')
      for letter in (self.root.children):
         node = self.root.children[letter].words
         print(f'{letter} -> {node}')


#----------------------------------------------------------------
class Graph:
   '''Digunakan untuk pemetaan relasi antar kata untuk saran bantuan'''
   def __init__(self):
      self.graph = {}

   def add_vertex(self, word):
      '''Menambahkan node/kata'''
      if word not in self.graph:
         self.graph[word] = []

   def add_edge(self, from_word, to_word):
      '''Menambah hubungan antar kata'''
      self.add_vertex(from_word)
      self.add_vertex(to_word)

      self.graph[from_word].append(to_word)

   def get_neighbors(self, word):
      '''Mengambil tetangga'''
      return self.graph.get(word, [])
   
   def display(self):
      '''menampilkan graph'''
      for word in self.graph:
         print(f'{word} -> {self.graph[word]}')


#_________________________________________________

#word_tree = WordTree()
#for words in animal_words:
#   word_tree.insert(words)
#word_tree.display()

#graph = Graph()
#graph.add_edge("KUCING", "GAJAH")
#graph.add_edge("GAJAH", "HARIMAU")
#graph.add_edge("HARIMAU", "ULAR")
#graph.get_neighbors("GAJAH")
#graph.display()

#tree = WordTree()
#tree.insert("ULAR")
#tree.insert("UDANG")
#tree.insert("UNTA")
#tree.insert("HARIMAU")
#tree.insert("HIU")
#tree.display()
#h = tree.get_words_by_letter('h')
#print(f'H: {h}')

#TES
#ht = HashTable()
#ht.insert("andi", 20)
#ht.insert("budi", 25)
#ht.insert("cici", 30)
#ht.display()
#ht.insert("dani", 35)
#ht.display()
#print("Umur andi:", ht.get("andi"))
#print("Umur budi:", ht.get("budi"))
#ht.insert("budi", 21)
#ht.display()
#ht.delete("budi")
#ht.display()
#print("Umur joko:", ht.get("joko"))

#c =  CircularLinkedList()
#c.append('Rea')
#c.append('Cia')
#c.display()
#print(f'Next turn: {c.next_turn()}')
#print("Giliran:", c.get_current())
#print(f'Next turn: {c.next_turn()}')

#dll = DoubleLinkedList()
#dll.append('10')
#dll.append('20')
#dll.append('30')
#dll.prepend('5')
#print("Forward:")
#dll.display_forward()
#print("Backward:")
#dll.display_backward()
#dll.delete('20')
#print("Setelah hapus 20:")
#dll.display_forward()

#t = SingleLinkedList()
#t.insert('ULAR')
#t.insert('RUSA')
#t.insert('ayam')
#t.insert('MINOTOUR')
#t.insert('rakun')
#t.insert('NOT')
#t.traversal()
#print()
#t.delete('ular')
#t.traversal()
#print()
#t.insert('rakun')
#t.delete('kopi')
#t.traversal()
#t.delete('sapi')


#s = Queque()
#print(s.size())
#print(s.is_empty())
#s.enqueue(2)
#s.enqueue(7)
#s.enqueue(4)
#s.enqueue(10)
#s.display()
#print(s.peek())
#print(s.size())
#print(s.dequeue())
#s.display()
#print(s.size())
#print(s.peek())