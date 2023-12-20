from tkinter import *
from tkinter import ttk
import menubar
import window


class Editor(ttk.Frame):
    def __init__(self, root):
        # creating rootWindow
        self.rootWindow = root
        self.window = window.Window(self.rootWindow)
        self.menubar = menubar.Menubar(self.rootWindow, self.window)

    def run(self):
        self.menubar.createMenubar("#007fff", "black", "white", "black")
        self.window.createTextBox()
        self.rootWindow.mainloop()


# starting our program
if __name__ == "__main__":
    root = Tk()
    root.title("kia Editor")
    texter = Editor(root)
    texter.run()

# TODO:
# scrollbar
# font size
# zoom
# about tab
# help ?
# SHORTCUTS
# borders / aesthetics
