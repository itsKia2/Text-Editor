from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox


class Window(ttk.Frame):
    def __init__(self, root):
        self.rootWindow = root
        self.rootWindow.geometry("900x500")
        self.fileName = ""

    def createTextBox(self):
        self.textBox = Text(self.rootWindow, state="normal")
        self.textBox.pack(fill="both", expand="1")

    def openNewFile(self):
        if len(self.textBox.get("1.0", "end-1c")) != 0:
            ans = messagebox.askquestion(
                title="Save File", message="Would you like to save this file"
            )
            if ans == "yes":
                self.saveFile()
                self.textBox.delete("1.0", END)
            else:
                self.textBox.delete("1.0", END)
        self.fileName = ""
        # self.textBox.delete("1.0", END)

    def openFile(self):
        # opens existing files
        # TODO add error handling
        # TODO add shortcuts
        if len(self.textBox.get("1.0", "end-1c")) != 0:
            ans = messagebox.askquestion(
                title="Save File", message="Would you like to save this file"
            )
            if ans == "yes":
                self.saveFile()
                self.textBox.delete("1.0", END)
            else:
                self.textBox.delete("1.0", END)
        filetypes = (("text files", "*.txt"), ("All files", "*.*"))
        file = fd.askopenfile(
            title="Open Existing File", initialdir="/home/kia/", filetypes=filetypes
        )
        self.fileName = file.name
        self.textBox.insert(0.0, file.read())

    def saveFile(self):
        if self.fileName == "":
            self.saveAsFile()
        else:
            print("SAVE")

    def saveAsFile(self):
        print("SAVE AS FILE")
