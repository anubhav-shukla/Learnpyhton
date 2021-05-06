# python tkinter tut
# tee-kinter , tk-inter , kinter

# starter code
# way to import tkinter
# import tkinter
# from tkinter import *
import tkinter as tk
import os
from tkinter import ttk
from csv import DictWriter
win = tk.Tk()
win.title('GUI')

# create lebels 
name_lable=ttk.Label(win,text='Enter your name: ')
name_lable.grid(row=0, column=0,sticky=tk.W)


email_label=ttk.Label(win,text='Enter your email: ')
email_label.grid(row=2,column=0,sticky=tk.W)

age_label=ttk.Label(win,text='Enter your age: ')
age_label.grid(row=1,column=0,sticky=tk.W)

gender_label=ttk.Label(win,text='Select your gender: ')
gender_label.grid(row=3,column=0,sticky=tk.W)

#layout manager: pack , grid

# widgets --> label, buttons , radio buttons - tk , ttk


# create Entry box
name_var = tk.StringVar()
name_entrybox=ttk.Entry(win,width=16,textvariable=name_var)
name_entrybox.grid(row=0,column=1)
name_entrybox.focus()



age_var = tk.StringVar()
age_entrybox=ttk.Entry(win,width=16,textvariable=age_var)
age_entrybox.grid(row=2,column=1)

email_var = tk.StringVar()
email_entrybox=ttk.Entry(win,width=16,textvariable=email_var)
email_entrybox.grid(row=1,column=1)
#create combobox
gender_var = tk.StringVar() 
gender_combobox=ttk.Combobox(win , width=14,textvariable=gender_var,state='readonly')
gender_combobox['values']=('Male','Female','others')
gender_combobox.current(0)
gender_combobox.grid(row=3,column=0)

# radio button
# student , teacher
usertype=tk.StringVar()
radiobtn1 = ttk.Radiobutton(win,text='Student', value='Student',variable=usertype)
radiobtn1.grid(row=4,column=0)

radiobtn2=ttk.Radiobutton(win,text='Teacher', value='Teacher',variable=usertype)
radiobtn2.grid(row=4,column=1)

#check button
ckeckbtn_var=tk.IntVar()
checkbtn=ttk.Checkbutton(win,text='Check if you want to subscribe to our newa letter',variable=ckeckbtn_var) 
checkbtn.grid(row=5,columnspan=3)


# create button
# def action():
#     username = name_var.get()
#     userage = age_var.get()
#     user_email = email_var.get()
#     print(f'User Name is {username}  age is {user_email} email {userage}')
#     usegender=gender_var.get()
#     user_type=usertype.get()
#     if ckeckbtn_var.get()==0:
#         subscribed='NO'
#     else:
#         subscribed='Yes'   
#     print(usegender,user_type,subscribed)     
#     with open('file.txt','a') as f:
#        print(f.write(f'{username},{userage},{user_email},{usegender},{user_type},{subscribed}\n'))
#     name_entrybox.delete(0,tk.END)
#     age_entrybox.delete(0,tk.END)
#     email_entrybox.delete(0,tk.END)    
#     name_lable.configure(foreground='Blue')    
    
    # submit_button.configure(foreground='Blue')
    # print(f'User Name is {username}  age is {user_email} email {userage}')
    # print(usegender,user_type,subscribed)
def action():
    username = name_var.get()
    userage = age_var.get()
    user_email = email_var.get()
    print(f'User Name is {username}  age is {user_email} email {userage}')
    usegender=gender_var.get()
    user_type=usertype.get()
    if ckeckbtn_var.get()==0:
        subscribed='NO'
    else:
        subscribed='Yes'   
    # print(usegender,user_type,subscribed)     
    # with open('file.txt','a') as f:
    #    print(f.write(f'{username},{userage},{user_email},{usegender},{user_type},{subscribed}\n'))
#    write to csv file
    with open('file.csv','a',newline='') as f:
        dict_writer = DictWriter(f,fieldnames=['UserName','User Email address','User Age','User Gender','User Type','Subscribed'])
        if os.stat('file.csv').st_size==0:
            dict_writer.writeheader()

        dict_writer.writerow({
            'UserName': username,
            'User Email address':user_email,
            'User Age' : userage,
            'User Gender' : usegender,
            'User Type': user_type,
            'Subscribed':subscribed            
        })
    name_entrybox.delete(0,tk.END)
    age_entrybox.delete(0,tk.END)
    email_entrybox.delete(0,tk.END)    
    name_lable.configure(foreground='Blue')    
  
        
submit_button = tk.Button(win,text='Submit',command=action)
submit_button.grid(row=6,column=0)    
win.mainloop()