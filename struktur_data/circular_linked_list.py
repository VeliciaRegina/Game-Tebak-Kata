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
      '''Menampilkan giliran player'''
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
         temp = temp.next
      
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


# c =  CircularLinkedList()
# c.append('Rea')
# c.append('Cia')
# c.display()
# print(f'Next turn: {c.next_turn()}')
# print("Giliran:", c.get_current())
# print(f'Next turn: {c.next_turn()}')