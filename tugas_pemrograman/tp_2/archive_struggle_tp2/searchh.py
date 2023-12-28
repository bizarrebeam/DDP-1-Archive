import os
import sys
import time

display_information = lambda a, b, c, d, e: print(f"{a[:40]:>50s}{b:>15s}{c:>15s}{d:>30s}{e:>20}")
display_error_message = lambda: print("Operator harus berupa AND, OR atau ANDNOT.")
display_general_message = lambda: print("Argumen program tidak benar.")

def parse_the_files(xml_file):
    try:
        with open(xml_file, "r", encoding = "utf-8") as file:
            lines = file.readlines()
    
    except Exception:
        display_general_message()
        return []
    
def get_the_info(lines):
    info = {"provinsi": "", "klasifikasi": "", "sub_klasifikasi": "", "lembaga_peradilan": ""  }
    
    for line in lines:
        if line.strip().startswith("<putusan "):
            words = line.strip().split()
            for word in words:
                if word.startswith("provinsi="):
                    info["provinsi"] = word.split('"')[1]
                elif word.startswith('klasifikasi="'):
                    info["klasifikasi"] = word.split('"')[1]
                elif word.startswith('sub_klasifikasi="'):
                    info["sub_klasifikasi"] = word.split('"')[1]
                elif word.startswith('lembaga_peradilan="'):
                    info["lembaga_peradilan"] = word.split('"')[1]
    return info

def scan_the_files(lines, section, keywords, operator):
    in_section = False
    current_section = ""
    current_element = ""
    matched = []
    begin_time = time.time()

    for line in lines:
        if f"<{section}>" in line or section == "all":
            in_section = True
            current_section = line.strip()
            current_element = "" # blm handle all
            continue
        elif "</" in line:
            in_section = False
            current_section = ""
            current_element = ""
            continue

        if in_section:
            current_element += line.strip()

        if operator == "AND" and all(keyword in current_element for keyword in keywords):
            matched = (current_section, current_element)
            matched.append(matched)
        elif operator == "OR" and any(keyword in current_element for keyword in keywords):
            matched = (current_section, current_element)
            matched.append(matched)
        elif operator == "ANDNOT" and all(keyword not in current_element for keyword in keywords):
            matched = (current_section, current_element)
            matched.append(matched)
        else:
            display_error_message
        
    finish_time = time.time()
    scanning_time = finish_time - begin_time
    
    return matched, scanning_time

if __name__ == "__main__":

    if len(sys.argv) < 3:
        display_general_message()
        sys.exit(1)
    
    xml_file = [f for f in os.listdir(file_directory) if f.endswith(".xml")]

    section = sys.argv[2] 
    operator = sys.argv[-2] if len(sys.argv) == 5 else "all"
    
    if len(sys.argv) == 5:
        keywords = sys.argv[3].split()
    else:
        keywords = []

    for files in xml_file:
        lines = parse_the_files(os.path.join(file_directory, files))

        if operator not in ["all", "AND", "OR", "ANDNOT"]:
            display_error_message()
        else:
            results = []
            results, scanning_time = scan_the_files(lines, section, keywords, operator)
            info = get_the_info(lines)

            for section, element in results:
                display_information(files, info["provinsi"], info["klasifikasi"], info["sub_klasifikasi"], info["lembaga_peradilan"])
                print(f"Banyaknya dokumen yang ditemukan = {len(results)}")
                print(f"Total waktu pencarian = {scanning_time:.4f} detik")
   
   


    