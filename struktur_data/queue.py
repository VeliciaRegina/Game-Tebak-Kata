class Queue:
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