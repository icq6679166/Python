# encoding=UTF-8
import Tkinter
import tkFont


def func1():
    label.config(text="your choice is pixel3xl")


def func2():
    label.config(text="your choice is iphoneXSMax")

def funcX():
    if sel1.get() == 1:
        label.config(text="your choice is pixel3xl")
    elif sel1.get() ==2:
        label.config(text="your choice is iphoneXSMax")

top = Tkinter.Tk()
sel1 = Tkinter.IntVar()
sel1.set(1)
f1 = tkFont.Font(family='Noto Sans Cond', size=25)
f2 = tkFont.Font(family='Source Code Pro', size=26)
label = Tkinter.Label(top, text="your choice is:", font=f1)
radioButton1 = Tkinter.Radiobutton(top, text='Android', variable=sel1, value=1, command=funcX, font=f2)
radioButton2 = Tkinter.Radiobutton(top, text="iOS", variable=sel1, value=2, command=funcX, font=f2)
label.pack()
radioButton1.pack()
radioButton2.pack()
top.mainloop()
