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
        with open(xml_file, "r", encoding="utf-8") as file:
            lines = file.readlines()

        putusan_data = []
        info = {
            "provinsi": "",
            "klasifikasi": "",
            "sub_klasifikasi": "",
            "lembaga_peradilan": "",
        }

        # Loop to extract the info from the 'putusan' tags and add it into a list of dictionaries
        in_putusan = False
        for line in lines:
            if line.startswith("<putusan"):
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

            if in_putusan and "</putusan>" in line:
                in_putusan = False
                putusan_data.append(info)

        return putusan_data

    except Exception:
        display_general_message()
        return []

# Function to match the keywords based on specific argument (section and operator) given
def match_the_keywords(putusan_data, section, keywords, operator):
    matched = []
    begin_time = time.time()

    for data in putusan_data:
        content = f"{data['provinsi']} {data['klasifikasi']} {data['sub_klasifikasi']} {data['lembaga_peradilan']}"
        
        if operator == "AND" and all(keyword in content for keyword in keywords):
            matched.append(data)
        elif operator == "OR" and any(keyword in content for keyword in keywords):
            matched.append(data)
        elif operator == "ANDNOT" and not any(keyword in content for keyword in keywords):
            matched.append(data)

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

    if section != "all":
        keywords = [sys.argv[2], sys.argv[4]] if len(sys.argv) == 5 else [sys.argv[2]]
    else:
        keywords = [sys.argv[2]] if len(sys.argv) == 4 else sys.argv[2]

    matched_results = []

    # Iterate over XML files in the "dataset" directory
    for xml_file in os.listdir("dataset"):
        if xml_file.endswith(".xml"):
            xml_path = os.path.join("dataset", xml_file)

            putusan_data = parse_the_files(xml_path)
            files_matched, scanning_time = match_the_keywords(
                putusan_data, section, keywords, operator
            )

            if files_matched:
                matched_results.extend(files_matched)

    if matched_results:
        for result in matched_results:
            # Display the file information
            display_information(
                os.path.basename(xml_file),
                result["provinsi"],
                result["klasifikasi"],
                result["sub_klasifikasi"],
                result["lembaga_peradilan"]
            )

        # Display the number of matching documents and total search time
        print(f"Total number of documents found = {len(matched_results)}")
        print(f"Total search time = {scanning_time:.4f} seconds")
