from tkinter import *
from tkinter import ttk
import menubar


class Editor(ttk.Frame):
    def __init__(self, root):
        # creating rootWindow
        self.rootWindow = root
        self.rootWindow.title("Text Editor")
        self.menubar = menubar.Menubar(self.rootWindow)

    def createWindow(self):
        self.frame1 = ttk.Frame(self.rootWindow, padding=20)
        self.frame1.grid()
        ttk.Label(self.frame1, text="Hello World!\n").grid(column=0, row=0)
        ttk.Button(self.frame1, text="Quit", command=self.rootWindow.destroy).grid(
            column=0, row=1
        )

    def run(self):
        self.createWindow()
        self.menubar.createMenubar("#007fff", "black", "white", "black")
        self.rootWindow.mainloop()


# starting our program
root = Tk()
texter = Editor(root)
texter.run()
