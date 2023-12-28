""" 
Program menerjemahkan pesan dalam 
hexadecimal menuju karakter ASCII, dan 
dan menyusun password dari input dua integer
menuju binary. 
"""

#Pesan yang diterima dari Kelompok Zog
pesan_zog = input("Masukkan pesan yang dikirimkan "
                  "dari Kelompok Zog!:")

#Clue password yang diberikan Kelompok Zog
angka_pertama = int(input("Masukkan angka pertama!: "))
angka_kedua = int(input("Masukkan angka kedua!: "))

#Mengkonversi pesan dari hexadecimal menuju ASCII
bytes_zog = bytes.fromhex(pesan_zog)
ascii_zog = bytes_zog.decode("ASCII")

#Mengkonversi password berdasarkan clue yang diberikan
int_password = angka_pertama * angka_kedua * 13
bin_password = bin(int_password)

#Cetak hasil terjemahan pesan dan password
print(f"Hasil terjemahan pesan: {ascii_zog} ")
print(f"Password: {bin_password}")
print()
print(f'Pesan "{ascii_zog}" telah diterima dengan '
      f'password"{bin_password}".')


