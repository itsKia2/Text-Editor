from tkinter import *
from tkinter import ttk
import menubar
import window


class Editor(ttk.Frame):
    def __init__(self, root):
        # creating rootWindow
        self.rootWindow = root
        self.rootWindow.title("Text Editor")
        self.menubar = menubar.Menubar(self.rootWindow)
        self.window = window.Window(self.rootWindow)

    def run(self):
        self.window.createWindow()
        self.menubar.createMenubar("#007fff", "black", "white", "black")
        self.rootWindow.mainloop()


# starting our program
root = Tk()
texter = Editor(root)
texter.run()
