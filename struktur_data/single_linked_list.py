class NodeSingle:
   def __init__(self, data):
      self.data = data.upper()
      self.next = None

class SingleLinkedList:
   '''Digunakan untuk menyimpan scrore pemain.'''
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

   def append (self, data):
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