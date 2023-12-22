from tkinter import *
from tkinter import ttk


class Menubar(ttk.Frame):
    def __init__(self, rootWindow, window):
        self.rootWindow = rootWindow
        self.window = window

    def createMenubar(self, background, foreground, activebg, activefg):
        # config for overall menubar
        self.menubar = Menu(
            self.rootWindow,
            background=background,
            foreground=foreground,
            activebackground=activebg,
            activeforeground=activefg,
        )

        # add cascades
        self.createFileCasc(background, foreground)
        self.createEditCasc(background, foreground)
        self.createViewCasc(background, foreground)

        # adding menubar to rootWindow config
        self.rootWindow.config(menu=self.menubar)

    def createFileCasc(self, background, foreground):
        # config for first cascade
        file = Menu(
            self.menubar, tearoff=0, background=background, foreground=foreground
        )
        # first cascade

        file.add_command(label="New", command=lambda: self.window.openNewFile())  #
        file.add_command(label="Open", command=lambda: self.window.openFile())  #
        file.add_command(label="Save", command=lambda: self.window.saveFile())  #
        file.add_command(label="Save as", command=lambda: self.window.saveAsFile())  #
        file.add_separator()  #
        file.add_command(
            label="Exit", command=self.rootWindow.quit, accelerator="CTRL-Q"
        )  #

        # adding all file commands to cascade
        self.menubar.add_cascade(label="File", menu=file)

    def createEditCasc(self, background, foreground):
        edit = Menu(
            self.menubar, tearoff=0, background=background, foreground=foreground
        )
        edit.add_command(
            label="Copy",
            accelerator="Ctrl+C",
            command=lambda: self.window.textBox.event_generate("<<Copy>>"),
        )
        edit.add_command(
            label="Paste",
            accelerator="Ctrl+V",
            command=lambda: self.window.textBox.event_generate("<<Paste>>"),
        )
        edit.add_command(
            label="Cut",
            accelerator="Ctrl+X",
            command=lambda: self.window.textBox.event_generate("<<Cut>>"),
        )

        self.menubar.add_cascade(label="Edit", menu=edit)

    def createViewCasc(self, background, foreground):
        # config for view cascade
        view = Menu(
            self.menubar, tearoff=0, background=background, foreground=foreground
        )
        view.add_command(
            label="Increase font", command=lambda: self.window.changeFont(1)
        )
        view.add_command(
            label="Decrease font", command=lambda: self.window.changeFont(0)
        )
        # file.add_separator()

        self.menubar.add_cascade(label="View", menu=view)
