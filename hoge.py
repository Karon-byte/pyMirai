from tkinter import *
from tkinter import ttk

root = Tk()
root.title("hoge button test")

btn_t=StringVar()
btn_t.set("hello")
mainframe=ttk.Frame(root,padding=30)
frame2=ttk.Frame(mainframe,padding=30)
ent=ttk.Entry(frame2,textvariable=btn_t)
btn1=ttk.Button(frame2,text="PUSH!",padding=20,command=lambda:btn_t.set(btn_t.get()+"world"))

mainframe.pack()
frame2.pack()
ent.pack()
btn1.pack()

root.mainloop()
