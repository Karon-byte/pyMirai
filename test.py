from tkinter import *
from tkinter import ttk
from btnTest import Buttons

root=Tk()
root.title("test")

tks=[]
root_frame=ttk.Frame(root,padding=30)
frame2=ttk.Frame(root_frame,width=100,height=100)
lab1=ttk.Label(frame2,text="test, Hello world")

tks.append(root_frame)
tks.append(frame2)
tks.append(lab1)

for item in tks:
    item.pack()

root.mainloop()