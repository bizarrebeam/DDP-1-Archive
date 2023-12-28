import tkinter as tk
from tkinter import Canvas, Label, Entry, messagebox

class EAN13BarcodeGenerator(tk.Canvas):
    def __init__(self, master=None):
        super().__init__(master, width=800, height=600)
        self.pack()
        self.master.title("EAN-13 Barcode Generator")
        self.master.geometry("800x600")
        self.master.resizable(True, True)
        self.create_widgets()

    def create_widgets(self):
        self.label_filename = tk.Label(self, text="Save Barcode to PS file [eg: EAN13.eps]:")
        self.label_filename.grid(row=0, column=0, columnspan=2)

        self.entry_filename = tk.Entry(self)
        self.entry_filename.grid(row=0, column=2)

        self.label_enter_code = tk.Label(self, text="Enter code (first 12 decimal digits):")
        self.label_enter_code.grid(row=1, column=0, columnspan=2)

        self.entry_code = tk.Entry(self)
        self.entry_code.grid(row=1, column=2)

        self.button_generate = tk.Button(self, text="Generate Barcode", command=self.generate_barcode)
        self.button_generate.grid(row=2, column=0, columnspan=3)

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
        self.delete("all")
        self.create_text(400, 30, text=f"EAN-13 Barcode: {ean13_code}", font=("Courier", 14), anchor="center")

        # Save barcode as PostScript file
        self.postscript(file=filename + ".eps", colormode="color")

        # Generate barcode image
        self.create_barcode_image(ean13_code)

        # Display check digit
        self.create_text(400, 500, text=f"Check Digit: {check_digit}", font=("Courier", 14), anchor="center")

    
    def create_barcode_image(self, ean13_code):
        encoding_patterns = [
            "0001101", "0011001", "0010011", "0111101", "0100011",
            "0110001", "0101111", "0111011", "0110111", "0001011"
        ]

        # Draw the start pattern
        self.create_rectangle(30, 70, 90, 530, fill="black", outline="black")

        # Draw the encoded digits
        x1 = 90
        y1 = 70
        for i, digit in enumerate(ean13_code):
            if i == 0:
                patterns = [encoding_patterns[int(digit)][j] for j in range(7)]
            elif i <= 6:
                patterns = [encoding_patterns[int(digit)][j % 7] for j in range(7)]
            else:
                patterns = [encoding_patterns[int(digit)][j % 7] for j in range(7, 14)]

            for j, bit in enumerate(patterns):
                x2 = x1 + 10
                y2 = 530 if bit == "1" else 70  # Adjusted this line
                self.create_line(x1, y1, x2, y2, fill="black", width=2)

                # Move to the next position
                x1 = x2

        # Draw the end pattern
        self.create_rectangle(x1, y1, x1 + 20, 530, fill="black", outline="black")


    def calculate_check_digit(self, code):
        weights = [3, 1] * 6
        total = sum(int(digit) * weight for digit, weight in zip(code, weights))
        check_digit = (10 - (total % 10)) % 10
        return check_digit

if __name__ == "__main__":
    root = tk.Tk()
    app = EAN13BarcodeGenerator(master=root)
    root.mainloop()