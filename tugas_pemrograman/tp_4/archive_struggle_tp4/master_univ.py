import tkinter.messagebox as tkmsg
from tkinter import *


# Kelas utama membuat window interface
class Main_Window:
    def __init__(self):
        self.__root = Tk()
        self.__root.geometry("420x400")
        self.__root.title("EAN-13 [by Amira Nisrina Nashita]")

        # Main Frame
        self.__main_frame = Frame(self.__root)
        self.__main_frame.pack()

        # Postscript Frame
        self.__ps_frame = Frame(self.__main_frame)
        self.__ps_frame.pack()
        Label(self.__ps_frame, text="Save barcode to PS file [eg: EAN13.eps]:").pack()
        self.__input_ps = StringVar()
        self.__field_ps = Entry(self.__ps_frame, textvariable=self.__input_ps, width=20)
        self.__field_ps.pack()

        # Code Frame
        self.__code_frame = Frame(self.__main_frame)
        self.__code_frame.pack()
        Label(self.__code_frame, text="Enter code (first 12 decimal digits):").pack()
        self.__input_code = StringVar()
        self.__field_code = Entry(self.__code_frame, textvariable=self.__input_code, width=20)
        self.__field_code.pack()

        # Canvas
        self.__display = Canvas(self.__code_frame, bg="white", height=300, width=400)
        self.__display.pack()

        self.__field_code.bind("<Return>", self.evaluate_code)

    def run(self):
        self.__root.mainloop()

    def get_code(self):
        return self.__input_code.get()

    def get_filename(self):
        return self.__input_ps.get()

    def show_error(self, title, message):
        tkmsg.showerror(title, message)

    def clear_text(self):
        self.__input_ps.set("")
        self.__input_code.set("")

    # Fungsi untuk menghandle input code dan menjalankan evaluate code
    def evaluate_code(self, *args):
        # Memastikan entry code telah terisi
        if self.get_code():
            try:
                if int(self.get_code()):
                    pass
                else:
                    raise ValueError

                if len(self.get_code()) != 12:
                    raise IndexError

                self.evaluate_filename()

            except ValueError:
                self.show_error("Wrong Input!", "Code only accept integers value!")

            except IndexError:
                self.show_error("Wrong Input!", "Length of code is not 12")

    # Fungsi untuk menghandle input nama file dan menyimpan barcode ke dalam file postscript
    def evaluate_filename(self, *args):
        try:
            if self.get_filename()[-4:] == ".eps" or self.get_filename()[-3:] == ".ps":
                pass
            else:
                raise TypeError

            try:
                if open(self.get_filename(), "r"):
                    raise FileExistsError

            except FileNotFoundError:
                barcode = Barcode(self.get_code())
                self.display_barcode(barcode.get_bits(), barcode.get_code())

                self.__display.update()
                self.__display.postscript(file=self.get_filename(), colormode="color")


        except TypeError:
            self.show_error("Wrong Input!", "Please enter correct postscript input file!")
            self.clear_text()

        except FileExistsError:
            self.show_error("File Exists Error!", "File Exists. Program will not continue to save file!")
            barcode = Barcode(self.get_code())
            self.display_barcode(barcode.get_bits(), barcode.get_code())

    def display_barcode(self, bits, code):
        self.__display.delete("all")
        self.__display.create_text(200, 50, fill='blue', font='* 18 bold', text='EAN-13 Barcode:')

        # Mencetak barcode
        for i in range(95):
            if bits[i] == '1':
                if i <= 2:
                    self.__display.create_rectangle((57 + i * 3, 70, 60 + i * 3, 235), fill='red', outline='red',
                                                    width=0)
                elif i >= 45 and i <= 49:
                    self.__display.create_rectangle((57 + i * 3, 70, 60 + i * 3, 235), fill='red', outline='red',
                                                    width=0)
                elif i >= 92 and i <= 94:
                    self.__display.create_rectangle((57 + i * 3, 70, 60 + i * 3, 235), fill='red', outline='red',
                                                    width=0)
                else:
                    self.__display.create_rectangle((57 + i * 3, 70, 60 + i * 3, 220), fill='black', width=0)

        # Mencetak digit code dan checksum
        self.__display.create_text(46, 245, font='* 16 bold', text=code[0], fill="black")
        for i in range(13):
            if i >= 1 and i <= 6:
                self.__display.create_text(58 + i * 21, 245, font='* 16 bold', text=f'{code[i]}', fill="black")
            elif i >= 7 and i <= 12:
                self.__display.create_text(70 + i * 21, 245, font='* 16 bold', text=f'{code[i]}', fill="black")

        self.__display.create_text(200, 275, fill='#008037', font='* 16 bold', text=f'Check Digit: {code[-1]}')


# Kelas untuk mendefinisikan spesifikasi EAN13
class EAN13_Specs:
    SIDE_GUARD = '101'
    MIDDLE_GUARD = '01010'

    __ENCODING = {
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

    __LCODE = {
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
    }

    __GCODE = {
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
    }

    def get_bits(self, code, number):
        if code == 'l':
            return self.__LCODE[number]
        elif code == 'g':
            return self.__GCODE[number]
        elif code == 'r':
            return self.__GCODE[number][::-1]
        else:
            raise SyntaxError

    def get_checksum(self, code):
        checksum = 0
        for i in code[0::2]:
            checksum += int(i)
        for i in code[1::2]:
            checksum += int(i) * 3

        return str((10 - checksum % 10) % 10)

    def get_encoding(self, number):
        return self.__ENCODING[number]


# Kelas untuk menggabungkan  95 bits yang telah terencode
class Barcode(EAN13_Specs):
    def __init__(self, code):
        first_part = code[0]
        other_part = code[1:]
        other_part += super().get_checksum(code)

        encoding = super().get_encoding(first_part)
        bits = ''
        bits += super().SIDE_GUARD
        for i in range(12):
            if i == 6:
                bits += super().MIDDLE_GUARD
            bits += super().get_bits(encoding[i], other_part[i])
        bits += super().SIDE_GUARD
        code += super().get_checksum(code)

        # Main_Window().display_barcode(bits,code)
        self.__bits = bits
        self.__code = code

    def get_code(self):
        return self.__code

    def get_bits(self):
        return self.__bits


def main():
    x = Main_Window()
    x.run()


# Menjalankan program
if __name__ == '__main__':
    main()