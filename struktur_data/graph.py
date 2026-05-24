class Graph:
   '''Digunakan untuk pemetaan relasi antar kata berdasarkan huruf terakhir'''
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

#graph = Graph()
#graph.add_edge("KUCING", "GAJAH")
#graph.add_edge("GAJAH", "HARIMAU")
#graph.add_edge("HARIMAU", "ULAR")
#graph.get_neighbors("GAJAH")
#graph.display()