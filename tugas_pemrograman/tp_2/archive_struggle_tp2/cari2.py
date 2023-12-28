import os # ini yg yaqueen
import sys
import time

# Display error issue if the argument is invalid 
display_error_message = lambda: print("The operator should be 'AND', 'OR', or 'ANDNOT' operators.")
display_general_message = lambda: print("The argument is incorrect.")

def read_the_xml(xml_file):
    try: 
        with open(xml_file, "r", encoding = "utf-8") as file:
            for line in file:
                yield line.strip()
    except Exception:
        display_general_message()
        return None

# Functions to extract the putusan tag's attribute 
def extract_attributes_content(lines):
    content = {
        "xml_name": "",
        "provinsi": "",
        "klasifikasi": "",
        "sub_klasifikasi": "",
        "lembaga_peradilan": "",
        }

    for line in lines:
        if "<putusan" in line:
            words = line.split() 

            for word in words: 
                if word.startswith("id="): 
                    content["xml_name"] = word.split('"')[1]
                elif word.startswith("provinsi="): 
                    content["provinsi"] = word.split('"')[1] 
                elif word.startswith('klasifikasi="'):
                    content["klasifikasi"] = word.split('"')[1]
                elif word.startswith('sub_klasifikasi="'):
                    content["sub_klasifikasi"] = word.split('"')[1]
                elif word.startswith('lembaga_peradilan="'):
                    content["lembaga_peradilan"] = word.split('"')[1]
        
    return content

# Functions to display the extracted attribute from the putusan tag
def display_information(content):
    print(f"{content['xml_name']:<40s}{content['provinsi']:>15s}"
        f"{content['klasifikasi']:>15s}{content['sub_klasifikasi']:<30s}"
        f"{content['lembaga_peradilan']:<20s}")

# Functions to parse the file content and attempt to match the argument
def match_the_keywords(xml_file, section, keywords, operator):
    begin_time = time.time()
    current_section = ""
    matched = False

    for line in read_the_xml(xml_file) : 
        start_section = f"<{current_section}>"
        end_section = f"</{current_section}>"
        at_start = line.find(start_section)
        at_end = line.find(end_section)

        if start_section in line:
            current_section += line[at_start + len(start_section):].strip()

        elif end_section in line:
            current_section += line[:at_end].strip()

            if operator == "AND" and any(keyword in current_section for keyword in keywords):
                matched = True

                display_the_match = extract_attributes_content(current_section.split())
                if display_the_match:
                    display_information(display_the_match)

            elif operator == "OR" and any(keyword in current_section for keyword in keywords):
                matched = True

                display_the_match = extract_attributes_content(current_section.split())
                if display_the_match:
                    display_information(display_the_match)

            elif operator == "ANDNOT" and keywords[0] in current_section and not keywords[1] in current_section:
                matched = True

                display_the_match = extract_attributes_content(current_section.split())
                if display_the_match:
                    display_information(display_the_match)

            current_section = ""

        elif current_section:
            current_section += line.strip()
    
    finish_time = time.time()
    scanning_time = finish_time - begin_time

    return matched, scanning_time

if __name__ == "__main__":
    input_args = sys.argv[1:]
   
    if len(input_args) == 0:
        display_general_message()
        sys.exit(1)
    
    section = input_args[0]
    operator = "AND"
    keywords = []

    if len(input_args) >= 2:
        operator = input_args[1]
        keywords = input_args [2:]

    directory = os.path.join(os.getcwd(), "dataset")
    total_documents_matched = 0
    total_search_time = 0

    for xml_file in os.listdir(directory):
        if xml_file.endswith(".xml"):
            xml_path = os.path.join(directory, xml_file)

            matched, scanning_time = match_the_keywords(xml_path, section, keywords, operator)
            
            if matched:
                total_documents_matched += 1
                total_search_time += scanning_time
    
    print(f"Total number of documents found = {total_documents_matched}")
    print(f"Total search time = {total_search_time:.4f} seconds")

            
                    
        





            