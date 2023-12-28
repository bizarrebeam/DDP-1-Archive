'''
Nama    = Muhammad Rifqi Adli Gumay
Kelas   = DDP 1 G
NPM     = 2106752224
'''
import tkinter as tk
import tkinter.messagebox as tkmsg
#tampung first group yang tiap index didapat dari first digit dalam tupples
tupples_first_group = ('LLLLLL','LLGLGG','LLGGLG','LLGGGL','LGLLGG','LGGLLG','LGGGLL','LGLGLG','LGLGGL','LGGLGL')
#tampung kode L dan G yang tiap indeks nya juga didapat dari first group (6 digit pertama setelah first digit)
dict_lG_code = {'L' : ('0001101','0011001','0010011','0111101','0100011','0110001','0101111','0111011','0110111','0001011'),\
                'G' : ('0100111','0110011','0011011','0100001','0011101','0111001','0000101','0010001','0001001','0010111')}
#tampung last group, karena R semua jadi tiap R code didapat dari indeks last group alias 6 bit terakhir
tupples_r_code = ('1110010','1100110','1101100','1000010','1011100','1001110','1010000','1000100','1001000','1110100')

#buat main class
class MainApp(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # TODO: lengkapi method ini
        #untuk label save nama file
        self.lbl_save_barcode = tk.Label(self, \
                                  text='Save barcode to PS file [eg: EAN13.eps]:',font="Times 12 bold")
        #untuk entry masukin nama file nanti
        self.ent_save_barcode = tk.Entry(self)
        #untuk label digit code
        self.lbl_code = tk.Label(self, \
                                  text='Enter code (first 12 decimal digits):',font="Times 12 bold")
        self.ent_code = tk.Entry(self) # entry masukin digit code
        self.canvas = tk.Canvas(self, width = 240, height = 270,bg='white') #buat canvas 
        #kenapa pack? karena saya ingin widget yang dibuat susunannya berurutan
        self.lbl_save_barcode.pack()
        self.ent_save_barcode.pack()
        self.lbl_code.pack()
        self.ent_code.pack()
        self.master.bind('<Return>', self.olah_data) # agar saat menekan enter dia bakal lsg diolah datanya
        self.canvas.pack()
    #fungsi untuk menampung code 101010100010101 dari first group
    def first_group(self,first_digit, first_group):
        tampung_bit = ''
        shift = 0
        for tampung in tupples_first_group[int(first_digit)]:
            if tampung == 'L':
                tampung_bit += dict_lG_code['L'][int(first_group[shift])]
            else:
                tampung_bit += dict_lG_code['G'][int(first_group[shift])]
            shift += 1
        return tampung_bit
    #fungsi untuk menampung code 101010100101010 dari last group
    def last_group(self,last_group):
        tampung_bit = ''
        for tampung in last_group:
            tampung_bit += tupples_r_code[int(tampung)]
        return tampung_bit
    #fungsi untuk mengolah data masukan
    def olah_data(self, event):
        #panggil string yang telah diinput di entry
        self.canvas.delete("all") #ini agar setiap sesudah ngesave (jika ada file yg dibuat sebelunya), dia akan menghapus terlebih dahulu gambar di canvas
        #variabel untuk validation name
        valid1 = '\/:*?"<>|' 
        valid2 = ['CON','PRN','AUX','NUL','COM1','COM2','COM3','COM4','COM5','COM6','COM7','COM8','COM9',\
                  'LPT1','LPT2','LPT3','LPT4','LPT5','LPT6','LPT7','LPT8','LPT9'] #reserves file names https://www.howtogeek.com/fyi/windows-10-still-wont-let-you-use-these-file-names-reserved-in-1974/
        #handle validation error
        try:
            nama_file = self.ent_save_barcode.get()
            code_digit = self.ent_code.get()
            cek_digit = self.cek_digit(code_digit)
            for kata in  nama_file:
                if kata in valid1:
                    return self.wrong_input()
            if len(code_digit) != 12:
                self.wrong_input()
            else:
                if (nama_file[-3:] != ".ps") and (nama_file[-4:] != ".eps"):
                    self.wrong_input()
                elif nama_file[:-4] in valid2 and nama_file[:-3] in valid2:
                    self.wrong_input()
                else:
                    self.create_code(cek_digit)
        except ValueError: #value eror kek misalnya digit code 1a1232131231213 dia bakal di handle 
            return self.wrong_input()
    #for makek number check digit yang nanti bakalan dipakek di digit akhir ean 13
    def cek_digit(self,code_digit):
        angka = 0
        code_digit = self.ent_code.get()
        for i in range(len(code_digit)):
            if i%2 == 1:
                angka += 3*int(code_digit[i])
            else:
                angka += int(code_digit[i])
        total = angka%10
        if total != 0:
            cek_digit = 10 - total
        else:
            cek_digit = total
        return cek_digit
    #function untuk membuat barcode 
    def create_code(self, cek_digit):
        self.canvas.delete("all")
        code_digit = self.ent_code.get()
        nama_file = self.ent_save_barcode.get()
        code_lengkap = code_digit + str(cek_digit)
        tampung_digit = self.first_group(code_lengkap[0],code_lengkap[1:7])
        self.canvas.create_rectangle(32,80,33,205,outline='blue')
        self.canvas.create_rectangle(36,80,37,205,outline='blue')
        self.canvas.create_text(22,220,text=f'{code_lengkap[0]}', font='Times 18 bold')
        x_axis = 38
        #iterable buat code first group kalo ketemu 1 dia bakal buat rectangle
        for kata in tampung_digit:
            if kata == '1':
                self.canvas.create_rectangle(x_axis,80,x_axis+1,195,outline='green')
            x_axis+=2
        self.canvas.create_text(79,220,text=f'{code_lengkap[1:7]}', font='Times 18 bold')
        self.canvas.create_rectangle(124,80,125,205,outline='blue')
        self.canvas.create_rectangle(128,80,129,205,outline='blue')
        x_axis = 133
        tampung_digit2 = self.last_group(code_lengkap[7:13])
        #iterable buat code last group kalo ketemu 1 dia bakal buat rectangle
        for kata in tampung_digit2:
            if kata == '1':
                self.canvas.create_rectangle(x_axis,80,x_axis+1,195,outline='green')
            x_axis+=2
        self.canvas.create_text(174,220,text=f'{code_lengkap[7:13]}', font='Times 18 bold')
        self.canvas.create_rectangle(220,80,221,205,outline='blue')
        self.canvas.create_rectangle(217,80,218,205,outline='blue')
        self.canvas.create_text(130,50,text='EAN-13 Barcode:', fill='black', font='Times 16 bold')
        self.canvas.create_text(130,250, text=f'Check Digit: {cek_digit}', fill='orange', font='Times 16 bold')
        self.canvas.postscript(file= nama_file,colormode='color')
    def wrong_input(self):
        tkmsg.showinfo("Wrong input!", message="Please enter correct input code.")

if __name__ == "__main__":
    myapp = MainApp()
    myapp.master.title("EAN-13 [by iqi]")
    myapp.master.geometry("300x400")
    myapp.master.resizable(0,0)
    myapp.master.mainloop()


'''
Special thanks to Kak Ahmad Naufan dah bimbing selama 1 semester ini,
Semoga lancar kuliah kedepannya dan diberikan nilai yang memuaskan.
Salam,
Rifqi
'''