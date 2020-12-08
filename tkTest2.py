from tkinter import *
from tkinter import ttk
from btnTest import Buttons

btns=[]

root=Tk()
root.title("Second Test")

root_frame=ttk.Frame(root,padding=30)
frame2=ttk.Frame(root_frame,width=100,height=100)
label1=ttk.Label(frame2,text="helloWorld")

for x in range(11):
    obj = Buttons(frame2,x)
    btns.append(obj.makebtn())

for x in range(11):
    btns[x].pack()

root_frame.pack()
frame2.pack()
label1.pack()

root.mainloop()