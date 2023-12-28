import math

# deklarasi harga
harga_per_luas = 0.4

# meminta input pengguna
panjang_persegi = float(input("Masukkan panjang sisi persegi: "))
panjang_trapesium = float(input("Masukkan panjang sisi trapesium: "))
jumlah_nametag = int(input("Banyak name tag yang ingin dibuat: "))

# perhitungan luas
hitung_lingkaran = 0.5 * 0.25 * math.pi * pow(panjang_persegi, 2)
hitung_persegi = pow(panjang_persegi, 2)
hitung_segitiga = pow(panjang_persegi, 2) * 0.5
hitung_trapesium = (panjang_persegi + panjang_trapesium) * panjang_persegi * 0.5
hitung_total = hitung_trapesium + hitung_persegi + hitung_segitiga + hitung_lingkaran

hitung_per_nametag = round(hitung_total, 2) * jumlah_nametag
harga_per_nametag = round(hitung_per_nametag * harga_per_luas)

if jumlah_nametag == 1:
    print(f"""Luas satu name tag adalah {hitung_per_nametag}
    Harga yang perlu dibayar sebesar {harga_per_nametag * jumlah_nametag}
    """)
else:
    print(f"""Luas satu name tag adalah {hitung_per_nametag}
    Luas total name tag adalah {harga_per_nametag}
    Harga yang perlu dibayar sebesar {harga_per_nametag}
    """)
