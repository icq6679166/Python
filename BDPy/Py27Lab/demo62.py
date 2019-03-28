# encoding=UTF-8
import Tkinter
import tkFont

def display(ev):
    l1.config(text=entry1.get(), fg='#FF0000')

top = Tkinter.Tk()
f1 = tkFont.Font(family='Noto Sans Cond', size=25)
f2 = tkFont.Font(family='Source Code Pro', size=26)

l1 = Tkinter.Label(top, text='input something and display', font=f1)

entry1 = Tkinter.Entry(top, font=f2)
b1 = Tkinter.Button(top, text="submit", font=f1, command=None)
b1.bind('<Button-1>',display)
entry1.bind('<Return>', display)
l1.pack()
entry1.pack()
b1.pack()
top.mainloop()
