# binding function to layout

from tkinter import *

root = Tk()


def printName():
    print("Hello my name is...")


button_1 = Button(root, text='Run', command=printName)
button_1.pack()

root.mainloop()
