# Kolaborator: Nasha Zahira (2306165553)

import os
import sys
import time

"""
Function to extract the pututsan tag's attribute.
The function accept lines within opened XML file
"""
def extract_attributes_content(lines):
    # Store the atrribute's content in dictionary
    content = {
        "xml_name": "",
        "provinsi": "",
        "klasifikasi": "",
        "sub_klasifikasi": "",
        "lembaga_peradilan": "",
        }

    try: # Attempt to parse the attributes
        for line in lines:
            if "<putusan" in line:              # Get the content in attribute tag
                words = line.split() 
            
                for word in words:              # Stored the specific content from attribute tag
                    if word.startswith("id="): 
                        content["xml_name"] = word.split('"')[1].rjust(40)
                    elif word.startswith("provinsi="): 
                        content["provinsi"] = word.split('"')[1].rjust(15)
                    elif word.startswith('klasifikasi="'):
                        content["klasifikasi"] = word.split('"')[1].rjust(15)
                    elif word.startswith('sub_klasifikasi="'):
                        content["sub_klasifikasi"] = word.split('"')[1].rjust(30)
                    elif word.startswith('lembaga_peradilan="'):
                        content["lembaga_peradilan"] = word.split('"')[1].rjust(20)    
        return content
    
    except Exception: # Handle the trouble in parsing tag
        return None

def display_matched_files(content):
    print()

"""
If user specify the <section> argument, this 
function will perform a search in that section
"""
def search_for_section(section, keyword_1, operator = None, keyword_2 = None):
    begin_time = time.time()
    matched = 0

    # Loop to iterate all XML files in the dataset directory
    for xml_dataset in os.listdir("dataset"):
        if xml_dataset.endswith(".xml"):
            xml_path = os.path.join("dataset", xml_dataset)

        # Open each XML file 
        with open(xml_path, "r") as xml:
            xml_file = xml.readlines()

        # Access the attributes content function


        # Declare the specific section to perform the match
        begin_tag = f"<{section}>"
        end_tag = f"<\{section}>"
        start_line = xml_file.find(begin_tag)
        end_line = xml_file.find(end_tag)

        # Perform the search on that section only
        if begin_tag != 1 and end_tag != -1:            # Making sure the start and end tag placed properly
            xml_content = xml_file[begin_tag:end_tag]   # Read the content within that section

            if operator is None:
                if keyword_1.lower() in xml_content:
                    matched += 1

                    




            



