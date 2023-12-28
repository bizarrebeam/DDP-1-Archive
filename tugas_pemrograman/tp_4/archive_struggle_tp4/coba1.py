from tkinter import *  # impor semuanya di modul tkinter
from tkinter import messagebox


class MyFirstGUI:

    def __init__(self, master, bar):
        self.master = master
        master.title("EAN-13")
        master.geometry('500x500')

        self.bar = bar

    def click(self):
        bc = self.bar
        bcd = bc.get()
        cekdig = 0
        mSampingJudul = 230
        mSampingBc = 50
        mSamping = 50
        mAtasJudul = 50
        mAtasBc = mAtasJudul + 70
        warna = ['white', 'black']
        barcode = []
        firstg = ''
        jarak = 100

        ean_first = {'0': 'LLLLLL', '1': 'LLGLGG', '2': 'LLGGLG',
                     '3': 'LLGGGL', '4': 'LGLLGG', '5': 'LGGLLG', '6': 'LGGGLL', '7': 'LGLGLG',
                     '8': 'LGLGGL', '9': 'LGGLGL'}

        lcode = {'0': '0001101', '1': '0011001', '2': '0010011', '3': '0111101', '4': '0100011', '5': '0110001',
                 '6': '0101111', '7': '0111011', '8': '0110111', '9': '0001011'}

        gcode = {'0': '0100111', '1': '0110011', '2': '0011011', '3': '0100001', '4': '0011101', '5': '0111001',
                 '6': '0000101', '7': '0010001', '8': '0001001', '9': '0010111'}

        rcode = {'0': '1110010', '1': '1100110', '2': '1101100', '3': '1000010', '4': '1011100', '5': '1001110',
                 '6': '1010000', '7': '1000100', '8': '1001000', '9': '1110100'}

        dig_enc = {0: [3, 2, 1, 1], 1: [2, 2, 2, 1], 2: [2, 1, 2, 2], 3: [1, 4, 1, 1], 4: [
            1, 1, 3, 2], 5: [1, 2, 3, 1], 6: [1, 1, 1, 4], 7: [1, 3, 1, 2], 8: [1, 2, 1, 3],
            9: [3, 1, 1, 2]}  # unused doodoo code

        if (len(bcd) == 12):

            self.canvas = Canvas(self.master, width=450,
                                 height=450, bg="white")
            cnv = self.canvas
            cnv.grid(column=1, row=2, columnspan=4)

            # bikin garisnya

            for i in range(len(bcd)):
                if (i % 2 != 0):
                    cekdig += int(bcd[i])*3
                else:
                    cekdig += int(bcd[i])

            cekdig = 10 - (cekdig % 10)
            bcnum = bcd + str(cekdig)
            print(bcnum)

            self.canvas.create_text(
                mSampingJudul, mAtasJudul, fill="black", font="Arial 16 bold", text="EAN-13 Barcode:")

            # bikin barcode FIRST group
            firstg = ean_first[bcnum[0]]

            numcodef = bcnum[1:]
            numcodel = bcnum[1:] + str(cekdig)
            print("FirstG: ", firstg, "Code Num: ", numcodef)

            for n in range(len(firstg)):

                    # kalo itunya L
                for x in range(len(numcodef)//2):
                    if (firstg[n] == 'L') and (x == n):
                        for keyl, valuel in lcode.items():
                            if keyl in numcodef[x]:
                                print("VALUE L:", valuel)
                                barcode.append(valuel)

                    elif(firstg[n] == 'G') and (x == n):
                        # kalo digitnya G
                        for keyg, valueg in gcode.items():
                            if keyg in numcodef[x]:
                                print("VALUE G:", valueg)
                                barcode.append(valueg)

                # bikin barcode LAST group
            for i in range(len(numcodel)//2, len(numcodel)-1):
                for key, value in rcode.items():
                    if key in numcodel[i]:
                        # masukin ke list barcode
                        barcode.append(value)
                        print(barcode)

            barcode = ''.join(barcode)  # acuan penggambaran

            # MENGGAMBAR GARIS PEMBATAS AWAL BARCODE
            u = 0
            for grsawal in range(2):
                u += 6
                self.canvas.create_line(
                    85 + u, 100,  85 + u, 330, width=3, fill='blue'
                )

            # MENGGAMBAR BARCODE GROUP PERTAMA
            for gbrfirst in range(len(barcode)//2):

                self.canvas.create_line(
                    jarak, 100,  jarak, 300, width=3, fill=warna[int(barcode[gbrfirst])]
                )
                jarak += 3

            # MENGGAMBAR GARIS TENGAH BARCODE
            jarak += 3
            for grstengah in range(2):

                self.canvas.create_line(
                    jarak, 100,  jarak, 330, width=3, fill='blue'

                )
                jarak += 6

            jarak -= 3

            # MENGGAMBAR BARCODE GROUP AKHIR
            for gbrlast in range(len(barcode)//2, len(barcode)-1):
                jarak += 3
                self.canvas.create_line(
                    jarak, 100,  jarak, 300, width=3, fill=warna[int(barcode[gbrlast])]
                )

            # MENGGAMBAR GARIS PEMBATAS AKHIR BARCODE
            u = 0
            for grsakhir in range(2):
                jarak += 6
                self.canvas.create_line(
                    jarak, 100,  jarak, 330, width=3, fill='blue'
                )

            # nomor barcode
            self.canvas.create_text(
                100, 350, fill="black", font="Arial 16 bold", text=bcnum)

            # nomor cek digit
            self.canvas.create_text(
                100, 366, fill="orange", font="Arial 16 bold", text=("Check Digit: ", cekdig))


root = Tk()


label = Label(
    root, text="Enter Code: ")
label.grid(column=0, row=0, columnspan=2)

barcodenum = Entry(root, width=50)
barcodenum.grid(row=0, column=2, columnspan=2)

my_gui = MyFirstGUI(root, barcodenum)

generate = Button(root, text="Generate", width=10, command=my_gui.click)
generate.grid(column=4, row=0)


root.mainloop()