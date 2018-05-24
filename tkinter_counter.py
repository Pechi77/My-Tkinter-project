# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 17:22:46 2017

@author: PA5027251
functions: counter, colorchooser,


"""
import tkinter as tk
from tkinter import messagebox
from tkinter import colorchooser

def counter_label(label):
    counter=0
  
    def count():
        global counter
        counter +=1
        label.config(text=str(counter))
        label.after(1000,count)
    count()
def mcolor():
    res=colorchooser.askcolor()
    label2=tk.Label(text="result collor",bg=res[1]).pack()
    
root=tk.Tk()
root.title("title")
label=tk.Label(root,fg="red")
label.pack()
counter_label(label)
button=tk.Button(root,text="stop",width=40,command=mcolor)
button.pack()
root.mainloop()




