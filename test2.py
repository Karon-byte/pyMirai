from tkinter import *
from tkinter import ttk
import btnTest
from btnTest import Buttons

root=Tk()
root.title("test")

tks=[]
btns=[]
opebtns=[]
btnvar=btnTest.btn_t

root_frame=ttk.Frame(root,padding=30)
frame2=ttk.Frame(root_frame,padding=30)
frame3=ttk.Frame(root_frame,padding=30)
frame4=ttk.Frame(root_frame,padding=30)
frame5=ttk.Frame(root_frame,padding=30)
opeframe=ttk.Frame(root_frame,padding=30)
lab1=ttk.Label(frame2,text="test Hello world")

f_frame=frame5
for x in range(10):
    if x == 1:
        f_frame=frame4
    elif x == 4:
        f_frame=frame3
    elif x == 7:
        f_frame=frame2
    f=Buttons(x,f_frame)
    btn=f.makebtn()
    btns.append(btn)
    

btns_add=ttk.Button(frame2,text="+",padding=20)
btns_sub=ttk.Button(frame3,text="-",padding=20)
btns_multi=ttk.Button(frame4,text="*",padding=20)
btns_div=ttk.Button(frame5,text="/",padding=20)
btns_equ=ttk.Button(frame5,text="=",padding=20)
btns_shift=ttk.Button(frame5,text="SHIFT",padding=20)
textentry=ttk.Entry(frame2,textvariable=btnvar)

opebtns.append(btns_add)
opebtns.append(btns_sub)
opebtns.append(btns_multi)
opebtns.append(btns_div)
tks.append(root_frame)
tks.append(frame2)
tks.append(frame3)
tks.append(frame4)
tks.append(frame5)
tks.append(lab1)

for item in tks:
    item.pack()

for x in range(1,10):
    btns[x].pack(side=LEFT,padx=10)
for x in opebtns:
    x.pack(side=RIGHT,padx=10)
btns_shift.pack(side=LEFT,padx=10)
btns[0].pack(side=LEFT,padx=10)
btns_equ.pack(side=LEFT,padx=10)


root.mainloop()