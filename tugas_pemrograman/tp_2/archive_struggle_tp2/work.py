import os
import sys
import time

display_matched = lambda a, b, c, d, e: print(f"{a}{b:>15s}{c:>15s}{d:>30s}{e:>20}")
display_error_message = lambda: print("The operator should be 'AND', 'OR', or 'ANDNOT' operators.")
display_general_message = lambda: print("The argument is incorrect.")

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

def scan_for_section(section, keyword_1, operator=None, keyword_2=None):
    begin_time = time.time()
    total_match = 0

    for xml_dataset in os.listdir("dataset"):
        if not xml_dataset.endswith(".xml"):
            continue

        xml_path = os.path.join("dataset", xml_dataset)

        with open(xml_path, "r") as xml:
            xml_file = xml.read().replace("\n", " ")
            attributes = extract_tag(xml_file)

            start_tag = xml_file.find(f"<{section}>")
            end_tag = xml_file.find(f"</{section}>")

            if start_tag != -1 and end_tag != -1:
                xml_content = xml_file.split(f"<{section}>")[1].split(f"</{section}>")[0]
                keyword_1_found = keyword_1.lower() in xml_content
                keyword_2_found = keyword_2 is None or keyword_2.lower() in xml_content

                if (operator is None and keyword_1_found) or \
                   (operator == "AND" and keyword_1_found and keyword_2_found) or \
                   (operator == "OR" and (keyword_1_found or keyword_2_found)) or \
                   (operator == "ANDNOT" and keyword_1_found and not keyword_2_found):
                    total_match += 1
                    display_matched(attributes["id"] + ".xml", attributes["provinsi"], attributes["klasifikasi"], attributes["sub_klasifikasi"], attributes["lembaga_peradilan"])

    # Calculate the time needed to perform the scan
    finish_time = time.time()
    scanning_time = finish_time - begin_time    

    # Display the scanning results
    print(f"Total number of documents found\t= {total_match}".expandtabs(10))
    print(f"Total search time\t= {scanning_time:.4f} seconds".expandtabs(40))

def scan_all_sections(keyword_1, operator=None, keyword_2=None):
    begin_time = time.time()
    total_match = 0

    for xml_dataset in os.listdir("dataset"):
        if not xml_dataset.endswith(".xml"):
            continue

        xml_path = os.path.join("dataset", xml_dataset)

        with open(xml_path, "r") as xml:
            xml_file = xml.read().replace("\n", " ")
            attributes = extract_tag(xml_file)
        
            keyword_1_found = keyword_1.lower() in xml_file
            keyword_2_found = keyword_2 is None or keyword_2.lower() in xml_file

            if (operator is None and keyword_1_found) or \
                (operator == "AND" and keyword_1_found and keyword_2_found) or \
                (operator == "OR" and (keyword_1_found or keyword_2_found)) or \
                (operator == "ANDNOT" and keyword_1_found and not keyword_2_found):
                total_match += 1
                display_matched(attributes["id"] + ".xml", attributes["provinsi"], attributes["klasifikasi"], attributes["sub_klasifikasi"], attributes["lembaga_peradilan"])

    # Calculate the time needed to perform the scan
    finish_time = time.time()
    scanning_time = finish_time - begin_time    

    # Display the scanning results
    print(f"Total number of documents found\t= {total_match}".expandtabs(10))
    print(f"Total search time\t= {scanning_time:.4f} seconds".expandtabs(40))

def main(argv):
    input_args = argv  # Use the provided argument list

    if len(input_args) < 2:  # If the argument is invalid
        display_general_message()
        
        sys.exit(1)

    else:  # Assign the argument after validating
        section = input_args[0]
        keyword_1 = input_args[1]
        operator = None  # Initial assumption: len(input_args) == 2
        keyword_2 = None  # Initial assumption: len(input_args) == 2

        if len(input_args) == 4:  # If arguments have 2 keywords and operator
            operator = input_args[2]
            keyword_2 = input_args[3]

            if operator not in ["AND", "OR", "ANDNOT"]:  # Validating the operator
                display_error_message()
                sys.exit(1)
        
        # Call the functions defined
        if section.lower() == "all":
            scan_all_sections(keyword_1, operator, keyword_2)
        else:
            scan_for_section(section, keyword_1, operator, keyword_2)

# Run the script
if __name__ == "__main__":
    main(sys.argv[1:])
    


    
