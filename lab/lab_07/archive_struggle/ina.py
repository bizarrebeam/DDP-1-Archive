# Fungsi untuk menambahkan relasi antara parent dan child dalam pohon keluarga
def add_relation(tree, parent, child):
    if parent not in tree:
        tree[parent] = []  # Jika parent belum ada dalam pohon, tambahkan dengan daftar kosong
    tree[parent].append(child)  # Tambahkan child ke daftar keturunan parent

# Fungsi untuk mengecek apakah child adalah keturunan dari parent dalam pohon keluarga
def is_descendant(tree, parent, child):
    if parent not in tree:
        return False  # Jika parent tidak ada dalam pohon, return False
    if child in tree[parent]:
        return True  # Jika child langsung adalah keturunan dari parent, return True
    for descendant in tree[parent]:
        if is_descendant(tree, descendant, child):
            return True  # Jika child adalah keturunan turunan dari parent, return True
    return False  # Jika tidak ditemukan, return False

# Fungsi untuk mencetak semua keturunan dari seorang parent dalam pohon keluarga
def print_descendants(tree, parent, prefix=""):
    if parent in tree:
        print('-', end = " ")
        for child in tree[parent]:
            print(child, end=" ")  # Cetak child dengan prefix (indentasi)
        print()
        for child in tree[parent]:
            print_descendants(tree, child, prefix)  # Rekursif untuk mencetak keturunan child

# Fungsi untuk menghitung jarak generasi antara parent dan child dalam pohon keluarga
def generation_distance(tree, parent, child, distance=0):
    if parent == child:
        return distance  # Jika parent dan child sama, return jarak yang sudah dihitung
    if parent not in tree:
        return -1  # Jika parent tidak ada dalam pohon, return -1 (tidak ada hubungan)
    for descendant in tree[parent]:
        result = generation_distance(tree, descendant, child, distance + 1)
        if result != -1:
            return result  # Jika ditemukan hubungan, return jarak yang sudah dihitung
    return -1  # Jika tidak ditemukan, return -1

# Fungsi utama
def main():
    family_tree = {}  # Inisialisasi pohon keluarga sebagai kamus kosong

    print("Masukkan data relasi:")
    input_data = input().split()
    while input_data[0] != "SELESAI":
        add_relation(family_tree, input_data[0], input_data[1])  # Tambahkan relasi ke pohon keluarga
        input_data = input().split()

    while True:
        print("\n=====================================================================")
        print("Selamat Datang di Relation Finder! Pilihan yang tersedia:")
        print("1. CEK_KETURUNAN\n2. CETAK_KETURUNAN\n3. JARAK_GENERASI\n4. EXIT")
        choice = int(input("Masukkan pilihan: "))

        if choice == 1:
            parent = input("Masukkan nama parent: ")
            child = input("Masukkan nama child: ")
            if is_descendant(family_tree, parent, child):
                print(f"{child} benar merupakan keturunan dari {parent}")
            else:
                print(f"{child} bukan merupakan keturunan dari {parent}")

        elif choice == 2:
            parent = input("Masukkan nama parent: ")
            print_descendants(family_tree, parent, prefix="")

        elif choice == 3:
            parent = input("Masukkan nama parent: ")
            child = input("Masukkan nama child: ")
            distance = generation_distance(family_tree, parent, child)
            if distance != -1:
                print(f"{parent} memiliki hubungan dengan {child} sejauh {distance}")
            else:
                print(f"Tidak ada hubungan antara {parent} dengan {child}")

        elif choice == 4:
            print("=====================================================================")
            print("Terima kasih telah menggunakan Relation Finder!")
            break

        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")


if __name__ == "__main__":
    main()