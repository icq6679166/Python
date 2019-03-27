# encoding=UTF-8
import Tkinter
import tkFont


counter = 0
def callback1():
    global counter
    label3.config(text='按鈕被按下了%d次' % counter)
    counter += 1

class Counter:
    def __init__(self, counter):
        self.counter = counter
c1 = Counter(0)
def callback2():
    label2.config(text='button pressed %d times'%(c1.counter))
    c1.counter += 1

top = Tkinter.Tk()
for f in tkFont.families():
    print f
f1 = tkFont.Font(family='Noto Sans Cond', size=15)
f2 = tkFont.Font(family='Source Code Pro', size=16)
f3 = tkFont.Font(family='標楷體', size=24)
label1 = Tkinter.Label(top, text='I am a label', font=f2, fg='#C0FFEE', bg='#224488', padx=10, pady=10)
label2 = Tkinter.Label(top, text="This is another label", font=f1, fg='#FFC0EE', bg="#442288", padx=0, pady=5)
label3 = Tkinter.Label(top, text=u'這是標籤', font=f3, fg='#FFEEC0', bg='#882244', padx=30, pady=10)
button1 = Tkinter.Button(top, text=u'Immutable送出', font=f3, padx=10, pady=10, command=callback1)
button2 = Tkinter.Button(top, text=u'Mutable送出', font=f3, padx=10, pady=10, fg='#FFFFFF', bg='#000000', command=callback2)

label2.pack()
label3.pack()
label1.pack()
button1.pack()
button2.pack()

top.mainloop()
