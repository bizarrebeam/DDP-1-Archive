from tkinter import *  
from tkinter import messagebox

class MyBarcode():

    def __init__(self, master, barcode_entry) -> None:
        self.master = master
        master.title('EAN-13')
        master.geometry('500x500')
        self.barcode_entry = barcode_entry

    def generate_barcode(self):

        barcode_entry = self.barcode_entry
        barcode_text = barcode_entry.get()
        checksum = 0
        barcode_patterns = []

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

        if len(barcode_text) == 12:
            self.canvas = Canvas(self.master, width = 450, height = 450, bg = 'white')

            barcode_canvas = self.canvas
            barcode_canvas.grid(column = 1, row = 2, columnspan = 4)

            for i in range(len(barcode_text)):
                if i % 2 != 0:
                    checksum += int(barcode_text[i]) * 3
                else:
                    checksum += int(barcode_text[i])

            checksum = 10 - (checksum % 10)
            barcode_num = barcode_text + str(checksum)
            self.check_digit = checksum
            self.barcode_num = barcode_num
            print(barcode_num)

            self.canvas.create_text(130, 50, fill = 'black', font = 'Arial 16 bold', text = 'EAN-13 Barcode:' )

            first_digit_pattern = encoding_first_digit[barcode_num[0]]
            
            numerical_part = barcode_num[1:]
            numerical_part_checksum = barcode_num[1:] + str(checksum)
            print(f'First Digit Pattern: {first_digit_pattern}, Numerical Part: {numerical_part}')

            for i in range(len(first_digit_pattern)):

                for j in range(len(numerical_part) // 2):
                    
                    if (first_digit_pattern[i] == 'L') and (j == i):
                        for l_key, l_value in encoding_l_code.items():
                            if l_key in numerical_part[j]:
                                print(f'L Value: {l_value}')
                                barcode_patterns.append(l_value)

                    elif (first_digit_pattern[i] == 'G') and (j == i):
                        for g_key, g_value in encoding_g_code.items():
                            if g_key in numerical_part[j]:
                                print(f'G Value: {g_value}')
                                barcode_patterns.append(g_value)
                
            for i in range(len(numerical_part_checksum) // 2, len(numerical_part) -1 ):
                for key, value, in encoding_r_code.items():
                    if key in numerical_part_checksum[i]:
                        barcode_patterns.append(value)
                        print(barcode_patterns)

            barcode_patterns = ''.join(barcode_patterns)
            
            self.draw_barcode(barcode_patterns)

    def draw_barcode(self, barcode_patterns):
        offset_starting_line = 0
        for starting_line in range(2):
            offset_starting_line += 6
            self.canvas.create_line(
                85 + offset_starting_line, 100,  85 + offset_starting_line, 330, width=3, fill='blue'
            )
        
        barcode_position = 100
        barcode_colors = ['white', 'black']
        for group_first in range(len(barcode_patterns) // 2):
            self.canvas.create_line(
                barcode_position, 100, barcode_position, 300, width=3, fill=barcode_colors[int(barcode_patterns[group_first])]
            )
            barcode_position += 3
        
        barcode_position += 3
        for middle_line in range(2):
            self.canvas.create_line(
                barcode_position, 100, barcode_position, 330, width = 3, fill = 'blue'
            )
            barcode_position += 6
        
        barcode_position -= 3
        for group_last in range(len(barcode_patterns) // 2, len(barcode_patterns) -1):
            barcode_position += 3
            self.canvas.create_line(
                barcode_position, 100, barcode_position, 300, width=3, fill=barcode_colors[int(barcode_patterns[group_last])]
            )
        
        offset_ending_line = 0
        for ending_line in range(2):
            barcode_position += 6
            self.canvas.create_line(
                barcode_position, 100, barcode_position, 330, width=3, fill='blue'
            )

        self.canvas.create_text(
            100, 350, fill = 'black', font = 'Arial 16 bold', text = self.barcode_num
        )

        self.canvas.create_text(
            100, 366, fill = 'orange', font = 'Arial 16 bold', text = f'Check Digit: {self.check_digit}'
        )

def main():
    root = Tk()

    label = Label(root, text="Enter Code: ")
    label.grid(column=0, row=0, columnspan=2)

    barcodenum = Entry(root, width=50)
    barcodenum.grid(row=0, column=2, columnspan=2)

    my_gui = MyBarcode(root, barcodenum)

    generate = Button(root, text="Generate", width=10, command=my_gui.generate_barcode)
    generate.grid(column=4, row=0, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    main()