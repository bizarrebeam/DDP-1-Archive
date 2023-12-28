import os
import sys
import time

# Some displays that will be shown in the terminal based on interactions
display_error_message = lambda: print("The operator should be 'AND', 'OR', or 'ANDNOT' operators.")
display_general_message = lambda: print("The argument is incorrect.")

# Function to parse (read and extract data) the xml files
def parse_the_files(xml_file):
    try:
        # Read the xml file
        with open(xml_file, "r", encoding="utf-8") as file:
            lines = file.readlines()

        info = {
            "provinsi": "",
            "klasifikasi": "",
            "sub_klasifikasi": "",
            "lembaga_peradilan": "",
        }

        # Loop to extract the info from the 'putusan' tag and add it into dictionary
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

        return info

    except Exception as e:
        display_general_message()
        return {}

# Functions to match the keywords based on specific argument (section and operator) given
def match_the_keywords(info, keywords, operator):
    matched = []

    # Check if all keywords are present in the information
    if operator == "AND" and all(keyword in info.values() for keyword in keywords):
        matched.append(info)

    # Check if any keyword is present in the information
    if operator == "OR" and any(keyword in info.values() for keyword in keywords):
        matched.append(info)

    # Check if none of the keywords are present in the information
    if operator == "ANDNOT" and not any(keyword in info.values() for keyword in keywords):
        matched.append(info)

    return matched

if __name__ == "__main__":
    # Check whether the argument given is valid
    if len(sys.argv) < 3:
        display_general_message()
        sys.exit(1)

    # Determine the section, operator, and keywords from the argument given
    section = sys.argv[1]
    operator = sys.argv[-2] if len(sys.argv) == 5 else "all"
    keywords = [sys.argv[2], sys.argv[4]] if len(sys.argv) == 5 else sys.argv[2]

    # Define the directory where the XML files are located
    dataset_directory = os.path.join(os.getcwd(), "dataset")

    # Check if the directory exists
    if not os.path.exists(dataset_directory):
        print("The 'dataset' directory does not exist. Please make sure it's in the correct location.")
        sys.exit(1)

    xml_files = [f for f in os.listdir(dataset_directory) if f.endswith(".xml")]
    matched_results = []

    for file in xml_files:
        xml_file_path = os.path.join(dataset_directory, file)
        info = parse_the_files(xml_file_path)
        files_matched = match_the_keywords(info, keywords, operator)

        if files_matched:
            matched_results.extend(files_matched)

    if matched_results:
        # Display lists of files matched with the argument given
        for result in matched_results:
            # Display the file information in the specified format
            file_info = f"{os.path.basename(xml_file_path)} {result['provinsi']} {result['klasifikasi']} {result['sub_klasifikasi']} {result['lembaga_peradilan']}"
            print(file_info)
