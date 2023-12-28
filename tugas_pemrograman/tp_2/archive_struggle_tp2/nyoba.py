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
    print("Please choose one of the right argument as follows")
    print("python search.py [section] [keyword]")
    print("python search.py [section] [1st keyword] [AND/OR/ANDNOT] [2nd keyword]")

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
Functions to perform keyword(s) matching
based on the given operators.
"""
def match_keywords(xml_content, keywords, operator):
    keyword_1, keyword_2 = keywords     # Accept up to two keywords

    if (
        operator is None and keyword_1 in xml_content
    ) or (
        operator == "AND" and (keyword_1 in xml_content and keyword_2 in xml_content)
    ) or (
        operator == "OR" and (keyword_1 in xml_content or keyword_2 in xml_content)
    ) or (
        operator == "ANDNOT" and (keyword_1 in xml_content and keyword_2 not in xml_content)
    ):
        return True                     # Track that matched keywords find

    return False                        # Track that there's no matched find

"""
Functions to find the keywords within
specific section if user provides it
"""
def scan_for_section(section, keywords, operator):

    begin_time = time.time()
    total_match = 0                                       # Tracks the total file matched      

    # Loop over files on 'dataset' folder                 
    for xml_dataset in os.listdir("dataset"):
        if not xml_dataset.endswith(".xml"):              # Only access the XML file
            continue
        xml_path = os.path.join("dataset", xml_dataset)

        with open(xml_path, "r") as xml:                  # Read the xml file
            xml_file = xml.read().replace("\n", " ")      # Read the lines as a single string
            attributes = extract_tag(xml_file)            # Access the previous functions

            start_tag = xml_file.find(f"<{section}>")     # Find the section's start tag
            end_tag = xml_file.find(f"</{section}>")      # Find the section's end tag

            if start_tag != -1 and end_tag != -1:                                   # Making sure each tag placed properly
                xml_content = xml_file[start_tag + len(section) + 2 : end_tag]      # Get the info by skip the opening tag 
                                                                                        # and the following space
                if match_keywords(xml_content, keywords, operator):                 # Access the previous function
                    total_match += 1                                                # Tracks the total documents matched
                    display_matched(                                                # Display the file's info on the terminal
                        attributes["id"] + ".xml",
                        attributes["provinsi"],
                        attributes["klasifikasi"],
                        attributes["sub_klasifikasi"],
                        attributes["lembaga_peradilan"],
                    )

    # Calculate the time needed to perform the scan
    finish_time = time.time()
    scanning_time = finish_time - begin_time

    if total_match == 0:                    
        print("Sorry, there's no matching searches.")      
    
    print(f"Total number of documents found\t= {total_match}".expandtabs(10))
    print(f"Total search time\t= {scanning_time:.4f} seconds".expandtabs(40))

# Main function to process the argument
def main(argv):
    input_args = argv                                 # Process the given argument

    if len(input_args) < 2 or len(input_args)  > 4:    # If the argument's length 
        display_general_message()
        sys.exit(1)

    section = input_args[0]                           # Assign the argument
    keyword_1 = input_args[1]
    operator = None                                   # Default set: one keyword only without operator
    keyword_2 = None                                  # Default set: one keyword only without operator

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

    if len(input_args) == 4:                            # Assign the rest of argument
        operator = input_args[2]
        keyword_2 = input_args[3]

        if operator not in ["AND", "OR", "ANDNOT"]:     # Validating the operator
            display_error_message()
            sys.exit(1)
        
        if not keyword_2:                               # Check if user give operator but not
            display_general_message()                       # with the second keyword
            sys.exit(1)

    # Assign the rest of the argument
    keywords = (keyword_1.lower(), keyword_2.lower() if keyword_2 else None) 

    # Call the functions to perform the scanning
    scan_for_section(section, keywords, operator)

# Run the script
if __name__ == "__main__":
    main(sys.argv[1:])                                  # Exclude the script name from the argument
