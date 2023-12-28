import os
import sys
import time

# Functions to display issue messages if the argument given is invalid
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

def scan_for_section(section, keyword_1, operator = None, keyword_2 = None):
    begin_time = time.time()
    total_match = 0

    for xml_dataset in os.listdir("dataset"):
        if xml_dataset.endswith(".xml"):
            xml_path = os.path.join("dataset", xml_dataset)

            with open(xml_path, "r") as xml:
                xml_file = xml.read().replace("\n", " ")
                attributes = extract_tag(xml_file)
                
                start_tag = xml_file.find(f"<{section}>")
                end_tag = xml_file.find(f"</{section}>")

                if start_tag != -1 and end_tag != -1:
                    xml_content = xml_file.split(f"<{section}>")[1].split(f"</{section}>")[0]

                    if operator is None and (keyword_1.lower() in xml_content):
                        total_match += 1
                        display_matched(attributes["id"] + ".xml", attributes["provinsi"], attributes["klasifikasi"], attributes["sub_klasifikasi"], attributes["lembaga_peradilan"])

                    elif operator == "AND" and (keyword_1.lower() in xml_content and keyword_2.lower() in xml_content):                 
                        total_match += 1
                        display_matched(attributes["id"] + ".xml", attributes["provinsi"], attributes["klasifikasi"], attributes["sub_klasifikasi"], attributes["lembaga_peradilan"])

                    elif operator == "OR" and (keyword_1.lower() in xml_content or keyword_2.lower() in xml_content):                  
                        total_match += 1
                        display_matched(attributes["id"] + ".xml", attributes["provinsi"], attributes["klasifikasi"], attributes["sub_klasifikasi"], attributes["lembaga_peradilan"])
                    
                    elif operator == "ANDNOT" and (keyword_1.lower() in xml_content and not keyword_2.lower() in xml_content):                   
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
        if xml_dataset.endswith(".xml"):
            xml_path = os.path.join("dataset", xml_dataset)

            with open(xml_path, "r") as xml:
                xml_file = xml.read().replace("\n", " ")
                attributes = extract_tag(xml_file)

                if operator is None and (keyword_1.lower() in xml_file):
                    total_match += 1
                    display_matched(attributes["id"] + ".xml", attributes["provinsi"], attributes["klasifikasi"], attributes["sub_klasifikasi"], attributes["lembaga_peradilan"])

                elif operator == "AND" and (keyword_1.lower() in xml_file and keyword_2.lower() in xml_file):                 
                    total_match += 1
                    display_matched(attributes["id"] + ".xml", attributes["provinsi"], attributes["klasifikasi"], attributes["sub_klasifikasi"], attributes["lembaga_peradilan"])

                elif operator == "OR" and (keyword_1.lower() in xml_file or keyword_2.lower() in xml_file):                  
                    total_match += 1
                    display_matched(attributes["id"] + ".xml", attributes["provinsi"], attributes["klasifikasi"], attributes["sub_klasifikasi"], attributes["lembaga_peradilan"])
                
                elif operator == "ANDNOT" and (keyword_1.lower() in xml_file and not keyword_2.lower() in xml_file):                   
                    total_match += 1
                    display_matched(attributes["id"] + ".xml", attributes["provinsi"], attributes["klasifikasi"], attributes["sub_klasifikasi"], attributes["lembaga_peradilan"])

    # Calculate the time needed to perform the scan
    finish_time = time.time()
    scanning_time = finish_time - begin_time    

    # Display the scanning results
    print(f"Total number of documents found\t= {total_match}".expandtabs(10))
    print(f"Total search time\t= {scanning_time:.4f} seconds".expandtabs(40))

# Run the script
if __name__ == "__main__":
    input_args = sys.argv[1:]  # Exclude the script name from the argument

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
