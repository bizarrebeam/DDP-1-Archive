import tkinter as tk
import tkinter.messagebox as tkmsg

class MyBarcode(tk.Frame):

    def __init__(self, master=None) -> None:
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.check_digit = 0

    def create_widgets(self):
        self.label_save_barcode = tk.Label(self, text='Save barcode into [.eps]/[.ps] file!', font='Consolas 12 bold')
        self.entry_save_barcode = tk.Entry(self)
        self.label_input_code = tk.Label(self, text='Enter the 12 digits of code to be barcode', font='Consolas 12 bold')
        self.entry_input_code = tk.Entry(self)
        self.generate_button = tk.Button(self, text='Generate the Barcode!', font='Consolas 10 bold', command=self.validate_input, bg='#eacdc2')
        self.canvas = tk.Canvas(self, width=350, height=400, bg='white')

        self.label_save_barcode.pack()
        self.entry_save_barcode.pack()
        self.label_input_code.pack()
        self.entry_input_code.pack()
        self.generate_button.pack(pady=10)  
        self.canvas.pack()

    def validate_input(self):
        self.canvas.delete('all')

        try:
            filename = self.entry_save_barcode.get()
            barcode_num = self.entry_input_code.get()
            checkdigit = self.generate_checkdigit()

            if len(barcode_num) != 12:
                tkmsg.showerror("We can't process the length of the number :(", 'Please provide us with 12-digit number to be generated.')
            elif not filename.endswith((".ps", ".eps")):
                tkmsg.showerror('Invalid file type :(', "File must end with .ps or .eps.")
            else:
                self.generate_barcode(checkdigit)
                self.canvas.postscript(file=filename, colormode='color')

        except ValueError:
            tkmsg.showerror('Invalid input :(', 'Input is not an integer. Please provide us with a 12-digit number to be generated.')


    def generate_checkdigit(self):
        input_code = self.entry_input_code.get()
        checkdigit = 0

        for i in range(len(input_code)):

            if i % 2 != 0:
                checkdigit += int(input_code[i]) * 3
            else:
                checkdigit += int(input_code[i])

        checkdigit = 10 - (checkdigit % 10)
        self.check_digit = checkdigit

        return checkdigit

    def generate_barcode(self, checkdigit):
        self.canvas.delete("all")
        barcode_num = self.entry_input_code.get() + str(checkdigit)
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

        first_digit_pattern = encoding_first_digit[barcode_num[0]]
        numerical_part = barcode_num[1:]
        numerical_part_checksum = barcode_num[1:] + str(checkdigit)

        for i in range(len(first_digit_pattern)):

            for j in range(len(numerical_part) // 2):
                if (first_digit_pattern[i] == 'L') and (j == i):
                    for l_key, l_value in encoding_l_code.items():
                        if l_key in numerical_part[j]:
                            barcode_patterns.append(l_value)
                            
                elif (first_digit_pattern[i] == 'G') and (j == i):
                    for g_key, g_value in encoding_g_code.items():
                        if g_key in numerical_part[j]:
                            barcode_patterns.append(g_value)

        for i in range(len(numerical_part_checksum) // 2, len(numerical_part_checksum)-1):
            for key, value in encoding_r_code.items():
                if key in numerical_part_checksum[i]:
                    barcode_patterns.append(value)

        barcode_patterns = ''.join(barcode_patterns)
        self.draw_barcode(barcode_patterns)

    def draw_barcode(self, barcode_patterns):
        self.canvas.delete("all")

        # Constants
        line_width = 3
        line_fill = '#b75d69'
        text_fill = '#372549'
        check_digit_fill = '#774c60'
        start_x = 30
        start_y = 55
        spacing = 6
        barcode_height = 245
        barcode_position = 45
        barcode_colors = ['white', 'black']

        # Helper function to draw lines
        def draw_line(x1, y1, x2, y2, width, fill):
            self.canvas.create_line(x1, y1, x2, y2, width=width, fill=fill)

        # Draw starting lines
        for _ in range(2):
            start_x += spacing
            draw_line(start_x, start_y, start_x, start_y + barcode_height, line_width, line_fill)

        # Draw barcode groups
        for i in range(len(barcode_patterns) - 1):
            barcode_position += 3
            draw_line(barcode_position, start_y, barcode_position, start_y + barcode_height, line_width, barcode_colors[int(barcode_patterns[i])])

        # Draw ending lines
        for _ in range(2):
            barcode_position += spacing
            draw_line(barcode_position, start_y, barcode_position, start_y + barcode_height, line_width, line_fill)

        # Draw barcode text
        barcode_text = ' '.join(self.entry_input_code.get() + str(self.check_digit))
        first_digit, second_group, third_group = barcode_text[0], barcode_text[1:13], barcode_text[14:]

        self.canvas.create_text(180, 35, fill=text_fill, font='Arial 16 bold', text='Scan the EAN-13 Barcode!')
        self.canvas.create_text(175, 290, fill='black', font='Courier 14 bold', text=f'{first_digit}\t{second_group}\t{third_group}'.expandtabs(2))
        self.canvas.create_text(180, 330, fill=check_digit_fill, font='Arial 16 bold', text=f'Check Digit: {self.check_digit}')


def main():
    myapp = MyBarcode()
    myapp.master.title("Your EAN-13 Barcode Generator")
    myapp.master.geometry('460x500')
    myapp.master.resizable(False, False)

    myapp.master.mainloop()


if __name__ == "__main__":
    main()
