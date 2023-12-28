"""
Loop memproses menu utama program.
"""

while True:

    # Cetak tampilan menu utama program
    print("Selamat Datang di Toko Buku Place Anak Chill!")
    print("=============================================")
    print("1. Pinjam buku")
    print("2. Keluar")
    pilih_aksi = input("Pilih aksi yang ingin dilakukan: ")

    # Validasi pilihan aksi
    if pilih_aksi != "1" and pilih_aksi != "2":
        print("Perintah tidak diketahui!")
        continue  # Kembali ke menu utama

    # Fitur 1: Pinjam buku
    if pilih_aksi == "1":
        nama = input("Masukkan nama anda: ")
        saldo = int(input("Masukkan saldo anda (Rp): "))
        status_member = input("Apakah anda member? [Y/N]: ")
        
        # Jika pengguna adalah member
        if status_member.lower() == "y":
            # Member akan diminta menginput ID maksimal 3 kali
            for trial in range(3):
                id_member = input("Masukkan ID anda: ")
                
                # Konversi input ID menjadi integer
                nomor_id = []
                for id_digit in id_member:
                    nomor_id.append(int(id_digit))
                
                # Memeriksa apakah jumlah digit ID = 23
                if sum(nomor_id) == 23:
                    print("Login member berhasil!")
                    print()
                    break
                else:
                    print("ID anda salah!")
                    continue

            # Kembali ke menu utama setelah 3 kali percobaan        
            else:
                print("Anda telah melebihi batas percobaan!")
                print("Program akan kembali ke menu utama.")
                print()
                continue 

        # Jika pengguna non-member    
        elif status_member.lower() == "n":
            print("Login non-member berhasil!")
            print()

        # Jika input bukan Y/N (tidak valid)
        else:
            print("Input tidak valid!")
            print()
            continue

        """
        Loop memproses transaksi peminjaman buku.
        """
        while True:

            # Cetak katalog komik dan opsi keluar
            print("=============================================")
            print("Katalog Buku Place Anak Chill")
            print("=============================================")
            print("X-Man (Rp 7.000/hari)")
            print("Doraemoh (Rp 5.500/hari)")
            print("Nartoh (Rp 4.000/hari)")
            print("=============================================")
            print("Keluar")
            print("=============================================")
            print()
            komik = input("Komik yang dipilih (atau 'keluar' untuk kembali ke menu utama): ")
            
            # Kembali ke menu utama jika memilih keluar
            if komik.lower() == "keluar":
                print()
                break

            # Validasi pilihan komik penguna
            elif komik.lower() not in ["x-man", "doraemoh", "nartoh"]:
                print("Komik tidak ditemukan!")
                print("Masukkan judul komik sesuai katalog.")
                print()
                # Kembali meminta input komik
                continue

            # Program menjalankan peminjaman komik
            else:
                # Meminta informasi durasi peminjaman komik
                durasi = int(input("Ingin melakukan peminjaman untuk berapa hari?: "))
                print()
                
                # Menghitung biaya peminjaman 
                biaya_pinjam = 0

                if komik.lower() == "x-man":
                    biaya_pinjam = 7000 * durasi
                elif komik.lower() == "doraemoh":
                    biaya_pinjam = 5500 * durasi
                elif komik.lower() == "nartoh":
                    biaya_pinjam = 4000 * durasi

                # Potongan diskon 20% bagi member 
                if status_member.lower() == "y":
                    biaya_pinjam *= 0.8
                
                # Memastikan saldo pengguna cukup untuk peminjaman
                if saldo >= biaya_pinjam:
                    saldo -= biaya_pinjam
                    print(f"Berhasil meminjam komik {komik} "
                        f"selama {durasi} hari!")
                    print(f"Saldo anda sisa Rp{saldo}")
                    print()
                    
                elif saldo < biaya_pinjam:
                    selisih_saldo = biaya_pinjam - saldo
                    print(f"Tidak Berhasil meminjam komik {komik}!")
                    print(f"Saldo anda kurang Rp{selisih_saldo}")
                    print()
    
    # Fitur 2: Keluar sepenuhnya dari program
    elif pilih_aksi == "2":
        print("Terima kasih telah mengunjungi Toko Buku Place "
              "Anak Chill!")
        break

    # Pilihan aksi tidak valid
    else:
        print("Perintah tidak diketahui!")
        print()
        continue
