from tkinter import *
import time
import functools
import os

class Application(Frame):
    pass

    def MinimizeConsole():
        pass

root = Tk()
print(type(root))
root.geometry('+1440+50')
app = Application(master=root)
Application.MinimizeConsole()
app.master.title("Remote App")
app.mainloop()
root.destroy()