#Collab with Adelya Amanda dan Ananda Dwi Hanifa

# Memanggil turtle
import turtle

# Memanggil messagebox
from tkinter import messagebox

# Input jumlah tower yang akan dibangun
while True:
    jumlah_tower = turtle.numinput("Tower to Build", "Enter the number of towers you want to build (integer): ")

    # Validasi input
    if jumlah_tower is None:
        messagebox.showinfo("Peringatan!", "Masukkan angka yang benar! (Min: 1)")
        continue

    jumlah_tower = int(jumlah_tower)

    if jumlah_tower < 1:
        messagebox.showinfo("Peringatan!", "Masukkan angka yang benar! (Min: 1)")
        continue

    break

# Input jarak antar tower dan perbedaan jumlah lapisan antar tower jika tower>1
if jumlah_tower > 1:
    while True:
        jarak_antar_tower = turtle.numinput("Distance between Towers", "Enter the distance between towers you want to build (integer): ")


        if jarak_antar_tower is None:
            messagebox.showinfo("Peringatan!", "Masukkan angka yang benar! (Min: 2, Max: 5)")
            continue

        jarak_antar_tower = int(jarak_antar_tower)

        if jarak_antar_tower < 2 or jarak_antar_tower > 5:
            messagebox.showinfo("Peringatan!", "Masukkan angka yang benar! (Min: 2, Max: 5)")
            continue

        break

    while True:
        perbedaan_jumlah_lapisan_tower = turtle.numinput("Tower Layer Difference", "Enter the number of layer differences between each tower (integer): ")

        if perbedaan_jumlah_lapisan_tower is None:
            messagebox.showinfo("Peringatan!", "Masukkan angka yang benar! (Min: 2, Max: 5)")
            continue

        perbedaan_jumlah_lapisan_tower = int(perbedaan_jumlah_lapisan_tower)

        if perbedaan_jumlah_lapisan_tower < 2 or perbedaan_jumlah_lapisan_tower > 5:
            messagebox.showinfo("Peringatan!", "Masukkan angka yang benar! (Min: 2, Max: 5)")
            continue

        break

# Input lebar satu batu bata
while True:
    lebar_batu_bata = turtle.numinput("Brick Width", "Enter the width of a brick (integer): ")


    # Validasi input
    if lebar_batu_bata is None:
        messagebox.showinfo("Peringatan!", "Masukkan angka yang benar! (Min: 1, Max: 35)")
        continue

    lebar_batu_bata = int(lebar_batu_bata)

    if lebar_batu_bata < 1 or lebar_batu_bata > 35:
        messagebox.showinfo("Peringatan!", "Masukkan angka yang benar! (Min: 1, Max: 35)")
        continue

    break

# Input tinggi satu batu bata
while True:
    tinggi_batu_bata = turtle.numinput("Brick Height", "Enter the height of a brick (integer): ")

    # Validasi input
    if tinggi_batu_bata is None:
        messagebox.showinfo("Peringatan!", "Masukkan angka yang benar! (Min: 1, Max: 25)")

    tinggi_batu_bata = int(tinggi_batu_bata)

    if tinggi_batu_bata < 1 or tinggi_batu_bata > 25:
        messagebox.showinfo("Peringatan!", "Masukkan angka yang benar! (Min: 1, Max: 25)")
        continue

    break

# Input panjang lapisan di badan tower pertama
while True:
    panjang_lapisan_badan_tower_pertama = turtle.numinput("The Number of First Tower Layers", "Enter the number of layers for the first tower (integer): ")

    # Validasi input
    if panjang_lapisan_badan_tower_pertama is None:
        messagebox.showinfo("Peringatan!", "Masukkan angka yang benar! (Min: 1, Max: 25)")
        continue

    panjang_lapisan_badan_tower_pertama = int(panjang_lapisan_badan_tower_pertama)

    if panjang_lapisan_badan_tower_pertama < 1 or panjang_lapisan_badan_tower_pertama > 25:
        messagebox.showinfo("Peringatan!", "Masukkan angka yang benar! (Min: 1, Max: 25")
        continue

    break

# Input lebar badan tower
while True:
    lebar_badan_tower = turtle.numinput("Layer Width", "Enter the width of the layer (integer): ")

    # Validasi input
    if lebar_badan_tower is None:
        messagebox.showinfo("Peringatan!", "Masukkan angka yang benar! (Min: 1, Max: 10)")
        continue

    lebar_badan_tower = int(lebar_badan_tower)

    if lebar_badan_tower < 1 or lebar_badan_tower > 10:
        messagebox.showinfo("Peringatan!", "Masukkan angka yang benar! (Min: 1, Max: 10)")
        continue

    break

# Koordinat awal agar muncul ditengah
perhitungan_awal = jumlah_tower * (lebar_badan_tower + jarak_antar_tower) + (1.5 * lebar_badan_tower)
x = -200
y = -200

t = turtle.Turtle()  # Buat objek turtle baru di luar loop
t.speed(0)  # Atur kecepatan gambar menjadi tercepat

batu_bata = 0

# Loop Jumlah Tower
for k in range(jumlah_tower):
    # Loop Panjang Tower
    for j in range(panjang_lapisan_badan_tower_pertama):
        # Loop lebar tower
        for i in range(lebar_badan_tower):
            t.penup()
            t.goto(x, y)
            t.pendown()
            t.pencolor("black")
            t.fillcolor("#CA7F65")
            t.begin_fill()
            t.right(90)
            t.forward(tinggi_batu_bata)
            t.right(90)
            t.forward(lebar_batu_bata)
            t.right(90)
            t.forward(tinggi_batu_bata)
            t.right(90)
            t.forward(lebar_batu_bata)
            t.end_fill()

            x += lebar_batu_bata
            t.penup()
            batu_bata += 1

        y += tinggi_batu_bata
        x -= lebar_batu_bata * lebar_badan_tower

    # Loop kepala tower
    for m in range(lebar_badan_tower + 1):
        x_kepala = x - (lebar_batu_bata // 2)
        y_kepala = y
        t.penup()
        t.goto(x_kepala, y_kepala)
        t.pendown()
        t.pencolor("black")
        t.fillcolor("#693424")
        t.begin_fill()
        t.right(90)
        t.forward(tinggi_batu_bata)
        t.right(90)
        t.forward(lebar_batu_bata)
        t.right(90)
        t.forward(tinggi_batu_bata)
        t.right(90)
        t.forward(lebar_batu_bata)
        t.end_fill()
        x += lebar_batu_bata
        t.penup()
        batu_bata += 1
    
    panjang_lapisan_badan_tower_pertama += perbedaan_jumlah_lapisan_tower

    y = -200
    x += jarak_antar_tower * lebar_batu_bata


turtle.hideturtle()  # Sembunyikan kursor turtle
turtle.exitonclick() # Jendela/grafik turtle agar tidak langsung menutup

# Setelah loop selesai, atur posisi x dan y untuk teks
x = -250
y = -300

# Buat pesan untuk ditampilkan
pesan_mario = f"{int(jumlah_tower)} Super Mario Towers have been built with a total of {batu_bata} bricks"

# Pindahkan turtle ke posisi untuk menulis teks
t.penup()
t.goto(-250, -300)

# Tampilkan teks
t.write(pesan_mario, align="center", font=("Times New Roman", 15, "bold"))

# Jendela turtle tidak akan menutup sampai Anda mengklik mouse
t.done()