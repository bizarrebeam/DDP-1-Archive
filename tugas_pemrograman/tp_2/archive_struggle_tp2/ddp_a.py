import os
import sys
import time

# Function to display matched results on the terminal
def display_matched(a, b, c, d, e, f):
    print(f"{a} {b:>15s} {c:>15s} {d:>30s} {e:>20} {f:>10s}")

# Function to display an error message for invalid operators
def display_error_message():
    print("The operator should be 'AND', 'OR', or 'ANDNOT' operators.")

# Function to display a general error message for incorrect arguments
def display_general_message():
    print("The argument is incorrect.")
    print("Please choose one of the right argument as follows")
    print("python search.py [section] [keyword]")
    print("python search.py [section] [1st keyword] [AND/OR/ANDNOT] [2nd keyword]")

def print_progress_bar(iteration, total):
    return print(f'{int(iteration/total * 100)}%')

"""
Function to extract the putusan tag's attribute 
(tags are at the very top of the file). 
The function accept lines within the opened XML file
"""
def extract_tag(lines):
    try:
        attributes = {}
        words = lines.split()

        for word in words:
            parts = word.split('=')
            if len(parts) == 2:
                attributes[parts[0]] = parts[1].strip('"')

        return attributes

    except Exception:
        return None

"""
Functions to perform keyword(s) matching
based on the given operators.
"""
def match_keywords(xml_content, keywords, operator):
    
    keyword_1, keyword_2 = keywords

    if (
        operator is None and keyword_1 in xml_content
    ) or (
        operator == "AND" and (keyword_1 in xml_content and keyword_2 in xml_content)
    ) or (
        operator == "OR" and (keyword_1 in xml_content or keyword_2 in xml_content)
    ) or (
        operator == "ANDNOT" and (keyword_1 in xml_content and keyword_2 not in xml_content)
    ):
        return True

    return False

"""
Functions to find the keywords within
specific section if user provides it
"""
def scan_for_section(section, keywords, operator):

    begin_time = time.time()
    total_match = 0

    for i, xml_dataset in enumerate(os.listdir("dataset")):
        if not xml_dataset.endswith(".xml"):
            continue
        xml_path = os.path.join("dataset", xml_dataset)

        with open(xml_path, "r") as xml:
            xml_file = xml.read().replace("\n", " ")
            attributes = extract_tag(xml_file)

            start_tag = xml_file.find(f"<{section}>")
            end_tag = xml_file.find(f"</{section}>")

            if start_tag != -1 and end_tag != -1:
                xml_content = xml_file[start_tag + len(section) + 2 : end_tag]
                
                if match_keywords(xml_content, keywords, operator):
                    total_match += 1
                    display_matched(
                        attributes["id"] + ".xml",
                        attributes["provinsi"],
                        attributes["klasifikasi"],
                        attributes["sub_klasifikasi"],
                        attributes["lembaga_peradilan"],
                        + print_progress_bar(i + 1, len(os.listdir("dataset")))
                    )

    finish_time = time.time()
    scanning_time = finish_time - begin_time

    if total_match == 0:
        print("No matching searches.")
    else:
        print(f"Total number of documents found\t= {total_match}".expandtabs(10))
        print(f"Total search time\t= {scanning_time:.4f} seconds".expandtabs(40))

# Main function to process the argument
def main(argv):
    input_args = argv

    if len(input_args) < 2:
        display_general_message()
        sys.exit(1)

    section = input_args[0]
    keyword_1 = input_args[1]
    operator = None
    keyword_2 = None

    # Check if the section is either "all" or a valid section name
    valid_sections = ["kepala_putusan", "identitas","riwayat_penahanan", 
        "riwayat_perkara", "riwayat_tuntutan", "riwayat_dakwaan", "fakta", 
        "fakta_umum", "pertimbangan_hukum", "amar_putusan", "penutup"] 

    if section.lower() != "all" and section.lower() not in valid_sections:
        print("Sorry, there's no such section in file.")
        print('Please choose "all" to search all sections or choose one:')
        print("kepala_putusan, identitas, riwayat_penahanan, riwayat_perkara,")
        print("riwayat_tuntutan, riwayat_dakwaan, fakta, fakta_umum,")
        print("pertimbangan_hukum, amar_putusan, penutup")
        sys.exit(1)

    if len(input_args) == 4:
        operator = input_args[2]
        keyword_2 = input_args[3]

        if operator not in ["AND", "OR", "ANDNOT"]:
            display_error_message()
            sys.exit(1)
        
        if not keyword_2:
            display_general_message()
            sys.exit(1)

    keywords = (keyword_1.lower(), keyword_2.lower() if keyword_2 else None)

    if section.lower() == "all":
        match_keywords(keywords, operator)
    else:
        scan_for_section(section, keywords, operator)

if __name__ == "__main__":
    main(sys.argv[1:])
