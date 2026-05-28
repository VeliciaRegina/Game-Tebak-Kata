def read_words_from_file(theme):
   '''Membaca kata-kata dari file berdasarkan tema'''
   words = []
   filename = f'data/{theme}'
   with open (filename, 'r') as file:
      for line in file:
         word = line.strip().upper()
         if word:
            words.append(word)
   return words

def build_graph(graph, words):
   '''Membuat relasi kata berdasarkan huruf awal (kucinG -> Gajah)'''
   for word1 in words:
      for word2 in words:
         if word1 != word2:
            if word1[-1] == word2[0]:
               graph.add_edge(word1, word2)

def generate_hint(current_word, word_graph, used_word_hash):
   '''Menghasilkan maksimal 3 hint kata tetangga yang belum pernah digunakan'''
   neighbours = word_graph.get_neighbors(current_word)

   available_hints = [word for word in neighbours if not used_word_hash.get(word)]
   return available_hints[:3]