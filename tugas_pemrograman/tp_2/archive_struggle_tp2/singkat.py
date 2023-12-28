import os
import sys
import time

# Function to display matched results on the terminal
def display_matched(a, b, c, d, e):
    print(f"{a} {b:>15s} {c:>15s} {d:>30s} {e:>20}")

# Function to display an error message for invalid operators
def display_error_message():
    print("The operator should be 'AND', 'OR', or 'ANDNOT' operators.")

# Function to display a general error message for incorrect arguments
def display_general_message():
    print("The argument is incorrect.")

"""
Function to extract the putusan tag's attribute 
(tags are at the very top of the file).
The function accepts lines within the opened XML file
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

# Function to cache file content and attributes
def cache_file_content(xml_file_path):
    with open(xml_file_path, "r") as xml:
        xml_content = xml.read().replace("\n", " ")
        attributes = extract_tag(xml_content)
        xml_content_lower = xml_content.lower()
        return attributes, xml_content_lower

# Function to search for keywords in a given section
def search_section_cached(attributes, xml_content_lower, keywords, operator):
    keyword_1, keyword_2 = keywords

    if (
        operator is None and keyword_1 in xml_content_lower
    ) or (
        operator == "AND" and keyword_1 in xml_content_lower and keyword_2 in xml_content_lower
    ) or (
        operator == "OR" and (keyword_1 in xml_content_lower or keyword_2 in xml_content_lower)
    ) or (
        operator == "ANDNOT" and keyword_1 in xml_content_lower and keyword_2 not in xml_content_lower
    ):
        return True
    return False

"""
If the user specifies the <section> argument, this 
function will perform a scan in that section only
"""
def scan_for_section_cached(section, keywords, operator):
    begin_time = time.time()
    total_match = 0

    # Cache file content and attributes
    cached_files = []
    for xml_dataset in os.listdir("dataset"):
        if not xml_dataset.endswith(".xml"):
            continue
        xml_path = os.path.join("dataset", xml_dataset)
        attributes, xml_content_lower = cache_file_content(xml_path)
        cached_files.append((attributes, xml_content_lower))

    for attributes, xml_content_lower in cached_files:
        start_tag = xml_content_lower.find(f"<{section}>")
        end_tag = xml_content_lower.find(f"</{section}>")

        if start_tag != -1 and end_tag != -1:
            xml_content = xml_content_lower[start_tag + len(section) + 2 : end_tag]
            if search_section_cached(attributes, xml_content_lower, keywords, operator):
                total_match += 1
                display_matched(
                    attributes["id"] + ".xml",
                    attributes["provinsi"],
                    attributes["klasifikasi"],
                    attributes["sub_klasifikasi"],
                    attributes["lembaga_peradilan"],
                )

    finish_time = time.time()
    scanning_time = finish_time - begin_time

    print(f"Total number of documents found\t= {total_match}".expandtabs(10))
    print(f"Total search time\t= {scanning_time:.4f} seconds".expandtabs(40))

"""
If the user provides 'all' argument, this function 
will perform a scan for the entire sections
within the file
"""
def scan_all_sections_cached(keywords, operator):
    begin_time = time.time()
    total_match = 0

    # Cache file content and attributes
    cached_files = []
    for xml_dataset in os.listdir("dataset"):
        if not xml_dataset.endswith(".xml"):
            continue
        xml_path = os.path.join("dataset", xml_dataset)
        attributes, xml_content_lower = cache_file_content(xml_path)
        cached_files.append((attributes, xml_content_lower))

    for attributes, xml_content_lower in cached_files:
        if search_section_cached(attributes, xml_content_lower, keywords, operator):
            total_match += 1
            display_matched(
                attributes["id"] + ".xml",
                attributes["provinsi"],
                attributes["klasifikasi"],
                attributes["sub_klasifikasi"],
                attributes["lembaga_peradilan"],
            )

    finish_time = time.time()
    scanning_time = finish_time - begin_time

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

    if len(input_args) == 4:
        operator = input_args[2]
        keyword_2 = input_args[3]

        if operator not in ["AND", "OR", "ANDNOT"]:
            display_error_message()
            sys.exit(1)

    keywords = (keyword_1.lower(), keyword_2.lower() if keyword_2 else None)

    if section.lower() == "all":
        scan_all_sections_cached(keywords, operator)
    else:
        scan_for_section_cached(section, keywords, operator)

if __name__ == "__main__":
    main(sys.argv[1:])
