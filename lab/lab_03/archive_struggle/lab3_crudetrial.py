running = True

while running:
    print("Selamat datang! Masukkan nama file yang berisi daftar makanan yang kamu miliki.")
    input_file = input("Masukkan nama file input daftar makanan: ")
    output_file = input("Masukkan nama file output: ")

    try:
        with open(input_file, 'r') as file:
            file_content = file.readlines()

        first_food = ""
        second_food = ""

        # Initialize a set to keep track of unique food items
        unique_food = set()

        for line in file_content:
            line = line.strip().lower()

            if line.startswith("daftar makanan 1:"):
                first_food = line.split(":")[1].strip()
            elif line.startswith("daftar makanan 2:"):
                second_food = line.split(":")[1].strip()

            word = line.split(":")
            if len(word) > 1:
                foods = word[1].split(",")

                for food in foods:
                    food = food.strip()
                    if food:
                        unique_food.add(food)

        with open(output_file, "w") as output:
            # Convert the set of unique food items back to a comma-separated string
            unique_food_str = ",".join(unique_food)
            output.write(unique_food_str)

        print()
        print("""Apa yang ingin kamu lakukan?
        ================================================
        1. Tampilkan daftar makanan pertama
        2. Tampilkan daftar makanan kedua
        3. Tampilkan gabungan makanan dari dua daftar
        4. Tampilkan makanan yang sama dari dua daftar
        5. Keluar
        ================================================
        """)
        pilih_aksi = input("Masukkan aksi yang ingin dilakukan: ")

        if pilih_aksi == "1":
            print()
            print("Daftar makanan pertama:")
            print(first_food)

        elif pilih_aksi == "2":
            print()
            print("Daftar makanan kedua:")
            print(second_food)

        elif pilih_aksi == "3":
            print()
            print("Gabungan makanan favorit dari kedua daftar:")
            combined = first_food + "," + second_food
            unique_combined = ",".join(set(combined.split(",")))
            print(unique_combined)

        elif pilih_aksi == "4":
            print()
            print("Makanan yang sama dari kedua daftar:")
            common_food = set(first_food.split(",")).intersection(second_food.split(","))
            print(",".join(common_food))

        elif pilih_aksi == "5":
            running = False

    except FileNotFoundError:
        print()
        print("Maaf, file input tidak ada. Masukkan ulang nama file yang valid.")
        print()
