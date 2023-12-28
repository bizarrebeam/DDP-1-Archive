from tkinter import *
class Penghitung:
    def __init__(self, master):
        self.master = master
        master.title("Penghitung")
        master.geometry("300x100")

        self.hitungan = 0
        self.label = Label(master, text=self.hitungan)
        self.label.pack()

        self.tambah_button = Button(master, text="Tambah", command=self.tambah, bg="#00FF00")
        self.tambah_button.pack()
        self.kurang_button = Button(master, text="Kurang", command=self.kurang, bg="#FF0000")
        self.kurang_button.pack()
        self.lipat10_button = Button(master, text="Lipat 10", command=self.lipat, bg="#0000FF")
        self.lipat10_button.pack()

    def tambah(self):
        self.hitungan += 1
        self.label['text'] = self.hitungan

    def kurang(self):
        self.hitungan -= 1
        self.label['text'] = self.hitungan

    def lipat(self):
        self.hitungan *= 10
        self.label['text'] = self.hitungan
        
root = Tk()
penghitung = Penghitung(root)
root.mainloop()