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
        student_data[(name.strip(), npm.strip(), task.strip())] = content

    return student_data


def check_the_similarity(task_one, task_two):
    keywords_one = set(task_one.split())
    keywords_two = set(task_two.split())

    common_keywords = len(keywords_one & keywords_two)
    unique_keywords = len(keywords_one | keywords_two)

    similarity_percentage = (common_keywords / unique_keywords) * 100

    return similarity_percentage

def main():
    data = scan_the_tasks("Lab6.txt")

    print("Selamat datang di program Plagiarism Checker!")
    
    while True:
        print("=====================================================================")
        coursename = input("Masukkan nama mata kuliah yang ingin diperiksa: ")
        if coursename == "EXIT":
            print("Terima kasih telah menggunakan program Plagiarism Checker!")
            print()
            break
        elif coursename not in ["DDP-1", "Kalkulus", "Matdis-1"]:
            print(f"{coursename} tidak ditemukan.")
            print()
            continue

        for key, content in data.items():
            name, npm, course = key

            if course == coursename:
                student1_input = input("Masukkan nama/NPM mahasiswa pertama: ").strip()
                if student1_input in (name, npm):
                    task1 = content
                    student1 = name
                else:
                    print(f"Informasi mahasiswa {student1_input} tidak ditemukan.")
                    print()

                student2_input = input("Masukkan nama/NPM mahasiswa kedua: ").strip()
                if student2_input in (name, npm):
                    task2 = content
                    student2 = name
                else:
                    print(f"Informasi mahasiswa {student2_input} tidak ditemukan.")
                    print()

        plagiarism_percentage = check_the_similarity(task1, task2)

        print("============================= Hasil =================================")
        print(f"Tingkat kemiripan tugas {coursename} {student1} dan {student2} adalah {plagiarism_percentage:.2f}%.")
        
        if plagiarism_percentage < 31:
            print(f"{student1} dan {student2} tidak terindikasi plagiarisme.")
        elif 31 <= plagiarism_percentage <= 70:
            print(f"{student1} dan {student2} terindikasi plagiarisme ringan.")
        else:
            print(f"{student1} dan {student2} terindikasi plagiarisme.")
        
        print()
        print("=====================================================================")

if __name__ == "__main__":
    main()
