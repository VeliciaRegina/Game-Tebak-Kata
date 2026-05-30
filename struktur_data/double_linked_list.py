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


