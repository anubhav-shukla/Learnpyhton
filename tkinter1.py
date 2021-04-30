# python tkinter tut
# tee-kinter , tk-inter , kinter

# starter code
# way to import tkinter
# import tkinter
# from tkinter import *
import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title('GUI')

# create levels 
name_lable=ttk.Label(win,text='Enter your name: ')
name_lable.grid(row=0, column=0,sticky=tk.W)


email_label=ttk.Label(win,text='Enter your email: ')
email_label.grid(row=2,column=0,sticky=tk.W)

age_label=ttk.Label(win,text='Enter your age: ')
age_label.grid(row=1,column=0,sticky=tk.W)

#layout manager: pack , grid

# widgets --> label, buttons , radio buttons - tk , ttk


# create Entry box
name_var = tk.StringVar()
name_entrybox=ttk.Entry(win,width=16,textvariable=name_var)
name_entrybox.grid(row=0,column=1)




age_var = tk.StringVar()
age_entrybox=ttk.Entry(win,width=16,textvariable=age_var)
age_entrybox.grid(row=2,column=1)

email_var = tk.StringVar()
email_entrybox=ttk.Entry(win,width=16,textvariable=email_var)
email_entrybox.grid(row=1,column=1)


# create button
def action():
    username = name_var.get()
    userage = age_var.get()
    user_email = email_var.get()
    print(f'User Name is{username}  age is {user_email} email{userage}')

submit_button = ttk.Button(win,text='Submit',command=action)
submit_button.grid(row=3,column=0)    
win.mainloop()