import os
import sys
import time

# Some displays that will be shown in the terminal based on interactions
display_information = lambda a, b, c, d, e: print(f"{a[:40]:>50s}{b:>15s}{c:>15s}{d:>30s}{e:>20}")
display_error_message = lambda: print("The operator should be AND, OR atau ANDNOT.")
display_general_message = lambda: print("The argument is incorrect.")

# Function to parse (read and extract data) the xml files
def parse_the_files(xml_file):
    try: 
        # Read the xml file
        with open(xml_file, "r", encoding = "utf-8") as file:
            lines = file.readlines()
        
        info = {"provinsi": "", "klasifikasi": "", "sub_klasifikasi": "", "lembaga_peradilan": ""}
        
        # Loop to extract the info from the 'putusan tag' and add it into dictionary
        in_putusan = False
        for line in lines:
            if not in_putusan and line.startswith("<putusan"):
                in_section = True

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
        return []
    
# Functions to match the keywords based on specific argument (section and operator) given
def match_the_keywords(lines, section, keywords, operator):
    matched = []
    begin_time = time.time()

    # Work with the xml content as a single string
    xml_content = "".join(lines)

    # Work with the whole xml content if the argument 'all' given
    if section == "all":
        if operator == "AND" and all(keyword in xml_content for keyword in keywords):
            matched.append(xml_content)
        elif operator == "OR" and any(keyword in xml_content for keyword in keywords):
            matched.append(xml_content) 
        elif operator == "ANDNOT" and not any(keyword in xml_content for keyword in keywords):
            matched.append(xml_content)
    
    # Parse the file to extract content from the specified section
    else:
        in_section = False
        current_element = ""

        for line in lines:
            if f"<{section}>" in line:
                in_section = True
                current_element = line.strip()
                continue
            elif f"</{section}>" in line:
                in_section = False
                current_element = ""   # jd ini tu kan first line (opening tag) set if pertama true, iterates (line pertama). lanjut ke line selanjutnya, dia 
                continue # skip langsung ke if paling bawah, krena in section ny blm ketemu closing tag, blm dimatiin

            if in_section:
                current_element += line.strip() # ini tu ditambahin line yg blm di strip, di atas yg di strip itu line yg ada pening tag ny
        
        # Serch within the specified section
        if operator == "AND" and all(keyword in xml_content for keyword in keywords):
            matched.append(current_element)
        elif operator == "OR" and any(keyword in xml_content for keyword in keywords):
            matched.append(current_element) 
        elif operator == "ANDNOT" and not any(keyword in xml_content for keyword in keywords):
            matched.append(current_element)
        
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

    xml_files = [f for f in os.listdir("dataset") if f.endswith(".xml")]
    for file in xml_files:
        lines, info = parse_the_files(os.path.join("dataset", xml_files))
        files_matched = match_the_keywords(lines, section, keywords, operator)

        if files_matched:
            # Display lists of files matched with the argument given
            display_information(xml_files, info["provinsi"], info["klasifikasi"], info["sub_klasifikasi"], info["lembaga_peradilan"])

            # Display the number of matching documents and total search time
            print(f"Total of documents found = {len(files_matched)} documents")
            print(f"Total search time = {files_matched[1]:.4f} seconds")

            


