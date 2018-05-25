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
print(type(a))









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
    lbl_err.config(text="")
def fileopen2():
    file2=filedialog.askopenfile()
    file2=file2.name
    text_textbox2.set(str(file2))
text_user=""
text_pwd=""
def transfer():

    if not user_authendicated(text_user,text_pwd):
        lbl_err.config(text="invalid user")
        return "Invalid user"
    phone_path=text_textbox1.get()
    msg_path=text_textbox2.get()
    print(phone_path)
    print(msg_path)
    phone_path_ext=os.path.splitext(phone_path)[1]
    msg_path_ext=os.path.splitext(msg_path)[1]
    if msg_path_ext != '.txt' or phone_path_ext != '.txt':
        lbl_err.config(text="Invalid file uploaded")
    if phone_path.strip() =="" or msg_path.strip() == "":
        lbl_err.config(text="Please Fill data in the required fields")
    elif  not os.path.exists(phone_path) or not os.path.exists(msg_path):
        lbl_err.config(text="Please select a valid file/directory")
    else:
        with open(phone_path,"r") as file_obj:
            phone_numbers=file_obj.readlines()
        with open(msg_path,"r") as file_obj:
            message=file_obj.read()
        if len(phone_numbers)==0:
                lbl_err.config(text="No phone numbers found")
        if len(message)==0:
                lbl_err.config(text="No messages found")
        phone_numbers=[item.strip() for item in phone_numbers]
        phone_numbers=[item[1:] if str(item[0])=="+" else item for item in phone_numbers]
        message=message.replace("\n"," ")

def user_configuration():
    newWindow=Toplevel(a)
    newWindow.title("User configuration")
    newWindow.geometry("300x200+500+100")
    user_lbl=tkinter.Label(newWindow,text="username",fg="green",bg="white",font=("aerial",10,"italic")).place(x=15,y=50)
    pwd_lbl=tkinter.Label(newWindow,text="password",fg="green",bg="white",font=("aerial",10,"italic")).place(x=15,y=100)
    text_user=tkinter.StringVar()
    text_pwd=tkinter.StringVar()
    user_Entry=tkinter.Entry(newWindow,textvariable=text_user,width=38)
    pwd_Entry=tkinter.Entry(newWindow,textvariable=text_pwd,width=38)
    save_btn=tkinter.Button(newWindow,text="Save",fg="green",bg="white",font=("aerial",10,"italic"),command=save_user_config).place(x=80,y=150)
    text_user=user_Entry.get()
    text_pwd=pwd_Entry.get()
    user_Entry.place(x=110,y=50,width=120)
    pwd_Entry.place(x=110,y=100,width=120)
def user_authendicated(text_user,text_pwd):
    if text_user=="pechi" and text_pwd=="pechi":
        return True
    else:
        return False

def save_user_config():
    text_user=user_Entry.get()
    text_pwd=pwd_Entry.get()
    print("po",text_user,text_pwd)

def counter_label(label):
    counter=0

    def count():
        global counter
        counter +=1
        counter_label.config(text=str(counter))
        counter_label.after(1000,count)
    count()


a.title("Whatsapp bot")
a.geometry("500x600+500+100")
my_label1=tkinter.Label(a,text="welcome",fg="red",bg="yellow",font=("aerial",15,"bold")).pack()
my_label2=tkinter.Label(a,text="Phone number",fg="green",bg="white",font=("aerial",10,"italic")).place(x=15,y=100)
my_label3=tkinter.Label(a,text="Message",fg="green",bg="white",font=("aerial",10,"italic")).place(x=15,y=150)
lbl_pechi=tkinter.Label(a,text="pechi.pythonanywhere.com",fg="blue",bg="yellow",font=("aerial",10,"italic")).place(x=280,y=530)
lbl_err=Label(a,text="",fg="red",bg="yellow",font=("aerial",10,"italic"))
#my_label4=tkinter.Label(text="fourth label",fg="blue",bg="white").grid(row=2000,column=0)
text_textbox1=tkinter.StringVar()
text_textbox2=tkinter.StringVar()
textbox1=tkinter.Entry(a,textvariable=text_textbox1,width=38).place(x=150,y=100)

textbox2=tkinter.Entry(a,textvariable=text_textbox2,width=38).place(x=150,y=150)
print(textbox2)
my_button1=tkinter.Button(a,text="Browse", justify="right",highlightcolor="yellow",activeforeground="green",fg="red",bg="white",command=fileopen).place(x=400,y=100)
my_button2=tkinter.Button(a,text="Browse",fg="red",bg="white",command=fileopen2).place(x=400,y=150)
btn_transfer=tkinter.Button(a,text="Send message",fg="green",bg="white",command=transfer).place(x=300,y=250)
print("pp",text_textbox1.get())

"""checkboxes"""
chk_dir=Checkbutton()

"""Adding menu"""
menu1=tkinter.Menu()

#packing objects
lbl_err.place(x=20,y=80)

main_items=tkinter.Menu()
main_items.add_command(label="config",command=user_configuration)
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
