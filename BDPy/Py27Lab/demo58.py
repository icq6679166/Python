# encoding=UTF-8
import Tkinter
import tkFont


def func1():
    l1.config(fg='#000000', bg='#FFFFFF', text='status')


def func2(ev):
    l1.config(fg='#FF0000', bg='#00FFFF', text='enter')


def func3(ev):
    l1.config(fg='#00FF00', bg='#FF00FF', text='leave')


def func4(ev):
    l1.config(fg='#C0FFEE', bg='#002244', text='middle double click')


def func5(ev):
    l1.config(fg='#FFC0EE', bg='#220044', text='right drag')


top = Tkinter.Tk()
f1 = tkFont.Font(family='Noto Sans Cond', size=15)
f2 = tkFont.Font(family='Source Code Pro', size=16)
l1 = Tkinter.Label(top, fg='#000000', bg='#FFFFFF', text='status', font=f1)
b1 = Tkinter.Button(top, text='click', font=f2, command=func1)
b1.bind('<Leave>', func3)
b1.bind('<Enter>', func2)
b1.bind('<Double-2>', func4)
b1.bind('<B3-Motion>', func5)
l1.pack()
b1.pack()
top.mainloop()
