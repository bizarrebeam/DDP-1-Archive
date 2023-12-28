import tkinter as tk
from tkinter import messagebox

class EAN13BarcodeGenerator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("EAN-13 Barcode Generator")
        self.geometry("800x600")
        self.resizable(True, True)
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self)
        frame.pack()

        self.label_filename = tk.Label(frame, text="Save Barcode to PS file [eg: EAN13.eps]:")
        self.label_filename.grid(row=0, column=0, columnspan=2)

        self.entry_filename = tk.Entry(frame)
        self.entry_filename.grid(row=0, column=2)

        self.label_enter_code = tk.Label(frame, text="Enter code (first 12 decimal digits):")
        self.label_enter_code.grid(row=1, column=0, columnspan=2)

        self.entry_code = tk.Entry(frame)
        self.entry_code.grid(row=1, column=2)

        self.button_generate = tk.Button(frame, text="Generate Barcode", command=self.generate_barcode)
        self.button_generate.grid(row=2, column=0, columnspan=3)

        self.canvas = tk.Canvas(self, width=800, height=400, bg="white")
        self.canvas.pack()

    def generate_barcode(self):
        filename = self.entry_filename.get()
        if not filename:
            messagebox.showerror("Error", "Please enter a valid filename.")
            return

        code = self.entry_code.get()
        if not code or len(code) != 12 or not code.isdigit():
            messagebox.showerror("Error", "Invalid code. Please enter 12 numeric digits.")
            return

        check_digit = self.calculate_check_digit(code)
        ean13_code = code + str(check_digit)

        # Print barcode on canvas
        self.canvas.delete("all")
        self.canvas.create_text(400, 30, text=f"EAN-13 Barcode: {ean13_code}", font=("Courier", 14), anchor="center")

        # Save barcode as PostScript file
        self.canvas.postscript(file=filename + ".eps", colormode="color")

        # Generate barcode image
        self.create_barcode_image(ean13_code)

        # Display check digit
        self.canvas.create_text(400, 500, text=f"Check Digit: {check_digit}", font=("Courier", 14), anchor="center")

    def create_barcode_image(self, ean13_code):
        l_code = {
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

        g_code = {
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

        r_code = {
            '0': '1110010',
            '1': '1100110',
            '2': '1101100',
            '3': '1000010',
            '4': '1011100',
            '5': '1001110',
            '6': '1010000',
            '7': '1000100',
            '8': '1001000',
            '9': '1110100'
        }

        # Adjust the width of the bars and spaces
        bar_width = 4
        space_width = 1

        # Draw the start pattern
        self.canvas.create_line(30, 70, 30, 530, fill="black", width=bar_width)

        # Draw the encoded digits
        for i, digit in enumerate(ean13_code):
            if i < 6:
                patterns = l_code[digit]
            elif i == 6:
                self.canvas.create_line(30 + i * 50, 70, 30 + i * 50, 530, fill="black", width=bar_width)
                patterns = g_code[digit]
            else:
                patterns = r_code[digit]

            for j, bit in enumerate(patterns):
                x1 = 30 + i * 50 + j * (bar_width + space_width)
                y1 = 70
                x2 = x1
                y2 = 530 if bit == '1' else 220

                # Draw the bars based on the pattern
                self.canvas.create_line(x1, y1, x2, y2, fill="black", width=bar_width)

        # Draw the end pattern
        self.canvas.create_line(30 + 13 * 50, 70, 30 + 13 * 50, 530, fill="black", width=bar_width)

    def calculate_check_digit(self, code):
        weights = [1, 3] * 6
        total = sum(int(digit) * weight for digit, weight in zip(code, weights))
        check_digit = (10 - (total % 10)) % 10
        return check_digit

if __name__ == "__main__":
    app = EAN13BarcodeGenerator()
    app.mainloop()
