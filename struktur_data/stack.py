class Stack:
   '''Digunakan untuk membatalkan kata terakhir yang diinput (undo)'''
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

