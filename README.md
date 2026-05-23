Game bernama "Tebak Kata Berantai"
game sederhana di mana pemain harus menyambung kata (misal: ULAR -> RUSA -> AYAM).

Konsep game:
-multiplayer 2 pemain
-tema kata hewan/negara
-pemain harus menyambung huruf akhir
-ada skor
-ada hint (setiap pakai hint skor berkurang)
-ada undo
-ada nyawa (3 nyawa)

Algoritma game:

1. Main Menu
2. Input Player
3. Queue Lobby
4. Pilih Tema
5. Generate Kata Awal
6. Gameplay
   Validasi Kata:
   Benar -> lanjut
   Salah -> kurangi nyawa
   Simpan ke Linked List
   Update Stack
   Ganti Giliran
7. Game Over
8. Sorting Leaderboard
9. Save File
