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
        self.createFileCasc(background, foreground, activebg, activefg)
        self.createViewCasc(background, foreground, activebg, activefg)

        # adding menubar to rootWindow config
        self.rootWindow.config(menu=self.menubar)

    def createFileCasc(self, background, foreground, activebg, activefg):
        # config for first cascade
        file = Menu(
            self.menubar, tearoff=0, background=background, foreground=foreground
        )
        # first cascade
        file.add_command(label="New", command=lambda: self.window.openNewFile())
        file.add_command(label="Open", command=lambda: self.window.openFile())
        file.add_command(label="Save", command=lambda: self.window.saveFile())
        file.add_command(label="Save as", command=lambda: self.window.saveAsFile())
        file.add_separator()
        file.add_command(label="Exit", command=self.rootWindow.quit)

        # adding all file commands to cascade
        self.menubar.add_cascade(label="File", menu=file)

    def createViewCasc(self, background, foreground, activebg, activefg):
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

        # adding all file commands to cascade
        self.menubar.add_cascade(label="View", menu=view)
