from tkinter import *
from tkinter import ttk

root = Tk()
root.title("test5")

btn_t=StringVar()
btn_shift = False
subtexts=[]
tks=[]
btns=[]
btns_l_num=[["7","8","9"],["4","5","6"],["1","2","3"],[".","0","ans"]]
btns_l_func=[
    [
        ["CLR","CLR cmd"],["⬅","⬅cmd"],["➡","➡cmd"],["shift","shift cmd"],
    ],
    [
        ["π","π cmd"],["x^2","x^2 cmd"],["x^y","x^y cmd"],["DEL","DEL cmd"],
    ],
        ["logx","logx cmd"],["(","( cmd"],[")",") cmd"],
    ]
opebtns=[]
fpad=5
btn_pad=10

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

root_frame=ttk.Frame(root,padding=fpad)
f1=ttk.Frame(root_frame,padding=fpad)
f2=ttk.Frame(root_frame,padding=fpad)
f2_l=ttk.Frame(f2,padding=fpad)
f2_r=ttk.Frame(f2,padding=fpad)
f2_l.grid(row=0,ipadx=150,ipady=200)
f2_r.grid(row=1,ipadx=100,ipady=200)

for x in range(10):
    makebtn(x,f2_l,btns)

btns_add=ttk.Button(f2_r,text="\n+\n",padding=btn_pad,command=lambda:substext("+"))
btns_sub=ttk.Button(f2_r,text="\n-\n",padding=btn_pad,command=lambda:substext("-"))
btns_multi=ttk.Button(f2_r,text="\n*\n",padding=btn_pad,command=lambda:substext("*"))
btns_div=ttk.Button(f2_r,text="\n/\n",padding=btn_pad,command=lambda:substext("/"))
btns_equ=ttk.Button(f2_r,text="\n=\n",padding=btn_pad)
btns_shift=ttk.Button(f2_r,text="\nSHIFT\n",padding=btn_pad,command=lambda:btn_shift != btn_shift)

tks.append(root_frame)
