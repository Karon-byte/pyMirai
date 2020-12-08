from tkinter import *
from tkinter import ttk

btn_t=StringVar()

class Buttons:
    def __init__(self,text,root):
        self.text=text
        self.root=root

    def makebtn(self):
        return ttk.Button(self.root,text=self.text,padding=20,command=btn_t.set(btn_t.get()+self.text))