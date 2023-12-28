import os
import sys
import time

# Some displays that will be shown in the terminal based on interactions
display_information = lambda a, b, c, d, e: print(f"{a[:40]:>50s}{b:>15s}{c:>15s}{d:>30s}{e:>20}")
display_error_message = lambda: print("The operator should be 'AND', 'OR', or 'ANDNOT' operators.")
display_general_message = lambda: print("The argument is incorrect.")

# Function to parse (read and extract data) the xml files
def parse_the_files(xml_file):
    try: 
        # Read the xml file
        with open(xml_file, "r", encoding = "utf-8") as file:
            lines = file.readlines()
        
        info = {
            "provinsi": "",
            "klasifikasi": "",
            "sub_klasifikasi": "",
            "lembaga_peradilan": "",
        }
        
        # Loop to extract the info from the 'putusan tag' and add it into dictionary
        in_putusan = False
        for line in lines:
            if not in_putusan and line.startswith("<putusan"):
                in_putusan = True

            if in_putusan:
                words = line.split() 

                for word in words: 
                    if word.startswith("provinsi="): 
                        info["provinsi"] = word.split('"')[1] 
                    elif word.startswith('klasifikasi="'):
                        info["klasifikasi"] = word.split('"')[1]
                    elif word.startswith('sub_klasifikasi="'):
                        info["sub_klasifikasi"] = word.split('"')[1]
                    elif word.startswith('lembaga_peradilan="'):
                        info["lembaga_peradilan"] = word.split('"')[1]
            
            if in_putusan and "</" in line:
                in_putusan = False

        return lines, info
    
    except Exception:
        display_general_message()
        return [], {}

# Functions to match the keywords based on specific argument (section and operator) given
def match_the_keywords(lines, section, keywords, operator):
    matched = []
    begin_time = time.time()

    # Work with the xml content as a single string
    xml_content = "".join(lines)

    if section != "all":
        in_section = False
        current_element = ""

        for line in lines:
            if f"<{section}>" in line:
                in_section = True
                current_element = line.strip()
                continue
            elif f"</{section}>" in line:
                in_section = False
                current_element = ""
                continue

            if in_section:
                current_element += line.strip()

        # Search within the specified section
        if operator == "AND" and all(
            keyword in current_element for keyword in keywords):
            matched.append(current_element)
        elif operator == "OR" and any(keyword in current_element for keyword in keywords):
            matched.append(current_element)
        elif operator == "ANDNOT" and not any(keyword in current_element for keyword in keywords):
            matched.append(current_element)

    else:
        # Work with the whole xml content if the argument 'all' is given
        if operator == "AND" and all(keyword in xml_content for keyword in keywords):
            matched.append(xml_content)
        elif operator == "OR" and any(keyword in xml_content for keyword in keywords):
            matched.append(xml_content)
        elif operator == "ANDNOT" and not any(keyword in xml_content for keyword in keywords):
            matched.append(xml_content)

    finish_time = time.time()
    scanning_time = finish_time - begin_time
        
    return matched, scanning_time

if __name__ == "__main__":
    # Check whether the argument given is valid
    if len(sys.argv) < 3:
        display_general_message()
        sys.exit(1)
    
    # Determine the section, operator, and keywords from the argument given
    section = sys.argv[1]
    operator = sys.argv[-2] if len(sys.argv) == 5 else "all"
    keywords = [sys.argv[2], sys.argv[4]] if len(sys.argv) == 5 else sys.argv[2]
    matched_results = []

    # Iterate over XML files in the "dataset" directory
    for xml_file in os.listdir("dataset"):
        if xml_file.endswith(".xml"):
            xml_path = os.path.join("dataset", xml_file)

            lines, info = parse_the_files(xml_path)
            files_matched, scanning_time = match_the_keywords(
            lines, section, keywords, operator
            )

            if files_matched:
                matched_results.extend(files_matched)

    if matched_results:
        for result in matched_results:
            # Extract info from the result
            info = result[1]

            # Display the file information
            display_information(
                os.path.basename(result[0]), info["provinsi"], info["klasifikasi"], info["sub_klasifikasi"], info["lembaga_peradilan"]
            )

        # Display the number of matching documents and total search time
        print(f"Total number of documents found = {len(matched_results)}")
        print(f"Total search time = {scanning_time:.4f} seconds")
