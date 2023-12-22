from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox
from tkinter.font import Font
import tkinter
from tkinter.filedialog import asksaveasfile
import tkinter.scrolledtext as st


class Window(ttk.Frame):
    def __init__(self, root):
        self.rootWindow = root
        self.rootWindow.geometry("900x500")
        self.fileName = ""
        self.filetypes = (("text files", "*.txt"), ("All files", "*.*"))

    def createTextBox(self):
        # self.textBox = Text(self.rootWindow, state="normal")
        self.currSize = 11
        self.myFont = Font(family="Arial", size=self.currSize)
        self.textBox = st.ScrolledText(
            self.rootWindow, state="normal", font=self.myFont, undo=True
        )
        self.textBox.pack(fill=tkinter.BOTH, side=tkinter.LEFT, expand=True)
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
        file = fd.askopenfile(
            title="Open Existing File",
            # initialdir="",
            filetypes=self.filetypes,
        )
        self.fileName = file.name
        self.rootWindow.title(self.fileName + " - kia Editor")
        self.textBox.insert(0.0, file.read())

    def saveFile(self):
        if self.fileName == "":
            self.saveAsFile()
        else:
            text = str(self.textBox.get(1.0, END))
            file = open(self.fileName, mode="w")
            file.write(text)
            file.close()

    def saveAsFile(self):
        file = asksaveasfile(mode="w")
        self.fileName = file.name
        if file is None:
            return
        text = str(self.textBox.get(1.0, END))
        file.write(text)
        file.close()

    def changeFont(self, upDown):
        if upDown == 1:
            # font +2
            self.currSize = self.currSize + 2
            self.myFont.configure(size=self.currSize)
        else:
            # decrease font by 2
            self.currSize = self.currSize - 2
            self.myFont.configure(size=self.currSize)
        return
