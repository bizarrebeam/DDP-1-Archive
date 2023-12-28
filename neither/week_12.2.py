from tkinter import *
from tkinter.messagebox import showinfo

class DaftarMhs:

    daftar_mhs = []
    
    def __init__(self, master) -> None:
        self.master = master
        master.title("Daftar Mahasiswa")
        master.geometry("350x70")

        self.label = Label(master, text="Masukkan nama mhs: ")
        self.label.pack()

        self.nama = StringVar()
        self.field_nama = Entry(master, textvariable=self.nama, width=40)
        self.field_nama.pack()

        self.button = Button(master, text="Daftarkan", command = self.daftar)
        self.button.pack()

    def daftar(self):
        mhs = self.nama.get()
        DaftarMhs.daftar_mhs.append(mhs)
        showinfo(message="{} berhasil didaftarkan!\n\nDaftar mahasiswa menjadi\n{}".format(mhs, DaftarMhs.daftar_mhs))
        self.nama.set("")

root = Tk()
my_gui = DaftarMhs(root)
root.mainloop()