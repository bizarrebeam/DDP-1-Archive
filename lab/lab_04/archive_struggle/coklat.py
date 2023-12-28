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
            lines = file.readlines()

            if len(lines) <= 1:
                print("Ups, the input file does not exist.")
                return 
            
            for index, line in enumerate(lines, start = 1):
                content = line.strip().split('\t')
                no, smartphone, price, screensize, ram = index, content[0], content[1], content[2], content[3]
                print("| {: <2} | {: <25} | {: <8} | {: <10} | {: <3} |".format(no, smartphone, price, screensize, ram))
            
    except FileNotFoundError:
        print("Ups, the input file does not exist.")

# Function to search for a specific substring, case insensitive.
def search_phone(filename: str, keyword: str):
    try:
        with open(filename, "r") as file:
            print_headers()
            lines = file.readlines()
            matched = False

            for index, line in enumerate(lines, start = 1):
                content = line.strip().split('\t')
                smartphone = content[0]

                if keyword.lower() in smartphone.lower():
                    matched = True
                    no, price, screensize, ram = index, content[1], content[2], content[3]
                    print("| {: <2} | {: <25} | {: <8} | {: <10} | {: <3} |".format(no, smartphone, price, screensize, ram))

            if not matched:
                print("Ups, no matching search for {}".format(keyword))
    
    except FileNotFoundError:
        print("Ups, the input file does not exist.")

# Function to get descriptive statistics for a specific column.
def desc_stat(filename: str, column: int):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            if column < 0 or column >= len(lines[0].strip().split('\t')):
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
                print("Rata - rata: {:.2f}".format(average_stat))

                rows = len(stat_calculated)
                collumns = len(lines[0].strip().split('\t'))

                print("The size of data for the search result: {} x {}".format(rows, collumns))
            
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

    