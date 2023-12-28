# Set initial variables needed
running = True 
input_file = ""  
output_file = "" 

# Loop for the main program
while running:

    print()
    print("Selamat datang! Masukkan dua nama file yang berisi daftar makanan yang kamu miliki.")

    # Ask user to provide their files name
    if not input_file or not output_file:
        input_file = input("Masukkan nama file input daftar makanan: ")
        output_file = input("Masukkan nama file output: ")

    # Program try to read the provided file
    try:
        with open(input_file, 'r') as file:
            file_content = file.readlines()

        # Set initial variables needed
        first_food = ""
        second_food = ""
        unique_food = ""
        unique_combined = ""

        # Get the first and second food lists from the file
        for line in file_content:
            line = line.strip().lower()

            if line.startswith("daftar makanan 1:"):
                first_food = line[line.index(":") + 1:].strip()
            elif line.startswith("daftar makanan 2:"):
                second_food = line[line.index(":") + 1:].strip()

        # Open the output file for
        with open(output_file, "w") as output:

            combined = first_food + "," + second_food
            current_word = ""
            for char in combined:
                if char == ',':
                    current_word = current_word.strip()
                    if current_word:
                        if current_word not in unique_combined:
                            unique_combined += current_word + ","
                    current_word = ""
                else:
                    current_word += char

            unique_combined = unique_combined.rstrip(",")
            output.write(unique_combined)
        
        find_food = True
        while find_food:
            print()
            print("""Apa yang ingin kamu lakukan?
================================================
1. Tampilkan daftar makanan pertama
2. Tampilkan daftar makanan kedua
3. Tampilkan gabungan makanan dari dua daftar
4. Tampilkan makanan yang sama dari dua daftar
5. Keluar
================================================""")
            pilih_aksi = input("Masukkan aksi yang ingin dilakukan: ")

            if pilih_aksi == "1":
                print()
                print("Daftar makanan pertama:")
                print(first_food)

                with open(output_file, "w") as output:
                    output.write("Daftar makanan pertama:\n")
                    output.write(first_food + "\n")

            elif pilih_aksi == "2":
                print()
                print("Daftar makanan kedua:")
                print(second_food)

                with open(output_file, "a") as output:
                    output.write("Daftar makanan kedua:\n")
                    output.write(second_food + "\n")

            elif pilih_aksi == "3":
                print()
                print("Gabungan makanan favorit dari kedua daftar:")
                combined = first_food + "," + second_food + ","
                current_word = ""
                unique_combined = ""
                for char in combined:
                    if char == ',':
                        current_word = current_word.strip()
                        if current_word not in unique_combined:
                                unique_combined += current_word + ","
                        current_word = ""
                    else:
                        current_word += char

                unique_combined = unique_combined.rstrip(",")
                print(unique_combined)

                with open(output_file, "a") as output:
                    output.write("Gabungan makanan favorit dari kedua daftar:\n")
                    output.write(unique_combined + "\n")

            elif pilih_aksi == "4":
                identical_food = ""
                current_word = ""

                for char in first_food:
                    if char == ',':
                        current_word = current_word.strip()

                        if current_word in second_food.strip() and current_word not in identical_food:
                            identical_food += current_word + ","
                        current_word = ""
                    else:
                        current_word += char
                
                current_word = current_word.strip()

                if current_word in second_food.strip() and current_word not in identical_food:
                    identical_food += current_word + ","
                current_word = ""

                identical_food = identical_food.rstrip(",")

                if identical_food:
                    print()
                    print("Makanan yang sama dari kedua daftar:")
                    print(identical_food)
                    with open(output_file, "a") as output:
                        output.write("Makanan yang sama dari dua daftar:\n")
                        output.write(identical_food + "\n")

                else:
                    print()
                    print("Tidak ada makanan yang sama dari kedua daftar.")
                    with open(output_file, "a") as output:
                        output.write("Tidak ada makanan yang sama dari kedua daftar.\n")
            
            elif pilih_aksi == "5":
                print()
                print("Terima kasih telah menggunakan program ini!")
                print(f"Semua keluaran telah disimpan pada file {output_file}")
                find_food = False
                running = False
      
    except FileNotFoundError:
        print()
        print("Maaf, file input tidak ada. Masukkan ulang nama file yang valid.")
        input_file = ""  
        output_file = ""  
        print()
