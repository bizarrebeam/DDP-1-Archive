import tkinter as tk
import tkinter.messagebox as tkmsg

# inherit the tk.frame Class
class MyBarcode(tk.Frame):

    # initialize the instance
    def __init__(self, master=None) -> None:
        super().__init__(master)                
        self.pack()
        self.create_widgets()
        self.check_digit = 0
    
    # method to create GUI main interface widgets
    def create_widgets(self):
        # main interface contains labels, entry fields, button, and barcode canvas
        self.label_save_barcode = tk.Label(
            self, text='Save your barcode into [.eps]/[.ps] file!', font='Consolas 12 bold'
            )
        self.entry_save_barcode = tk.Entry(self)

        self.label_input_code = tk.Label(
            self, text='Enter the 12 digits of code to be barcode', font='Consolas 12 bold'
            )
        self.entry_input_code = tk.Entry(self)

        self.generate_button = tk.Button(
            self, text='Generate the Barcode!', font='Consolas 10 bold', command=self.validate_input, bg='#eacdc2'
            )
        
        self.canvas = tk.Canvas(self, width=350, height=400, bg='white')

        # 'pack' organize the widgets position in order
        self.label_save_barcode.pack()
        self.entry_save_barcode.pack()
        self.label_input_code.pack()
        self.entry_input_code.pack()
        self.generate_button.pack(pady=10)  
        self.canvas.pack()
    
    # method to process generated barcode if inputs are valid
    def validate_input(self):
        self.canvas.delete('all')

        try: # get all the input
            filename = self.entry_save_barcode.get()
            barcode_num = self.entry_input_code.get()
            checkdigit = self.generate_checkdigit()

            # validate the length of number of code to be barcode
            if len(barcode_num) != 12:
                tkmsg.showerror(
                    "We can't process the length of the number :(", 'Please provide us with 12-digit number to be generated.'
                    )
            
            # validate the file's extention  
            elif not filename.endswith((".ps", ".eps")):
                tkmsg.showerror(
                    'Invalid file type :(', "File must end with .ps or .eps."
                    )
            
            # if inputs are valid, generate barcode and save it into postcript file
            else:
                self.generate_barcode(checkdigit)
                self.canvas.postscript(file=filename, colormode='color')

        # if user provides a no-digit 
        except ValueError:
            tkmsg.showerror(
                'Invalid input :(', 'Input is not an integer. Please provide us with a 12-digit number to be generated.'
                )

    # method to generate the barcode's checkdigit
    def generate_checkdigit(self):
        input_code = self.entry_input_code.get()
        checkdigit = 0

        # calculate ean 13's standard for checkdigit
        for i in range(len(input_code)):

            if i % 2 != 0:                              # even position weighing three
                checkdigit += int(input_code[i]) * 3
            else:                                       # odd position weighing 1
                checkdigit += int(input_code[i])

        # the resulting sum modulo 10 is subtracted from 10
        checkdigit = 10 - (checkdigit % 10)
        self.check_digit = checkdigit

        return checkdigit

    # method to generate barcode in according to the ean-13 encoding rules
    def generate_barcode(self, checkdigit):
        self.canvas.delete("all")
        barcode_num = self.entry_input_code.get() + str(checkdigit)
        barcode_patterns = []

        # store the defined encoding rules
        encoding_first_digit = {
            '0': 'LLLLLL', '1': 'LLGLGG',
            '2': 'LLGGLG', '3': 'LLGGGL', 
            '4': 'LGLLGG', '5': 'LGGLLG', 
            '6': 'LGGGLL', '7': 'LGLGLG',
            '8': 'LGLGGL', '9': 'LGGLGL'
        }
        
        encoding_l_code = {
            '0': '0001101', '1': '0011001', 
            '2': '0010011', '3': '0111101', 
            '4': '0100011', '5': '0110001',
            '6': '0101111', '7': '0111011', 
            '8': '0110111', '9': '0001011'
        }

        encoding_g_code = {
            '0': '0100111', '1': '0110011', 
            '2': '0011011', '3': '0100001', 
            '4': '0011101', '5': '0111001',
            '6': '0000101', '7': '0010001', 
            '8': '0001001', '9': '0010111'
        }

        encoding_r_code = {
            '0': '1110010', '1': '1100110', 
            '2': '1101100', '3': '1000010', 
            '4': '1011100', '5': '1001110',
            '6': '1010000', '7': '1000100', 
            '8': '1001000', '9': '1110100'
        }

        # get the number for the first digit, numerical part, and including calculated checkdigit
        first_digit_pattern = encoding_first_digit[barcode_num[0]]
        numerical_part = barcode_num[1:]
        numerical_part_checksum = barcode_num[1:] + str(checkdigit)

        # encode the pattern for the first digit of barcode that contain L/G 
        for i in range(len(first_digit_pattern)):

            # ean-13 barcode encoding grouping digits into pairs of group and pairs of digit 
            for j in range(len(numerical_part) // 2):
                if (first_digit_pattern[i] == 'L') and (j == i):        # check if the pattern is 'L' and indices match
                    for l_key, l_value in encoding_l_code.items():      # find the corresponding values in L dictionary
                        if l_key in numerical_part[j]:
                            barcode_patterns.append(l_value)            # then store the corresponding value as pattern
                            
                elif (first_digit_pattern[i] == 'G') and (j == i):      # check if the pattern is 'G' and indices match
                    for g_key, g_value in encoding_g_code.items():      # find the corresponding values in G dictionary
                        if g_key in numerical_part[j]:
                            barcode_patterns.append(g_value)            # then store the corresponding value as pattern    

        # encode the pattern for the checksum 
        for i in range(len(numerical_part_checksum) // 2, len(numerical_part_checksum)-1): # starts from middle (second half) up till the end 
            for key, value in encoding_r_code.items():                  # find the corresponding values in R dictionary
                if key in numerical_part_checksum[i]:
                    barcode_patterns.append(value)                      # then store the corresponding value as pattern


        barcode_patterns = ''.join(barcode_patterns)                    # concatenate the barcode patterns into a single string
        self.draw_barcode(barcode_patterns)                             # draw the barcode on canvas

    # method to draw the barcode on the canva
    def draw_barcode(self, barcode_patterns):
        self.canvas.delete("all")

        # draw the starting line at the left edge of the canvas
        offset_starting_line = 0                                        # offset: changes in coordinate, at vertical/horizontal axis
        for starting_line in range(2):                                  # create two parallel lines with a vertical offset
            offset_starting_line += 6
            self.canvas.create_line(
               30 + offset_starting_line, 55, 30 + offset_starting_line, 275, width=3, fill='#b75d69'
            )
        
        # draw the first group of the barcode (half the length of barcode patterns)
        barcode_position = 45
        barcode_colors = ['white', 'black']
        for group_first in range(len(barcode_patterns) // 2):
            self.canvas.create_line(
                barcode_position, 55, barcode_position, 245, width=3, fill=barcode_colors[int(barcode_patterns[group_first])]
            )
            barcode_position += 3

        # draw the middle lines of the barcode (separator of first and second group)
        barcode_position += 3
        for middle_line in range(2):                                   # create two parallel lines with a horizontal offset
            self.canvas.create_line(                                    
                barcode_position, 55, barcode_position, 275, width=3, fill='#b75d69'
            )
            barcode_position += 6

        # draw the last group of the barcode
        barcode_position -= 3
        for group_last in range(len(barcode_patterns) // 2, len(barcode_patterns) - 1):        # start from the midpoint of barcode_patterns
            barcode_position += 3                                                              
            self.canvas.create_line(
                barcode_position, 55, barcode_position, 245, width=3, fill=barcode_colors[int(barcode_patterns[group_last])]
            )

        # draw the ending lines of the barcode (right edge of canvas and last group barcode)
        offset_ending_line = 0
        for ending_line in range(2):                                   # create two parallel lines with vertical offset
            barcode_position += 6
            self.canvas.create_line(
                barcode_position, 55, barcode_position, 275, width=3, fill='#b75d69'
            )

        # display the barcode text with the checkdigit on canvas
        preformatted = self.entry_input_code.get() + str(self.check_digit)
        barcode_text = ' '.join(preformatted)                          

        # adding space configuration for each digit
        first_digit = barcode_text[0]
        second_group = barcode_text[1:13]
        third_group = barcode_text[14:]

        # display additional text information
        self.canvas.create_text(
            180, 35, fill='#372549', font='Arial 16 bold', text='Scan the EAN-13 Barcode!'
        )

        self.canvas.create_text(
            175, 290, fill='black', font='Courier 14 bold', text=f'{first_digit}\t{second_group}\t{third_group}'.expandtabs(2)
        )

        self.canvas.create_text(
           180, 330, fill='#774c60', font='Arial 16 bold', text=f'Check Digit: {self.check_digit}'
        )

# function to execute the main application
def main():
    myapp = MyBarcode()                                             # instance of MyBarcode class
    myapp.master.title("Your EAN-13 Barcode Generator")             # set window title, geometry, and make it non-resizable
    myapp.master.geometry('460x500')
    myapp.master.resizable(False, False)                    
    myapp.master.mainloop()                                         # start the main even loop

# run the script directly and call the main function
if __name__ == "__main__":
    main()
