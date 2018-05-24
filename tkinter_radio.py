# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 11:18:12 2017

@author: PA5027251
tkinter radio buttons

"""
from tkinter import *
import tkinter
#defining functions
def close():
    root.quit()
    root.destroy()

def radfn():
    a=v.get()
    if a ==1:
        a1=Tk()
        a1.title("Python")
        lab1=Label(a1,text="welcome to python").pack()
        




root=Tk()
root.geometry("300x200")
menu_items=tkinter.Menu(root)
menu_items.add_command(label="close",command=close)




menu_rad=tkinter.Menu()
menu_rad.add_cascade(label="File",menu=menu_items)





v=IntVar()
v.set(1)
Label(text="Choose the language",justify=LEFT).pack()


rad1=Radiobutton(text="A",padx=40,variable=v,value=1,command=radfn).pack(anchor=W)
rad2=Radiobutton(text="B",padx=40,variable=v,value=2,command=radfn).pack(anchor=W)
rad3=Radiobutton(text="C",padx=40,variable=v,value=3,indicatoron=0,command=radfn).pack(anchor=W)
rad4=Radiobutton(text="D",padx=40,variable=v,value=4,command=radfn).pack(anchor=W)

Languages=[("Python",1),("C",2),("D",3),("E",4)]
for text, val in Languages:
    Radiobutton(text=text,padx=40,variable=v,value=val,command=radfn).pack(anchor=W)
    





root.config(menu=menu_rad)
root.mainloop()
