import sys

# Print table headers
def print_headers():
    print("| {: <2} | {: <25} | {: <8} | {: <10} | {: <3} |".format("No", "Smartphone", "Price", "Screensize", "RAM"))
    print("================================================================")

# Function to print the entire table content
def print_table(filename: str):
    try: 
        with open(filename, "r") as file:
            print_headers()
            line = file.readline().strip()  # Read the header line
            if not line:
                print("Ups, the input file does not exist.")
                return 
                
            index = 1
            print("| {: <2} |".format("No"), end="")
            for column in line.split('\t'):
                print(" {: <25} |".format(column), end="")
            print("\n================================================================")

            for line in file:
                content = line.strip().split('\t')
                index += 1
                print("| {: <2} |".format(index), end="")
                for item in content:
                    print(" {: <25} |".format(item), end="")
                print()
            
    except FileNotFoundError:
        print("Ups, the input file does not exist.")

# Function to search for a specific substring, case insensitive.
def search_phone(filename: str, keyword: str):
    try:
        with open(filename, "r") as file:
            print_headers()
            line = file.readline().strip()  # Read the header line
            if not line:
                print("Ups, the input file does not exist.")
                return 
            
            matched = []
            index = 1
            header = "| {: <2} |".format("No")
            for column in line.split('\t'):
                header += " {: <25} |".format(column)
            header += "\n================================================================"
            print(header)

            for line in file:
                content = line.strip().split('\t')
                smartphone = content[0]

                if keyword.lower() in smartphone.lower():
                    no, price, screensize, ram = index, content[1], content[2], content[3]
                    matched.append((no, smartphone, price, screensize, ram))
                    index += 1

            if not matched:
                print("Ups, no matching search for {}".format(keyword))
            else:
                for match in matched:
                    no, smartphone, price, screensize, ram = match
                    row = "| {: <2} | {: <25} | {: <8} | {: <10} | {: <3} |".format(no, smartphone, price, screensize, ram)
                    print(row)

                rows = len(matched)
                columns = 5
                print("\nUkuran data dari hasil pencarian: {} x {}".format(rows, columns))

    except FileNotFoundError:
        print("Ups, the input file does not exist.")

# Function to get descriptive statistics for a specific column.
def desc_stat(filename: str, column: int):
    try:
        with open(filename, "r") as file:
            line = file.readline().strip()  # Read the header line
            if not line:
                print("Ups, the input file does not exist.")
                return 
            
            lines = file.readlines()
            if column < 0 or column >= len(line.split('\t')):
                print("Invalid column number.")
                return 
            
            stat_calculated = []

            for line in lines:
                content = line.strip().split('\t')

                try:
                    cell_stat = float(content[column])
                    stat_calculated.append(cell_stat)

                except ValueError:
                    pass

            if stat_calculated:
                min_stat = min(stat_calculated)
                max_stat = max(stat_calculated)
                average_stat = sum(stat_calculated) / len(stat_calculated)

                print("Min data: {:.2f}".format(min_stat))
                print("Max data: {:.2f}".format(max_stat))
                print("Average: {:.2f}".format(average_stat))
            
            else:
                pass
    
    except FileNotFoundError:
        print("Ups, the input file does not exist.")

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python script_name.py <file_path> <search_keyword> <column_num>")
        sys.exit(1)

    file_path = sys.argv[1]
    key = sys.argv[2]
    column_num = int(sys.argv[3])

    
    print_table(file_path)

    print()

    search_phone(file_path, key)

    print()
    
    desc_stat(file_path, column_num)
