from tkinter import *
from tkinter import ttk


class Window(ttk.Frame):
    def __init__(self, root):
        self.rootWindow = root
        self.rootWindow.geometry("900x500")

    def createTextBox(self):
        self.textBox = Text(self.rootWindow, state="normal")
        self.textBox.place(relwidth=1.0, relheight=1.0)
        # self.textBox.pack(pady=10)
