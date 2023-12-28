# Kolaborator: Anindya Nabila Syifa 

# Function to extract data from the file
def read_student_data(filename):
    student_data = {}                                                               # Initialize the dictionary to store the data from the file

    with open(filename, "r") as file:
        lines = file.read().splitlines()                                            # Returns a list of strings

    get_index = 0                                                                   # Search the data needed based on index

    while get_index < len(lines):                               

        name, npm, task = lines[get_index].split(';')                               # Extract the students identity                   
        get_index += 2                                                              # Two separators: "==..." and blank line

        content = lines[get_index]
        get_index += 2                                                              # Two separators: "==..." and blank line

        key = (name.strip(), npm.strip(), task.strip())         

        if key not in student_data:                                                 # Each unique combination gets its own list of task contents
            student_data[key] = []
            
        student_data[key].append(content)

    return student_data

# Function to perform similarity check
def check_similarity(task_one, task_two):
    keywords_one = set(task_one.split())                                            # Set datatype helps to collect unique content
    keywords_two = set(task_two.split())

    common_keywords = len(keywords_one & keywords_two)                              # Intersection from both tasks content (shares similar)
    unique_keywords = len(keywords_one) + len(keywords_two)                         # Total of the unique content from both tasks

    similarity_percentage = (2 * common_keywords / unique_keywords) * 100           # Doubling for Task 1 <--> Task 2 comparation

    return similarity_percentage


# Function to process the main interface
def main():
    student_data = read_student_data("Lab6.txt")                                    # Call the previous function

    print(
        "Selamat datang di program Plagiarism Checker!"
        )

    while True:                                                                     # Main program loop
        print(
            "====================================================================="
            )
        
        coursename = input(
            "Masukkan nama mata kuliah yang ingin diperiksa: "
            )
        
        # Handle the coursename input validation
        if coursename == "EXIT":                                                    
            print(
                "Terima kasih telah menggunakan program Plagiarism Checker!"
                )
            break
        elif coursename not in [course for (_, _, course) in student_data.keys()]: # Coursename input is not exist in the existed dictionary
            print(
                f"{coursename} tidak ditemukan."
                )
            print()
            continue  

        student1_input = input(
            "Masukkan nama/NPM mahasiswa pertama: "
            ).strip()

        # Handle the student name input validation
        student1 = None                                                            # Initialize variable before looping the dictionary
        task1 = None

        for key, contents in student_data.items():
            name, npm, course = key

            if course == coursename and student1_input in (name, npm):             
                task1 = contents[0]                                                # Assign the student name value
                student1 = name
                break  

        if student1 is None:                                                       # Handle if the name is not exist in the dictionary
            print(f"Informasi mahasiswa tidak ditemukan.")
            print()
            continue  

        student2_input = input(
            "Masukkan nama/NPM mahasiswa kedua: "
            ).strip()
        
        student2 = None                                                            # Initialize variable before looping the dictionary
        task2 = None

        for key, contents in student_data.items():
            name, npm, course = key

            if course == coursename and student2_input in (name, npm):
                task2 = contents[0]                                                # Assign the student name value   
                student2 = name
                break  

        if student2 is None:                                                       # Handle if the name is not exist in the dictionary
            print(
                f"Informasi mahasiswa tidak ditemukan."
                )
            print()
            continue  
        
        # Display similarity checking results
        plagiarism_percentage = check_similarity(task1, task2)                     # Call the previous function

        print(
            "============================= Hasil ================================="
            )
        print(
            f"Tingkat kemiripan tugas {coursename} {student1} dan {student2} "\
                f"adalah {plagiarism_percentage:.2f}%."
            )

        if plagiarism_percentage < 31:
            print(
                f"{student1} dan {student2} tidak terindikasi plagiarisme."
                )
        elif 31 <= plagiarism_percentage <= 70:
            print(
                f"{student1} dan {student2} terindikasi plagiarisme ringan."
                )
        else:
            print(
                f"{student1} dan {student2} terindikasi plagiarisme."
                )

        print()

if __name__ == "__main__":
    main()
