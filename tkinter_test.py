from tkinter import *
import tkinter

# def hide_me(event):
#     event.widget.pack_forget()

# def show_err():
#     message.set('button pressed.')

# root = Tk()
# message = tkinter.StringVar()
# message.set('Not pressed.')
# print(message.__dict__)

# btn=Button(root, text="Click")
# btn.bind('<Button-1>', hide_me)
# btn.pack()
# Instruction = Label(root, text=message, font='size, 20')
# Instruction.pack()
# btn2=Button(root, text="Click too",command=show_err())
# #btn2.bind('<Button-1>', show_err(btn))
# btn2.pack()
# root.mainloop()
root=Tk()
Imacounter=0

def my_function():
	label1.config(text="intialized")



label1=Label(root,text="")
button1=Button(root,text="increase",command=my_function)
label1.pack()
button1.pack()


root.mainloop()