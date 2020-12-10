from tkinter import *
from tkinter import ttk
from btnTest import Buttons


root=Tk()
root.title("test")

btn_t=StringVar()
btn_shift = False
subtexts=[]

btn_pad=10
frame_pad=5

def substext(text):
    if btn_shift:
        btn =btn_t.get() + str(text)
        btn_t.set(btn)
    
    btn = btn_t.get() + str(text)
    btn_t.set(btn)

def makebtn(test,root,btn_l):
    btn_s = "\n   " + str(test) + "\nhoge"
    btn_l.append(
        ttk.Button(root,text=btn_s,padding=btn_pad,command=lambda:substext(test))
        )

tks=[]
btns=[]
opebtns=[]

frame_pad=5
root_frame=ttk.Frame(root,padding=frame_pad)
top_frame=ttk.Frame(root_frame,padding=frame_pad)
frame1=ttk.Frame(root_frame,padding=frame_pad)
frame2=ttk.Frame(root_frame,padding=frame_pad)
frame3=ttk.Frame(root_frame,padding=frame_pad)
frame4=ttk.Frame(root_frame,padding=frame_pad)
frame5=ttk.Frame(root_frame,padding=frame_pad)
ent1=ttk.Entry(top_frame,textvariable=btn_t,width=73)

f_frame=frame5
for x in range(10):
    if x == 1:
        f_frame=frame4
    elif x == 4:
        f_frame=frame3
    elif x == 7:
        f_frame=frame2
    makebtn(x,f_frame,btns)
    

btns_add=ttk.Button(frame2,text="\n+\n",padding=btn_pad,command=lambda:substext("+"))
btns_sub=ttk.Button(frame3,text="\n-\n",padding=btn_pad,command=lambda:substext("-"))
btns_multi=ttk.Button(frame4,text="\n*\n",padding=btn_pad,command=lambda:substext("*"))
btns_div=ttk.Button(frame5,text="\n/\n",padding=btn_pad,command=lambda:substext("/"))
btns_equ=ttk.Button(frame5,text="\n=\n",padding=btn_pad)
btns_shift=ttk.Button(frame5,text="\nSHIFT\n",padding=btn_pad,command=lambda:btn_shift != btn_shift)

opebtns.append(btns_add)
opebtns.append(btns_sub)
opebtns.append(btns_multi)
opebtns.append(btns_div)

tks.append(root_frame)
tks.append(top_frame)
tks.append(frame1)
tks.append(frame2)
tks.append(frame3)
tks.append(frame4)
tks.append(frame5)

btn_padx=5
btn_ipad=5
for item in tks:
    item.pack()
ent1.pack()
for x in range(1,10):
    btns[x].pack(side=LEFT,padx=btn_padx,ipadx=btn_ipad)
for x in opebtns:
    x.pack(side=RIGHT,padx=btn_padx,ipadx=btn_ipad)
btns_shift.pack(side=LEFT,padx=btn_padx,ipadx=btn_ipad)
btns[0].pack(side=LEFT,padx=btn_padx,ipadx=btn_ipad)
btns_equ.pack(side=LEFT,padx=btn_padx,ipadx=btn_ipad)


root.mainloop()