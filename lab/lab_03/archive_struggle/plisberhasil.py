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
        
        # The inner loop user's actions for files 
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
            user_action = input("Masukkan aksi yang ingin dilakukan: ")
            
            output = open(output_file, 'a')

            # If user want to display the first food list
            if user_action == "1":
                print()
                print("Daftar makanan pertama:")
                print(first_food)

                # Write the first food list to the output file
                output.write("Daftar makanan pertama:\n")
                output.write(first_food + "\n\n" )

            # If user want to display the second food list
            elif user_action == "2":
                print()
                print("Daftar makanan kedua:")
                print(second_food)

                # Write the second food list to the output file
                output.write("Daftar makanan kedua:\n")
                output.write(second_food + "\n\n")

            # If user want to display the combined food lists
            elif user_action == "3":
                # Set the initial variables needed
                combined = first_food + "," + second_food + ","
                current_word = ""
                unique_combined = ""
                
                # Add only the unique food from both lists
                for char in combined:
                    if char == ',':
                        current_word = current_word.strip()
                        if current_word not in unique_combined:
                                unique_combined += current_word + ","
                        current_word = ""
                    else:
                        current_word += char
                unique_combined = unique_combined.rstrip(",")

                print()
                print("Gabungan makanan favorit dari kedua daftar:")
                print(unique_combined)

                # Write the combined food list to the output file
                output.write("Gabungan makanan favorit dari kedua daftar:\n")
                output.write(unique_combined + "\n\n")

            # If user want to display the identical food list
            elif user_action == "4":
                # Set the initial variables needed
                identical_food = ""
                current_word = ""

                # Find identical food items between the first and second food lists
                for char in first_food:
                    if char == ',':
                        current_word = current_word.strip()

                        if current_word in second_food.strip() and current_word not in identical_food:
                            identical_food += current_word + ","
                        current_word = ""
                    else:
                        current_word += char
                identical_food = identical_food.rstrip(",")

                # Display and writing identical food items to the output file
                if identical_food:
                    print()
                    print("Makanan yang sama dari kedua daftar:")
                    print(identical_food)
                    output.write("Makanan yang sama dari dua daftar:\n")
                    output.write(identical_food + "\n\n")
                
                # Display if there's no identical food between the lists
                else:
                    print()
                    print("Tidak ada makanan yang sama dari kedua daftar.")
                    output.write("Tidak ada makanan yang sama dari kedua daftar.\n")
        
            # If user want to exit from the program
            elif user_action == "5":
                print("Terima kasih telah menggunakan program ini!")
                print(f"Semua keluaran telah disimpan pada file {output_file}")

                # Exit both the inner and the outer loop
                find_food = False
                running = False
     
    except FileNotFoundError:
        print()
        print("Maaf, file input tidak ada. Masukkan ulang nama file yang valid.")
        input_file = ""  
        output_file = ""  
        print()

