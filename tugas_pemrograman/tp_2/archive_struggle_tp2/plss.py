import sys
import os
import time

# Fungsi untuk melakukan parsing teks dan mengambil informasi yang diperlukan
def parse_text(text):
    try:
        # Mencari dan mengekstrak nilai dari atribut-atribut yang diperlukan dalam teks
        provinsi_start = text.find('provinsi="') + len('provinsi="')
        provinsi_end = text.find('"', provinsi_start)
        provinsi = text[provinsi_start:provinsi_end][:15].rjust(15)

        klasifikasi_start = text.find('klasifikasi="') + len('klasifikasi="')
        klasifikasi_end = text.find('"', klasifikasi_start)
        klasifikasi = text[klasifikasi_start:klasifikasi_end][:15].rjust(15)

        sub_klasifikasi_start = text.find('sub_klasifikasi="') + len('sub_klasifikasi="')
        sub_klasifikasi_end = text.find('"', sub_klasifikasi_start)
        sub_klasifikasi = text[sub_klasifikasi_start:sub_klasifikasi_end][:30].rjust(30)

        lembaga_peradilan_start = text.find('lembaga_peradilan="') + len('lembaga_peradilan="')
        lembaga_peradilan_end = text.find('"', lembaga_peradilan_start)
        lembaga_peradilan = text[lembaga_peradilan_start:lembaga_peradilan_end][:20].rjust(20)

        return provinsi, klasifikasi, sub_klasifikasi, lembaga_peradilan

    except Exception as e:
        # Handle jika terjadi kesalahan dalam parsing
        return None, None, None, None

# Fungsi untuk mencari dokumen dalam satu section tertentu
def search_section(section, keywords, operation=None, second_keywords=None):
    start_time = time.time()
    result_count = 0

    # Loop melalui semua file XML dalam folder dataset
    for filename in os.listdir("dataset"):
        if filename.endswith(".xml"):
            file_path = os.path.join("dataset", filename)

            with open(file_path, "r", encoding="utf-8") as file:
                document_text = file.read().lower().replace("\n", " ")  # Ubah ke huruf kecil untuk pencarian case-insensitive

                provinsi, klasifikasi, sub_klasifikasi, lembaga_peradilan = parse_text(document_text)

                # Cek apakah [section] adalah nama section tertentu, maka proses hanya section tersebut
                start_section = f"<{section}>"
                end_section = f"</{section}>"
                start_index = document_text.find(start_section)
                end_index = document_text.find(end_section)

                if start_index != -1 and end_index != -1:
                    section_text = document_text[start_index:end_index]
                    if operation is None:
                        # Pencarian kata kunci dalam teks section
                        if keywords.lower() in section_text:
                            result_count += 1
                            print(f"{filename} {provinsi} {klasifikasi} {sub_klasifikasi} {lembaga_peradilan}")

                    elif operation == "AND":
                        # Pencarian kata kunci pertama
                        if keywords.lower() in section_text:
                            # Pencarian kata kunci kedua
                            if second_keywords.lower() in section_text:
                                result_count += 1
                                print(f"{filename} {provinsi} {klasifikasi} {sub_klasifikasi} {lembaga_peradilan}")

                    elif operation == "OR":
                        # Pencarian kata kunci pertama atau kata kunci kedua
                        if keywords.lower() in section_text or (second_keywords and second_keywords.lower() in section_text):
                            result_count += 1
                            print(f"{filename} {provinsi} {klasifikasi} {sub_klasifikasi} {lembaga_peradilan}")

                    elif operation == "ANDNOT":
                        # Pencarian kata kunci pertama dan tidak kata kunci kedua
                        if keywords.lower() in section_text and (not second_keywords or second_keywords.lower() not in section_text):
                            result_count += 1
                            print(f"{filename} {provinsi} {klasifikasi} {sub_klasifikasi} {lembaga_peradilan}")

    end_time = time.time()
    total_time = end_time - start_time

    print(f"Banyaknya dokumen yang ditemukan = {result_count}")
    print(f"Total waktu pencarian = {total_time:.3f} detik")

# Fungsi untuk mencari dokumen dalam semua section
def search_all_sections(keywords, operation=None, second_keywords=None):
    start_time = time.time()
    result_count = 0

    # Loop melalui semua file XML dalam folder dataset
    for filename in os.listdir("dataset"):
        if filename.endswith(".xml"):
            file_path = os.path.join("dataset", filename)

            with open(file_path, "r", encoding="utf-8") as file:
                document_text = file.read().lower().replace("\n", " ")  # Ubah ke huruf kecil untuk pencarian case-insensitive

                provinsi, klasifikasi, sub_klasifikasi, lembaga_peradilan = parse_text(document_text)

                if operation is None:
                    # Pencarian kata kunci dalam teks dokumen
                    if keywords.lower() in document_text:
                        result_count += 1
                        print(f"{filename} {provinsi} {klasifikasi} {sub_klasifikasi} {lembaga_peradilan}")

                elif operation == "AND":
                    # Pencarian kata kunci pertama
                    if keywords.lower() in document_text:
                        # Pencarian kata kunci kedua
                        if second_keywords.lower() in document_text:
                            result_count += 1
                            print(f"{filename} {provinsi} {klasifikasi} {sub_klasifikasi} {lembaga_peradilan}")

                elif operation == "OR":
                    # Pencarian kata kunci pertama atau kata kunci kedua
                    if keywords.lower() in document_text or (second_keywords and second_keywords.lower() in document_text):
                        result_count += 1
                        print(f"{filename} {provinsi} {klasifikasi} {sub_klasifikasi} {lembaga_peradilan}")

                elif operation == "ANDNOT":
                    # Pencarian kata kunci pertama dan tidak kata kunci kedua
                    if keywords.lower() in document_text and (not second_keywords or second_keywords.lower() not in document_text):
                        result_count += 1
                        print(f"{filename} {provinsi} {klasifikasi} {sub_klasifikasi} {lembaga_peradilan}")

    end_time = time.time()
    total_time = end_time - start_time

    print(f"Banyaknya dokumen yang ditemukan = {result_count}")
    print(f"Total waktu pencarian = {total_time:.3f} detik")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Argumen program tidak benar.")
    else:
        section = sys.argv[1]
        keywords = sys.argv[2]  # Kata kunci pertama
        operation = None
        second_keywords = None

        if len(sys.argv) == 5:
            operation = sys.argv[3]
            second_keywords = sys.argv[4]  # Kata kunci kedua

            if operation not in ["AND", "OR", "ANDNOT"]:
                print("Operator harus berupa AND, OR, atau ANDNOT.")
                sys.exit(1)

        # Cek apakah kata kunci pertama diapit oleh tanda kutip ganda
        if keywords.startswith('"') and keywords.endswith('"'):
            keywords = keywords[1:-1]  # Hapus tanda kutip ganda

        # Cek apakah kata kunci kedua diapit oleh tanda kutip ganda
        if second_keywords and second_keywords.startswith('"') and second_keywords.endswith('"'):
            second_keywords = second_keywords[1:-1]  # Hapus tanda kutip ganda

        if section.lower() == "all":
            # Jika [section] adalah "all", maka proses semua section
            search_all_sections(keywords, operation, second_keywords)
        else:
            # Jika [section] adalah nama section tertentu, maka proses hanya section tersebut
            search_section(section, keywords, operation, second_keywords)
