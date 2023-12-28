def hitung_kemiripan(doc1, doc2):
    kata_kunci1 = set(doc1.split())
    kata_kunci2 = set(doc2.split())
    
    kata_kunci_umum = kata_kunci1 & kata_kunci2
    kata_kunci_unik = kata_kunci1 | kata_kunci2
    
    if not kata_kunci_unik:
        return 0.0
    kemiripan = (len(kata_kunci_umum) / len(kata_kunci_unik)) * 100
    return round(kemiripan, 2)

def periksa_plagiat(mata_kuliah, mahasiswa, data_mata_kuliah, data_mahasiswa):
    if mahasiswa[0] not in data_mahasiswa.values() and mahasiswa[0] not in data_mahasiswa:
        print("Informasi mahasiswa tidak ditemukan.")
        return
    print(f"Masukkan nama/NPM mahasiswa kedua: {mahasiswa[1]}")
    if mahasiswa[1] not in data_mahasiswa.values() and mahasiswa[1] not in data_mahasiswa:
        print("Informasi mahasiswa tidak ditemukan.")
        return
    
    dokumen1 = data_mata_kuliah[mata_kuliah].get(mahasiswa[0], "")
    dokumen2 = data_mata_kuliah[mata_kuliah].get(mahasiswa[1], "")
    
    if not dokumen1 or not dokumen2:
        print("Informasi tugas tidak ditemukan.")
        return
    
    kemiripan = hitung_kemiripan(dokumen1, dokumen2)
    
    print("=" * 70)
    print(f"Tingkat kemiripan tugas {mata_kuliah} {mahasiswa[0]} dan {mahasiswa[1]} adalah {kemiripan:.2f}%.")
    
    if kemiripan < 31:
        print(f"{mahasiswa[0]} dan {mahasiswa[1]} tidak terindikasi plagiarisme.")
    elif 31 <= kemiripan <= 70:
        print(f"{mahasiswa[0]} dan {mahasiswa[1]} terindikasi plagiarisme ringan.")
    else:
        print(f"{mahasiswa[0]} dan {mahasiswa[1]} terindikasi plagiarisme.")

data_mata_kuliah = {}
data_mahasiswa = {}

nama_saat_ini, npm_saat_ini, mata_kuliah_saat_ini, konten_saat_ini = None, None, None, ""

with open("lab6.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        if nama_saat_ini == None and line != "":
            bagian = line.split(";")
            if len(bagian) == 3:
                nama_saat_ini, npm_saat_ini, mata_kuliah_saat_ini = bagian[0], bagian[1], bagian[2]
                konten_saat_ini = ""
        elif not line.startswith("="):
            konten_saat_ini += line + " "
            if nama_saat_ini and npm_saat_ini and mata_kuliah_saat_ini and konten_saat_ini:
                data_mata_kuliah[mata_kuliah_saat_ini] = data_mata_kuliah.get(mata_kuliah_saat_ini, {})
                data_mata_kuliah[mata_kuliah_saat_ini][nama_saat_ini] = konten_saat_ini
                data_mahasiswa[npm_saat_ini] = nama_saat_ini
            nama_saat_ini, npm_saat_ini, mata_kuliah_saat_ini, konten_saat_ini = None, None, None, ""

print("Selamat datang di program Plagiarism Checker!")

while True:
    print("=" * 70)
    mata_kuliah = input("Masukkan nama mata kuliah yang ingin diperiksa: ")
    if mata_kuliah == "EXIT":
        print("Terima kasih telah menggunakan program Plagiarism Checker!")
        break
    elif mata_kuliah not in data_mata_kuliah:
        print(f"{mata_kuliah} tidak ditemukan.")
        continue

    mahasiswa = []
    mahasiswa.append(input("Masukkan nama/NPM mahasiswa pertama: "))
    mahasiswa.append(input("Masukkan nama/NPM mahasiswa kedua: "))

    periksa_plagiat(mata_kuliah, mahasiswa, data_mata_kuliah, data_mahasiswa)