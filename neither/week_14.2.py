from tkinter import Canvas, Tk

'''
koordinat titik: (x1,y1 atas kiri), (x2,y2 bawah kanan)
'''
class MyCanvas:

    def __init__(self, master) -> None:
        self.master = master
        self.canvas = Canvas(master, width=1000, height=1000)

        self.canvas.create_rectangle(100, 100, 500, 500, fill='white')
        self.canvas.create_rectangle(150, 150, 250, 180, fill='black')
        self.canvas.create_rectangle(350, 150, 450, 180, fill='black')
        self.canvas.create_oval(150, 200, 250, 300, fill='blue')
        self.canvas.create_oval(350, 200, 450, 300, fill='red')
        self.canvas.create_rectangle(260, 265, 340, 350, fill='black')
        self.canvas.create_rectangle(200, 350, 400, 420, fill='black' )
        self.canvas.pack()

root = Tk()
my_canvas = MyCanvas(root)
root.mainloop()