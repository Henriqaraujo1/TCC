from tkinter import *


class Right(Frame):
    '''just a frame widget with a black background'''
    def __init__(self, parent):
        Frame.__init__(self, parent, width=200, height=200)
        self.config(bg='black')


if __name__ == "__main__":
    # if this script is run, just do this:
    root = Tk()
    Right(root).pack()
    root.mainloop()