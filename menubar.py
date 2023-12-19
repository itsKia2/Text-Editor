from tkinter import *
from tkinter import ttk


class Menubar(ttk.Frame):
    def __init__(self, rootWindow):
        self.rootWindow = rootWindow

    def createFileCasc(self, background, foreground, activebg, activefg):
        # config for first cascade
        file = Menu(
            self.menubar, tearoff=0, background=background, foreground=foreground
        )
        # first cascade
        file.add_command(label="New")
        file.add_command(label="Open")
        file.add_command(label="Save")
        file.add_command(label="Save as")
        file.add_separator()
        file.add_command(label="Exit", command=self.rootWindow.quit)

        # adding all file commands to cascade
        self.menubar.add_cascade(label="File", menu=file)

    def createViewCasc(self, background, foreground, activebg, activefg):
        # config for first cascade
        view = Menu(
            self.menubar, tearoff=0, background=background, foreground=foreground
        )
        # first cascade
        # view.add_command(label="Fullscreen", command=self.toggleFullscreen())
        view.add_command(label="Filler - Fullscreen")
        view.add_command(label="Filler")
        # file.add_separator()

        # adding all file commands to cascade
        self.menubar.add_cascade(label="View", menu=view)

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
