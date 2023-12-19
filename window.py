from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd


class Window(ttk.Frame):
    def __init__(self, root):
        self.rootWindow = root
        self.rootWindow.geometry("900x500")

    def createTextBox(self):
        self.textBox = Text(self.rootWindow, state="normal")
        self.textBox.pack(fill="both", expand="1")

    def openFile(self):
        # opens existing files
        # TODO add error handling
        filetypes = (("text files", "*.txt"), ("All files", "*.*"))
        file = fd.askopenfile(
            title="Open Existing File", initialdir="/home/kia/", filetypes=filetypes
        )
        self.textBox.insert(0.0, file.read())

    def saveFile(self):
        pass

    def saveAsFile(self):
        pass

    def openNewFile(self):
        pass
