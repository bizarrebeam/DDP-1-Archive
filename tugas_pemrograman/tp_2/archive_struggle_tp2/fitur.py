# Kolaborator: Nasha Zahira (2306165553)                                                 

import os
import sys
import time

# Functions to print the table's header
def print_headers():
    print()
    print(
        "| {: >43} | {: >15} | {: >15} | {: >30} | {: >20} |".format(
        "Filename", "Provinsi", "Klasifikasi", "Subklasifikasi", "Lembaga Peradilan"
        )
    )
    print(
        "| {: >43} | {: >15} | {: >15} | {: >30} | {: >20} | ".format(
            "=" * 43, "=" * 15, "=" * 15, "=" * 30, "=" * 20
        )
   )

# Function to display matched results on terminal with the table formatting
def display_matched(a, b, c, d, e):
    print(
        "| {: >43} | {: >15} | {: >15} | {: >30} | {: >20} | ".format(
            a[:40], b[:15], c[:15], d[:30], e[:20]            # Cut the excessive/longer word exclusively
        )
    )
    print(
        "| {: >43} | {: >15} | {: >15} | {: >30} | {: >20} | ".format(
            "-" * 43, "-" * 15, "-" * 15, "-" * 30, "-" * 20
        )
    )

# Function to display an error message for invalid operators
def display_error_message():
    print("The operator should be 'AND', 'OR', or 'ANDNOT' operators.")

# Function to display a general error message for incorrect arguments
def display_general_message():
    print(
        "The argument is incorrect.\n"
        "Please choose one of the right argument as follows:\n"
        "python search.py [section] [keyword]\n"
        "python search.py [section] [1st keyword] [AND/OR/ANDNOT] [2nd keyword]\n"
        )

province_counts = {}
def display_top_provinces():
    print("\nTop provinces matched:")
    sorted_provinces = sorted(province_counts.items(), key=lambda x: x[1], reverse=True)
    for i, (province, count) in enumerate(sorted_provinces[:5], 1):
        print(f"{i}. {province}: {count} times")

"""
Function to extract the putusan tag's attribute 
(tags are at the very top of the file).
The function accept lines within the opened XML file
"""
def extract_tag(lines):
    try:
        attributes = {}                                      # Stored as dictionary
        words = lines.split()                           

        for word in words:
            parts = word.split('=')                          # Because the line is written as tag="data"                                           
            if len(parts) == 2:                              # Splitted into 2 strings
                attributes[parts[0]] = parts[1].strip('"')   # Get the data only

        return attributes

    except Exception:                                        
        return None

"""
If user specify the <section> argument, this 
function will perform a scan in that section only
"""
def scan_for_section(section, keyword_1, operator=None, keyword_2=None):
    begin_time = time.time()
    total_xmls = len(os.listdir("dataset"))
    total_match = 0                                          # Tracks the total file matched     

    # Loop over files on 'dataset' folder                                                  
    for index, xml_dataset in enumerate(os.listdir("dataset")):                 
        if not xml_dataset.endswith(".xml"):                 # Only access the XML file
            continue
        xml_path = os.path.join("dataset", xml_dataset) 

        with open(xml_path, "r") as xml:                     # Read the xml file
            xml_file = xml.read().replace("\n", " ")         # Read the lines as a single string
            attributes = extract_tag(xml_file)               # Access the previous function 
           
            start_tag = xml_file.find(f"<{section}>")        # Find the section's start tag  
            end_tag = xml_file.find(f"</{section}>")         # Find the section's end tag
                                                                                        
            if start_tag != -1 and end_tag != -1:                                           # Making sure each tag placed properly
                xml_content = xml_file.split(f"<{section}>")[1].split(f"</{section}>")[0]   # Scan the data between the tags
                keyword_1_found = keyword_1.lower() in xml_content                          # Marks the first keyword is found
                keyword_2_found = keyword_2 is None or keyword_2.lower() in xml_content     # Marks the second keyword is found

                # Process logic of matching based on operator given 
                if (
                    operator is None and keyword_1_found                                    # User provides one keyword only
                ) or (
                    operator == "AND" and keyword_1_found and keyword_2_found               # AND operator: both keywords matched   
                ) or (
                    operator == "OR" and (keyword_1_found or keyword_2_found)               # OR operator: at least one keyword matched
                ) or (      
                    operator == "ANDNOT" and keyword_1_found and not keyword_2_found        # ANDNOT operator: first keyword matched
                ):                                                                            # excluding the second keyword
                    total_match += 1                                                        # Tracks the total documents matched                                     
                    display_matched(
                        attributes["id"] + ".xml",
                        attributes["provinsi"],
                        attributes["klasifikasi"],
                        attributes["sub_klasifikasi"],
                        attributes["lembaga_peradilan"],
                    )
        
        progress = (index + 1) / total_xmls * 100
        print(f"\rCurrently scanning {attributes['id'] + '.xml'} and [{progress:.2f}%] to go\r", end="")

    # Calculate the time needed to perform the scan
    finish_time = time.time()
    scanning_time = finish_time - begin_time

    # Display final searching results
    print()
    print(
        f"Total number of documents found\t= {total_match}".expandtabs(10)
    )
    print(
        f"Total search time\t= {scanning_time:.3f} seconds".expandtabs(40)
    )

"""
If user provides 'all' argument, this function 
will perform a scan for the entire sections
within file
"""
def scan_all_sections(keyword_1, operator=None, keyword_2=None):
    begin_time = time.time()
    total_xmls = len(os.listdir("dataset"))
    total_match = 0                                         # Tracks the total file matched

    for index, xml_dataset in enumerate(os.listdir("dataset")):
        
        if not xml_dataset.endswith(".xml"):                # Only access the XML file
            continue

        xml_path = os.path.join("dataset", xml_dataset)

        with open(xml_path, "r") as xml:                    # Read the xml file
            xml_file = xml.read().replace("\n", " ")        # Read the lines as a single string
            attributes = extract_tag(xml_file)              # Access the previous function

            keyword_1_found = keyword_1.lower() in xml_file                                 # Marks the first keyword is found
            keyword_2_found = keyword_2 is None or keyword_2.lower() in xml_file            # Marks the second keyword is found

            # Process logic of matching based on operator given
            if (
                operator is None and keyword_1_found                                        # User provides one keyword only
            ) or (
                operator == "AND" and keyword_1_found and keyword_2_found                   # AND operator: both keywords matched
            ) or (
                operator == "OR" and (keyword_1_found or keyword_2_found)                   # OR operator: at least one keyword matched
            ) or (
                operator == "ANDNOT" and keyword_1_found and not keyword_2_found            # ANDNOT operator: first keyword matched
            ):                                                                                # excluding the second keyword
                # Tracks the total documents matched
                total_match += 1
                # Display the file's info on the terminal
                display_matched(
                    attributes["id"] + ".xml",
                    attributes["provinsi"],
                    attributes["klasifikasi"],
                    attributes["sub_klasifikasi"],
                    attributes["lembaga_peradilan"],
                )
        
        progress = (index + 1) / total_xmls * 100
        print(f"\rCurrently scanning {attributes['id'] + '.xml'} and [{progress:.2f}%] to go\r", end="")

    # Calculate the time needed to perform the scan
    finish_time = time.time()
    scanning_time = finish_time - begin_time

    # Display the scanning results
    print()
    print(
        f"Total number of documents found\t= {total_match}".expandtabs(10)
    )
    print(
        f"Total search time\t= {scanning_time:.3f} seconds".expandtabs(40)
    )

# Main function to process the argument
def main(argv):
    input_args = argv 
    province_counts.clear()                        

    # If the argument is invalid
    if len(input_args) < 2 or len(input_args) > 4:                               
        display_general_message()
        sys.exit(1)

    # Assign the argument after validating
    else:                                                 
        section = input_args[0].lower()
        keyword_1 = input_args[1].lower()
        operator = None                                      # Default set: one keyword only without operator
        keyword_2 = None                                     # Default set: one keyword only without operator

        valid_sections = [
            "kepala_putusan", "identitas","riwayat_penahanan", 
            "riwayat_perkara", "riwayat_tuntutan", "riwayat_dakwaan", "fakta", 
            "fakta_umum", "pertimbangan_hukum", "amar_putusan", "penutup"
            ] 
        if section.lower() != "all" and section.lower() not in valid_sections:
            print(
            "Sorry, there's no such section in file.\n"
            'Please choose "all" to search all sections or choose one:\n'
            "kepala_putusan, identitas, riwayat_penahanan, riwayat_perkara,\n"
            "riwayat_tuntutan, riwayat_dakwaan, fakta, fakta_umum,\n"
            "pertimbangan_hukum, amar_putusan, penutup\n"
            )
            sys.exit(1)

        if len(input_args) == 4:                             # If arguments have 2 keywords and operator
            operator = input_args[2].upper()
            keyword_2 = input_args[3].lower()

            if operator not in ["AND", "OR", "ANDNOT"]:      # Validating the operator
                display_error_message()                   
                sys.exit(1)

        print_headers()
        # Process matching search based on arguments given
        if section.lower() == "all":                                    # User didn't specify the section
            scan_all_sections(keyword_1, operator, keyword_2)
        else:
            scan_for_section(section, keyword_1, operator, keyword_2)   # User specify the section
    
    display_top_provinces()
    
# Run the script
if __name__ == "__main__":
    main(sys.argv[1:])                                      # Exclude the script name from the argument
