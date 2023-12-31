import tkinter
from tkinter import *


class keymaps:
    def __init__(self, root):
        self.rootWindow = root
        self.allBinds()

    def allBinds(self):
        self.rootWindow.bind(
            "<Control-c>",
            lambda event: self.rootWindow.window.textBox.event_generate("<<Copy>>"),
        )
        self.rootWindow.bind(
            "<Control-v>",
            lambda event: self.rootWindow.window.textBox.event_generate("<<Paste>>"),
        )
        self.rootWindow.bind(
            "<Control-x>",
            lambda event: self.rootWindow.window.textBox.event_generate("<<Cut>>"),
        )
        self.rootWindow.bind("<Control-q>", lambda event: self.rootWindow.quit())
        # undo keybind is there already (in-built)
