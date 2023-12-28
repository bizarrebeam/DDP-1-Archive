import os # ini yg yaqueen beneran yaqueen
import sys
import time

# Display error issue if the argument is invalid 
display_error_message = lambda: print("The operator should be 'AND', 'OR', or 'ANDNOT' operators.")
display_general_message = lambda: print("The argument is incorrect.")

# Function to read the xml files
def open_the_xml(xml_file):
    try: 
        with open(xml_file, "r", encoding = "utf-8") as file:
            xml_content = file.readlines()
            lines = "".join(xml_content).split("\n")
        return lines
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
def parse_the_xml(lines, section, keywords, operator):
    begin_time = time.time()

    current_section = ""
    section_content = []

    if section.lower() == "all":
        sections = []
        tag = ""

        for line in lines:
            if line.startswith("<") and line.endswith(">") and not tag.startswith("</"):
                tag = line[1:-1]
                sections.append(tag)
    else:
        sections = [section]

    matched = []

    for current_section in sections:  
        for line in lines:
            start_section = f"<{current_section}>"
            end_section = f"</{current_section}>"
            at_start = line.find(start_section)
            at_end = line.find(end_section)

            if start_section in line:
                current_section += line[at_start + len(start_section):].strip()
            elif end_section in line:
                current_section += line[:at_end].strip()
                section_content.append(current_section)
                current_section = ""
            elif current_section:
                current_section += line.strip()
        
        if len(keywords) == 1 and not operator:
            operator = "AND"

        for words in section_content:
            if operator == "AND" and all(keyword in words for keyword in keywords):
                matched.append(words)

            elif operator == "OR" and any(keyword in words for keyword in keywords):
                matched.append(words)

            elif operator == "ANDNOT" and keywords[0] in words and not keywords[1] in words:
                matched.append(words)
    
    finish_time = time.time()
    scanning_time = finish_time - begin_time

    return matched, scanning_time

if __name__ == "__main__":
    section = sys.argv[1]

    if len(sys.argv) == 3:
        operator = "AND"
        keywords = [sys.argv[2]]
    elif len(sys.argv) == 5:
        operator = sys.argv[-2]
        keywords = [sys.argv[2], sys.argv[-1]]
    else:
        display_error_message()
        sys.exit(1)

    directory = os.path.join(os.getcwd(), "dataset")
    total_documents_matched = 0
    total_search_time = 0

    for xml_file in os.listdir(directory):
        if xml_file.endswith(".xml"):
            xml_path = os.path.join(directory, xml_file)
        
            xml_content = open_the_xml(xml_path)

            if xml_content:
                matched, scanning_time = parse_the_xml(xml_content, section, keywords, operator)
                total_search_time += scanning_time

                if matched:
                    total_documents_matched += 1
                    attributes_content = extract_attributes_content(xml_content.split())
                    if attributes_content:
                        display_information(attributes_content)
        else:
            pass
    
    print(f"Total number of documents found = {total_documents_matched}")
    print(f"Total search time = {total_search_time:.4f} seconds")
                    
        





            