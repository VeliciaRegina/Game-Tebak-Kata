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
      '''Mengembalikan value berdasarkan key'''
      #cari indeks bucket
      index = self.hash_function(key)

      #ambil bucket
      bucket = self.table[index]

      #cari key di bucket
      for k, v in bucket:
         if k == key:
            return v
      return None
   
   def get_all_data(self):
      '''Mengambil semua data dari hash table'''
      all_data = []

      for bucket in self.table:
         for key, value in bucket:
            all_data.append(key)
      return all_data

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


#import random
#ht = HashTable()
#ht.insert("kucing", True)
#ht.insert("kuda", True)
#ht.insert("ayam", True)
#ht.display()
#ht.insert("cacing", True)
#ht.display()
#all_data = ht.get_all_data()
#print(all_data)
#print('data random: ', random.choice(all_data))
#print("Umur andi:", ht.get("andi"))
#print("Umur budi:", ht.get("budi"))
#ht.insert("budi", 21)
#ht.display()
#ht.delete("budi")
#ht.display()
#print("Umur joko:", ht.get("joko"))