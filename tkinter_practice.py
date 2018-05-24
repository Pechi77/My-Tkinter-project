# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 11:20:02 2017

@author: PA5027251
Tkinter
"""
import os
import tkinter 
from tkinter import messagebox
from tkinter import filedialog
from tkinter import *
#b=tkinter.Tk()
a=tkinter.Tk()

def browse1():
    te=text_textbox1.get()
    browse1_label=tkinter.Label(a,text=te).pack()
def browse2():
    browse2_label=tkinter.Label(a,text="Brows e2 is clicked").pack()
def killme():
    res=messagebox.askyesno(title="Quit",message="Do you want to quit")
    if res==1:
        a.quit()
        a.destroy()
def fileopen():
    file1=filedialog.askopenfile()
    
    file1=file1.name
    text_textbox1.set(str(file1))
def fileopen2():
    file2=filedialog.askopenfile()
    
    file2=file2.name
    text_textbox2.set(str(file2))
def transfer():
    src=text_textbox1.get()
    des=text_textbox2.get()
    print(src)
    print(des)
    if src.strip() =="" or des.strip() == "":
        lbl_err.config(text="Please Fill data in the required fields")
    elif  not os.path.exists(src) or not os.path.exists(des):
        lbl_err.config(text="Please select a valid file/directory")
    else:
        print("coming")
        lbl_err.config(text="valid file/directory")
            


    
def counter_label(label):
    counter=0
  
    def count():
        global counter
        counter +=1
        counter_label.config(text=str(counter))
        counter_label.after(1000,count)
    count()
    

a.title("File Transfer")
a.geometry("500x600+500+100")
my_label1=tkinter.Label(a,text="welcome",fg="red",bg="yellow",font=("aerial",15,"bold")).pack()
my_label2=tkinter.Label(a,text="Source",fg="green",bg="white",font=("aerial",10,"italic")).place(x=15,y=100)
my_label3=tkinter.Label(a,text="Destination",fg="green",bg="white",font=("aerial",10,"italic")).place(x=15,y=150)
lbl_pechi=tkinter.Label(a,text="Built by Pechi with Python",fg="blue",bg="yellow",font=("aerial",10,"italic")).place(x=280,y=530)
lbl_err=Label(a,text="",fg="red",bg="yellow",font=("aerial",10,"italic"))
#my_label4=tkinter.Label(text="fourth label",fg="blue",bg="white").grid(row=2000,column=0)
text_textbox1=tkinter.StringVar()
text_textbox2=tkinter.StringVar()
textbox1=tkinter.Entry(a,textvariable=text_textbox1,width=38).place(x=150,y=100)

textbox2=tkinter.Entry(a,textvariable=text_textbox2,width=38).place(x=150,y=150)
print(textbox2)
my_button1=tkinter.Button(a,text="Browse", justify="right",highlightcolor="yellow",activeforeground="green",fg="red",bg="white",command=fileopen).place(x=400,y=100)
my_button2=tkinter.Button(a,text="Browse",fg="red",bg="white",command=fileopen2).place(x=400,y=150)
btn_transfer=tkinter.Button(a,text="Transfer files",fg="green",bg="white",command=transfer).place(x=300,y=250)
print(text_textbox1.get())

"""checkboxes"""
chk_dir=Checkbutton()

"""Adding menu"""
menu1=tkinter.Menu()

#packing objects
lbl_err.place(x=20,y=80)

main_items=tkinter.Menu()
main_items.add_command(label="Open")
main_items.add_command(label="Save",command=browse2)
main_items.add_command(label="Exit",command=killme)

summ_items=tkinter.Menu()
summ_items.add_command(label="Dashboard")
summ_items.add_command(label="Exit")


menu1.add_cascade(label="Main",menu=main_items)
menu1.add_cascade(label="summary",menu=summ_items)

label=tkinter.Label(a,fg="red").place(x=400,y=10)
#counter_label(label)
a.config(menu=menu1)
a.mainloop()
