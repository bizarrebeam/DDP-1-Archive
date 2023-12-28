import tkinter as tk
import tkinter.messagebox as tkmsg
class MyBarcode(tk.Frame):

    def __init__(self, master = None) -> None:
        super().__init__(master)
        self.pack()
        self.create_widgets()
    
    def create_widgets(self):
        self.label_save_barcode = tk.Label(self, text = 'Save barcode to PS file [eg: EAN13.eps]', font = 'Times 12 bold')
        self.entry_save_barcode = tk.Entry(self)
        self.label_input_code = tk.Label(self, text = 'Enter the 12 digits of code to be barcode', font = 'Times 12 bold')
        self.entry_input_code = tk.Entry(self)
        self.canvas = tk.Canvas(self, width = 240, height = 270, bg= 'white')

        self.label_save_barcode.pack()
        self.entry_save_barcode.pack()
        self.label_input_code.pack()
        self.entry_input_code.pack()
        self.master.bind('<Return>')
        self.canvas.pack()

    def validate_input(self):
        self.canvas.delete('all')

        try:
            filename = self.label_save_barcode.get()
            barcode_num = int(self.entry_input_code.get())
            checkdigit = checkdigit(barcode_num)

            if len(barcode_num) != 12:
                tkmsg.showerror('Invalid input:(', 'Please input 12 digit number to be generated.')
            elif (filename[-3:] != ".ps") and (filename[-4:] != ".eps"):
                tkmsg.showerror('Invalid file type:(', "File must end with .ps or .eps.")
            else:
                self.generate_barcode(checkdigit)
        
        except ValueError:
            tkmsg.showerror('Invalid input:(', 'Input value is not a valid integer. Please enter an integer only.')
    
    def checkdigit(self):
        barcode_num = self.entry_input_code.get()
        checkdigit = 0

        if len(barcode_num) == 12:
            for i in range(len(barcode_num)):
                
                if i % 2 != 0:
                    checkdigit += int(barcode_num[i]) * 3
                else:
                    checkdigit += int(barcode_num[i])

            checkdigit = 10 - (checkdigit % 10)
            barcode_num = barcode_num + str(checkdigit)
            self.check_digit = checkdigit

    def generate_barcode(self):
        self.canvas.delete("all")
        barcode_num = self.entry_input_code.get()
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


