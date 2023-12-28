def scan_the_tasks(filename):
    student_data = {}

    with open(filename, "r") as file:
        lines = file.read().splitlines()
    
    index = 0

    while index < len(lines):
        name, npm, task = lines[index].split(';')
        index += 2
        content = lines[index]
        index += 2
        student_data[(name, npm, task)] = content

    return student_data


def check_the_similarity(task_one, task_two):
    keywords_one = set(task_one.split())
    keywords_two = set(task_two.split())

    common_keywords = len(keywords_one & keywords_two)
    unique_keywords = len(keywords_one | keywords_two)

    similarity_percentage = (common_keywords / unique_keywords) * 100

    return similarity_percentage

def main():
    print("Selamat datang di program Plagiarism Checker!")
    print("===============================================")

    student_data = scan_the_tasks("Lab6.txt")

    while True:
        task_course_name = input("Masukkan nama mata kuliah yang ingin diperiksa: ")

        if task_course_name == "EXIT":
            print("Terima kasih telah menggunakan program Plagiarism Checker")
            break

        matching_keys = [key for key in student_data if task_course_name in key[2]]

        if not matching_keys:
            print(f"Mata kuliah {task_course_name} tidak ditemukan.")
            continue  # Skip to the next iteration of the loop

        selected_key = matching_keys[0]  # Take the first match
        student_data_for_course = student_data[selected_key]

        student_one_input = input("Masukkan nama/NPM mahasiswa pertama: ")
        student_two_input = input("Masukkan nama/NPM mahasiswa kedua: ")

        student_one = None
        student_two = None

        for key in student_data:
            if student_one_input in (key[0], key[1]):
                student_one = key[0]
            if student_two_input in (key[0], key[1]):
                student_two = key[0]

        if student_one is None:
            for key in student_data_for_course:
                if student_one_input in (key[0], key[1]):
                    student_one = key[0]

        if student_two is None:
            for key in student_data_for_course:
                if student_two_input in (key[0], key[1]):
                    student_two = key[0]

        if student_one is None:
            print(f"Nama/NPM mahasiswa pertama ({student_one_input}) tidak ditemukan.")
            continue  # Skip to the next iteration of the loop

        if student_two is None:
            print(f"Nama/NPM mahasiswa kedua ({student_two_input}) tidak ditemukan.")
            continue  # Skip to the next iteration of the loop

        task_one = student_data_for_course[student_one]
        task_two = student_data_for_course[student_two]
        similarity_percentage = check_the_similarity(task_one, task_two)

        if similarity_percentage < 31:
            similarity_level = "Tidak terindikasi plagiarisme."
        elif similarity_percentage <= 70:
            similarity_level = "Terindikasi plagiarisme ringan."
        else:
            similarity_level = "Terindikasi plagiarisme."

        print("============================= Hasil =================================")
        print(f"Tingkat kemiripan tugas {selected_key[2]} {student_one} dan {student_two} adalah {similarity_percentage:.2f}%.")
        print(f"{student_one} dan {student_two} {similarity_level}")
        print("=====================================================================")

if __name__ == "__main__":
    main()






