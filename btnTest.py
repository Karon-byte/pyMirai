from tkinter import *
from tkinter import ttk
class Buttons:
    def __init__(self,text,root):
        self.text=text
        self.root=root

    def makebtn(self):
        return ttk.Button(self.root,text=self.text,padding=20)