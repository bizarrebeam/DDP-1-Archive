import tkinter as tk
from tkinter import Canvas, messagebox

class BarcodeReader:
    def __init__(self, master=None):
        self.master = master
        self.master.geometry("400x400")
        self.master.title("EAN-13[by Hanifa]")

    def homepage(self):
        tk.Label(self.master, text="Save barcode to PS file [eg: EAN13.eps]:", width=50).pack()
        self.ps_file = tk.StringVar()
        self.save_ps = tk.Entry(self.master, textvariable=self.ps_file)
        self.save_ps.pack()

        tk.Label(self.master, text="Enter code (first 12 decimal digits):", width=50).pack()
        self.code_file = tk.StringVar()
        self.code_entry = tk.Entry(self.master, textvariable=self.code_file)
        self.code_entry.pack()
        self.code_entry.bind("<Return>", self.cek_code)

        self.canvas = Canvas(self.master, width=400, height=500, bg="white")
        self.canvas.pack()
    
    def set_text(self):
        self.ps_file.set("")
        self.code_file.set("")
    
    def cek_code(self, event=None):
        self.codes = self.code_file.get()

        try:
            if int(self.codes):
                pass
            else:
                raise ValueError
            
            if len(self.codes) == 12:
                pass
            else:
                raise IndexError
            
            self.cek_filename()
            
        except ValueError:
            messagebox.showerror("Wrong Input!", "Code only accept integers value!")

        except IndexError:
            messagebox.showerror("Wrong Input!", "Length of code must 12")

    def cek_filename(self):
        file = self.ps_file.get()
        print(file[-4:] == ".eps")

        try:
            if file[-4:] == ".eps":
                print("p")
            else:
                raise ImportError
            
            try:
                if open(file, "r"):
                    raise FileExistsError
            
            except FileNotFoundError:
                    barcode = Barcode(self.codes)
                    self.display_custom_barcode_v2(barcode.get_bits(), barcode.get_code())

                    self.__display.update()
                    self.__display.postscript(file = self.get_filename(), colormode = "color")

        except FileExistsError:
            messagebox.showerror("File Exists Error!", "File Exists. Program will not continue to save file!")
            barcode = Barcode(self.codes)
            self.display_custom_barcode_v2(barcode.get_bits(), barcode.get_code())
        
        except ImportError:
            messagebox.showerror("Wrong Input!", "Please enter correct postscript input file!")
            self.set_text()

    def display_custom_barcode_v2(self, bits, code):
        self.canvas.delete("all")
        self.canvas.create_text(200, 50, fill='purple', font='* 18 bold', text='Custom Barcode v2:')

        # Mencetak barcode
        for i, bit in enumerate(bits):
            x1, y1, x2, y2 = 57 + i * 3, 70, 60 + i * 3, 235
            if bit == '1' and (i <= 2 or (45 <= i <= 49) or (92 <= i <= 94)):
                self.canvas.create_rectangle((x1, y1, x2, y2), fill='orange', outline='orange', width=0)
            else:
                self.canvas.create_rectangle((x1, y1, x2, y2), fill='gray', width=0)

        # Mencetak digit code dan checksum
        self.canvas.create_text(46, 245, font='* 16 bold', text=code[0], fill="black")
        for i in range(1, 13):
            x = 58 + i * 21 if 1 <= i <= 6 else 70 + i * 21
            self.canvas.create_text(x, 245, font='* 16 bold', text=f'{code[i]}', fill="black")

        self.canvas.create_text(200, 275, fill='#4e9a06', font='* 16 bold', text=f'New Check Digit: {code[-1]}')

class EAN13_Specs:
    SIDE_GUARD = '101'
    MIDDLE_GUARD = '01010'

    ENCODING = {
        '0': 'llllllrrrrrr',
        '1': 'llglggrrrrrr',
        '2': 'llgglgrrrrrr',
        '3': 'llggglrrrrrr',
        '4': 'lgllggrrrrrr',
        '5': 'lggllgrrrrrr',
        '6': 'lgggllrrrrrr',
        '7': 'lglglgrrrrrr',
        '8': 'lglgglrrrrrr',
        '9': 'lgglglrrrrrr'
    }

    __CODES = {
        'l': {
            '0': '0001101',
            '1': '0011001',
            '2': '0010011',
            '3': '0111101',
            '4': '0100011',
            '5': '0110001',
            '6': '0101111',
            '7': '0111011',
            '8': '0110111',
            '9': '0001011'
        },
        'g': {
            '0': '0100111',
            '1': '0110011',
            '2': '0011011',
            '3': '0100001',
            '4': '0011101',
            '5': '0111001',
            '6': '0000101',
            '7': '0010001',
            '8': '0001001',
            '9': '0010111'
        },
        'r': {
            '0': '1100010',
            '1': '1000110',
            '2': '1101100',
            '3': '1001000',
            '4': '1100100',
            '5': '1001100',
            '6': '1010010',
            '7': '1000100',
            '8': '1011000',
            '9': '1000010'
        }
    }

    def get_bit(self, code, number):
        if code in self.__CODES and number in self.__CODES[code]:
            return self.__CODES[code][number]
        else:
            raise SyntaxError("Invalid code or number.")
    def get_checksum(self, codes):        
        digit_genap = [x for x in codes[1:12:2]]
        total_digit_genap = 0
        for i in range(len(digit_genap)):
            total_digit_genap += int(digit_genap[i])

        digit_ganjil = [x for x in codes[0:12:2]]
        total_digit_ganjil = 0
        for i in range(len(digit_ganjil)):
            total_digit_ganjil += int(digit_ganjil[i])
        
        sum_digit = (total_digit_genap*3) + total_digit_ganjil
        sum_digit = sum_digit % 10
        if sum_digit!=0:
            check_digit = 10-sum_digit
        else:
            check_digit = sum_digit
        return str(check_digit)

class Barcode(EAN13_Specs):
    def __init__(self, code):
        super().__init__()
        print(type(code))
        self.__bits = self.generate_bits(code)
        self.__code = code + self.get_checksum(code)

    def generate_bits(self, code):
        first_part = code[0]
        other_part = code[1:]
        other_part += self.get_checksum(code)

        encoding = self.ENCODING[first_part]
        bits = self.SIDE_GUARD
        for i in range(12):
            if i == 6:
                bits += self.MIDDLE_GUARD
            bits += self.get_bit(encoding[i], other_part[i])
        bits += self.SIDE_GUARD

        return bits

    def get_code(self):
        return self.__code
    
    def get_bits(self):
        return self.__bits



def main():
    root = tk.Tk()  # Create an instance of Tk()
    x = BarcodeReader(root)  # Pass root as master
    x.homepage()  # Call homepage to create UI elements
    root.mainloop()

if __name__ == '__main__':
    main()
