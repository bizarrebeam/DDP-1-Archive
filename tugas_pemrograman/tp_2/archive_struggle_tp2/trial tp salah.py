import argparse
import xml.etree.ElementTree as ET

display_information = lambda a, b, c, d, e: print(f"{a[:40]:>50s} {b:>15s} {c:>15s} {d:>30s} {e:>20}")
display_error_message = lambda: print("Operator harus berupa AND, OR atau ANDNOT.")
display_general_message = lambda: print("Argumen program tidak benar.")


def scan_the_files(xml_file, sections, keywords, operator):
    # Parse XML into Element Tree
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Initial list to store matched results
    outputs = []

    # Iterate throught the XML elements to search for matching data
    for element in root.findall(sections):
        matched = all(keyword in element for keyword in keywords)

        # AND, OR, or ANDNOT argument 
        if operator == "AND" and matched:
            outputs.append(element)
        if operator == "OR" and matched:
            outputs.append(element)
        if operator == "ANDNOT" and not matched:
            outputs.append(element)

    for output in outputs:
        amar = output.get("amar")
        provinsi = output.get("provinsi")
        klasifikasi = output.get("klasifikasi")
        sub_klasifikasi = output.get("sub_klasifikasi")
        lembaga_peradilan = output.get("lembaga_peradilan")
    
        display_information(xml_file, provinsi, klasifikasi, sub_klasifikasi, lembaga_peradilan)


    


