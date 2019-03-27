# encoding=UTF-8
import Tkinter
import tkFont


def func(scale):
    l1.config(text=str1 % int(scale))


str1 = "current value=%d"
top = Tkinter.Tk()
f1 = tkFont.Font(family='Noto Sans Cond', size=25)
f2 = tkFont.Font(family='Source Code Pro', size=16)
l1 = Tkinter.Label(top, text=str1 % 0, font=f1)
l1.pack()
s1 = Tkinter.Scale(top, label="Scale", font=f2, from_=0, to=100, showvalue=False, variable=None,
                   command=func, orient='h')
s1.pack()
top.minsize(220, 150)
top.maxsize(220, 150)
top.mainloop()
