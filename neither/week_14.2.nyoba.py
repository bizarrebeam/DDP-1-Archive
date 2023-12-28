# from tkinter import *

# class MyCanvas:
    
#     def _init_(self, master):
#         self.master = master
#         self.canvas = Canvas(master, width=1000, height=1000)
#         self.canvas.create_oval(70, 70, 350, 350)
#         self.canvas.create_oval(125, 125, 175, 175, fill='black')
#         self.canvas.create_oval(225, 125, 275, 175, fill='black')
#         self.canvas.create_line(125, 250, 275, 250, width=5)
#         self.canvas.create_oval(225, 125, 275, 175, fill='black', tags='right')
#         self.canvas.create_arc(125, 225, 275, 275, extent=-180, width=5, fill='white')

# root = Tk()
# my_canvas = MyCanvas(root)
# root.mainloop()

from tkinter import Tk, Label, RAISED, Button
class Keypad:
    def __init__(self, root):
        labels = [['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
        ['*', '0', '#']]
        
        for r in range(4):
            for c in range(3):
                # create button for row r and column c
                button = Button(
                    root,
                    relief=RAISED,
                    padx=10,
                    text=labels[r][c]
                )
            # place label in row r and column c
                button.grid(row=r, column=c)
root = Tk()
keypad = Keypad(root)
root.mainloop()