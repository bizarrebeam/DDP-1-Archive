import math

diameter = int(input("Masukkan diameter lingkaran: "))

# Menghitung luas asli masing-masing bentuk
hitung_segiempat = pow(diameter, 2)
hitung_lingkaran = 0.25 * math.pi * pow(diameter, 2)
hitung_segitiga = 0.5 * diameter * (diameter * 0.5)

# Menghitung luas yang dicat
cat_merah = hitung_segiempat - hitung_lingkaran
cat_kuning = hitung_lingkaran - hitung_segitiga
cat_ungu = hitung_segitiga

# output
print(f"""Luas daerah cat merah: {round(cat_merah, 2)}
      Luas daerah cat kuning: {round(cat_kuning, 2)}
      Luas daerah cat ungu: {round(cat_ungu, 2)}""")
