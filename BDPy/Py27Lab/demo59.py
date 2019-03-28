# encoding=UTF-8
import Tkinter
import tkFont


def motion(ev):
    message1.config(text='move to[%d,%d]' % (ev.x, ev.y))


top = Tkinter.Tk()
f1 = tkFont.Font(family='Noto Sans Cond', size=25)
f2 = tkFont.Font(family='Source Code Pro', size=16)

message1 = Tkinter.Message(top, text='detect moving', padx=20, pady=20)
message1.config(bg='lightgreen', font=f1)
message1.bind('<Motion>', motion)
message1.pack()
top.minsize(400,200)
top.maxsize(400,200)
top.mainloop()

