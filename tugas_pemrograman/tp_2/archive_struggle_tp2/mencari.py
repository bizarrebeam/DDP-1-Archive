# Kolaborator: Nasha Zahira (2306165553)

import os
import sys
import time

# Functions to display issue messages if the argument given is invalid
display_error_message = lambda: print(
    "The operator should be 'AND', 'OR', or 'ANDNOT' operators."
    )
display_general_message = lambda: print(
    "The argument is incorrect."
    )

"""
Function to extract the putusan tag's attribute.
The function accept lines within opened XML file
"""
def extract_attributes_content(lines):
    try: # Attempt to parse the attributes
        for line in lines:
            if "<putusan" in line: # Get the content within the putusan tag             
                words = line.split() 
            
                for word in words:              
                    if word.startswith("id="): 
                        xml_filename = word.split('"')[1].rjust(40)
                    elif word.startswith("provinsi="): 
                        provinsi = word.split('"')[1].rjust(15)
                    elif word.startswith('klasifikasi="'):
                        klasifikasi = word.split('"')[1].rjust(15)
                    elif word.startswith('sub_klasifikasi="'):
                        sub_klasifikasi = word.split('"')[1].rjust(30)
                    elif word.startswith('lembaga_peradilan="'):
                        lembaga_peradilan = word.split('"')[1].rjust(20)    
        
        return xml_filename, provinsi, klasifikasi, sub_klasifikasi, lembaga_peradilan
    
    except Exception: # Handle the trouble in parsing tag
        return None, None, None, None, None

"""
If user specify the <section> argument, this 
function will perform a scan in that section only
"""
def scan_for_section(section, keyword_1, operator = None, keyword_2 = None):
    begin_time = time.time()
    total_match = 0

    # Loop to iterate all XML files in the dataset directory
    for xml_dataset in os.listdir("dataset"):
        if xml_dataset.endswith(".xml"):
            xml_path = os.path.join("dataset", xml_dataset)

            # Open each XML file 
            with open(xml_path, "r") as xml:
                xml_file = xml.read().replace("\n", " ")

                # Access the attributes content function
                display_matched = extract_attributes_content(xml_file)

                if display_matched is not None:
                    xml_filename, provinsi, klasifikasi, sub_klasifikasi, lembaga_peradilan = display_matched

                    # Declare the specific section to perform the match
                    begin_tag = f"<{section}>"
                    end_tag = f"</{section}>"
                    start_line = xml_file.find(begin_tag)
                    end_line = xml_file.find(end_tag)

                    # Making sure the start and end tag placed properly
                    if start_line != -1 and end_line != -1:    
                        # Scan the content within that section        
                        xml_content = xml_file[start_line:end_line]   

                        # If user only provides one keyword
                        if operator is None:                                   
                            if keyword_1.lower() in xml_content:
                                total_match += 1
                                print(f"{xml_filename}{provinsi}{klasifikasi}{sub_klasifikasi}{lembaga_peradilan}")

                        # Both keywords in that section's content                       
                        elif operator == "AND":                     
                            if keyword_1.lower() in xml_content and keyword_2.lower() in xml_content:
                                total_match += 1
                                print(f"{xml_filename}{provinsi}{klasifikasi}{sub_klasifikasi}{lembaga_peradilan}")

                        # One of the keyword in that section's content
                        elif operator == "OR":  
                            if keyword_1.lower() in xml_content or keyword_2.lower() in xml_content:
                                total_match += 1
                                print(f"{xml_filename}{provinsi}{klasifikasi}{sub_klasifikasi}{lembaga_peradilan}")

                        # The first keyword in the section but not the second keyword
                        elif operator == "ANDNOT": 
                            if keyword_1.lower() in xml_content and not keyword_2.lower() in xml_content:
                                total_match += 1
                                print(f"{xml_filename}{provinsi}{klasifikasi}{sub_klasifikasi}{lembaga_peradilan}")

    # Calculate the time needed to perform the scan
    finish_time = time.time()
    scanning_time = finish_time - begin_time    

    # Display the scanning results
    print(f"Total number of documents found\t= {total_match}".expandtabs(10))
    print(f"Total search time\t= {scanning_time:.4f} seconds".expandtabs(40))

"""
If user provides 'all' argument, this function 
will perform a scan for the entire sections
within file
"""
def scan_entire_sections(keyword_1, operator = None, keyword_2 = None):
    begin_time = time.time()
    total_match = 0

    # Loop to iterate all XML files in the dataset directory
    for xml_dataset in os.listdir("dataset"):
        if xml_dataset.endswith(".xml"):
            xml_path = os.path.join("dataset", xml_dataset)

            # Open each XML file 
            with open(xml_path, "r") as xml:
                xml_file = xml.read().replace("\n", " ")

                # Access the attributes content function
                display_matched = extract_attributes_content(xml_file)

                if display_matched is not None:
                    xml_filename, provinsi, klasifikasi, sub_klasifikasi, lembaga_peradilan = display_matched
        
                # If user only provides one keyword
                if operator is None:                                   
                    if keyword_1.lower() in xml_file:
                        total_match += 1
                        print(f"{xml_filename}{provinsi}{klasifikasi}{sub_klasifikasi}{lembaga_peradilan}")

                # Both keywords in that section's content                                    
                elif operator == "AND":                         
                    if keyword_1.lower() in xml_file and keyword_2.lower() in xml_file:
                        total_match += 1
                        print(f"{xml_filename}{provinsi}{klasifikasi}{sub_klasifikasi}{lembaga_peradilan}")
                
                # One of the keyword in that section's content
                elif operator == "OR":      
                    if keyword_1.lower() in xml_file or keyword_2.lower() in xml_file:
                        total_match += 1
                        print(f"{xml_filename}{provinsi}{klasifikasi}{sub_klasifikasi}{lembaga_peradilan}")

                # The first keyword in that section but not the second keyword
                elif operator == "ANDNOT":  
                    if keyword_1.lower() in xml_file and not keyword_2.lower() in xml_file:
                        total_match += 1
                        print(f"{xml_filename}{provinsi}{klasifikasi}{sub_klasifikasi}{lembaga_peradilan}")

    # Calculate the time needed to perform the scan
    finish_time = time.time()
    scanning_time = finish_time - begin_time    

    # Display the scanning results
    print(f"Total number of documents found\t= {total_match}".expandtabs(10))
    print(f"Total search time\t= {scanning_time:.4f} seconds".expandtabs(30))

# Run the script
if __name__ == "__main__":

    input_args = sys.argv[1:]           # Exclude the script name from the argument

    if len(input_args) < 2:             # If the argument is invalid
        display_general_message()
        sys.exit(1)
    else:                               # Assign the argument after validating
        section = input_args[0]         
        keyword_1 = input_args[1]
        operator = None                 # Initial assumption: len(input_args) == 2
        keyword_2 = None                # Initial assumption: len(input_args) == 2

        if len(input_args) == 4:        # If arguments have 2 keywords and operator
            operator = input_args[-2]
            keyword_2 = input_args[-1]

            if operator not in ["AND", "OR", "ANDNOT"]: # Validating the operator
                display_error_message()
                sys.exit(1)

    # Call the functions defined
    if section.lower() == "all":        
        scan_entire_sections(keyword_1, operator, keyword_2)
    else:
        scan_for_section(section, keyword_1, operator, keyword_2)

        

    












                    




            



