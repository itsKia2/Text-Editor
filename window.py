from tkinter import *
from tkinter import ttk


class Window(ttk.Frame):
    def __init__(self, root):
        self.rootWindow = root

    def createWindow(self):
        self.frame1 = ttk.Frame(self.rootWindow, padding=20)
        self.frame1.grid()
        ttk.Label(self.frame1, text="Hello World!\n").grid(column=0, row=0)
        ttk.Button(self.frame1, text="Quit", command=self.rootWindow.destroy).grid(
            column=0, row=1
        )
