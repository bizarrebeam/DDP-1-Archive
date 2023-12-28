import sys

# Function to display the header of the table
def print_headers():
    print("| {: <2} | {: <25} | {: <8} | {: <10} | {: <3} |".format(
        "No", "Smartphone", "Price", "Screensize", "RAM"))
    print("================================================================")

# Function to display the table for the entire text document
def print_table(txtfile: str):
    try:    # Attempt to open the file
        with open(txtfile, "r") as file:
            print_headers()
            lines = file.readlines()
            
            if len(lines) <= 1: # Making sure it opens the right txt file 
                print("Ups, the input file does not exist.")
                return 
            
            # Numbering each data in the txt file to adjust table formatting
            for index, line in enumerate(lines, start = 1):

                # Get the file's content so it readable to the program
                content = line.strip().split('\t')

                # Print the content into the table formatting
                no, smartphone, price, screensize, ram = index, \
                    content[0], content[1], content[2], content[3]
                print("| {: <2} | {: <25} | {: <8} | {: <10} | {: <3} |".format(
                    no, smartphone, price, screensize, ram))
            
    except FileNotFoundError: # If the name of file given doesn't exist
        print("Ups, the input file does not exist.")

# Function to find and display the match search
def search_phone(txtfile: str, keyword: str):
    try: # Attempt to open the file
        with open(txtfile, "r") as file:
            
            # Print the header's for the match search table
            print_headers()

            # Attempt to search the match from the data by reading each lines
            lines = file.readlines()

            # Initialize variables needed for iterating the lines
            row_number = 1
            matched = False

            for line in lines:
                # Get the content file so it readable to the program
                content = line.strip().split('\t')
                # Get the smartphone content  
                smartphone = content[0]           

                # If the program find the match content
                if keyword.lower() in smartphone.lower():  
                    no, price, screensize, ram = row_number, content[1], \
                        content[2], content[3]
                    matched = True

                    # Add the match content into the table
                    print("| {: <2} | {: <25} | {: <8} | {: <10} | {: <3} |".format(
                        no, smartphone, price, screensize, ram))
                    row_number += 1 # Move to the next row 

            # If the program didn't find the match
            if not matched:
                print("Ups, no matching search for {}".format(keyword))
            
            # The program has successfully get all the match content
            else:
                rows = row_number - 1       # Exclude the <no> row
                columns = 4                 # Default columns are 4
                print("\nThe size of data for the search result: {} x {}".format(
                    rows, columns))

    except FileNotFoundError: # If the name of file given doesn't exist
        print("Ups, the input file does not exist.")

# Function to get descriptive statistics for a specific column
def desc_stat(txtfile: str, column: int):
    try:    # Attempt to open the file
        with open(txtfile, "r") as file:
            lines = file.readlines()

            # If the column number not valid (less or exceed the supposed format)
            if column < 0 or column >= len(lines[0].strip().split('\t')):
                print("Ups, Invalid column number.")
                return 
            
            # Initialize variables needed 
            min_stat = float("inf")         # Data compared would be smaller
            max_stat = float("-inf")        # Data compared would be greater 
            sum_stat = 0                    # Required to count the average data 
            count = 0                       # Required to track cells counted

            for line in lines:
                # Get the content file so it readable to the program
                content = line.strip().split('\t') 

                try:
                    cell_stat = float(content[column])  # Get the cell data
                    count += 1                          # Track each cell counted 
                    sum_stat += cell_stat               # Track all cells counted

                    # Determine the min and max data by comparing with initial variable
                    if cell_stat < min_stat: 
                        min_stat = cell_stat
                    if cell_stat > max_stat:
                        max_stat = cell_stat

                except ValueError: # If the cells number is invalid
                    print("Ups, invalid cell number.")
                    pass

            # Count the average statistic
            if count > 0:     
                average_stat = sum_stat / count

                # Display the descriptive statistic data
                print("Min data\t: {:.2f}".format(min_stat).expandtabs(20))
                print("Max data\t: {:.2f}".format(max_stat).expandtabs(20))
                print("The data's average\t: {:.2f}".format(average_stat). \
                      expandtabs(5))
            
    except FileNotFoundError: # If the name of file given doesn't exist
        print("Ups, the input file does not exist.")

if __name__ == '__main__':      # Run the script
    if len(sys.argv) != 4:      # Warn the user to input the right argument format
        print("Usage: python script_name.py <file_path> <search_keyword>" \
              "<column_num>")
        sys.exit(1)  

    # Assign the argument into variables needed
    file_path = sys.argv[1]
    key = sys.argv[2]
    column_num = int(sys.argv[3])

    # Call the functioned defined and display it on the terminal
    print_table(file_path)
    print()
    search_phone(file_path, key)
    print()
    desc_stat(file_path, column_num)

    