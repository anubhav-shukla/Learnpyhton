import tkinter as tk 
from tkinter import ttk
win = tk.Tk()
from tkinter import messagebox as m_box
# label frame
label_frame = ttk.LabelFrame(win,text='Contact Details')
label_frame.grid(row=0,column=0,padx=40,pady=10)

# labels
name_label = ttk.Label(label_frame,text='Enter the name please: ', font=('Helvetica',14))
age_label = ttk.Label(label_frame,text='Enter the age please: ',font=('Helvetica',14))

# entry box variable
name_var = tk.StringVar()
age_var = tk.StringVar()

# entry boxes
name_entry = ttk.Entry(label_frame,width=36,textvariable=name_var)
age_entry = ttk.Entry(label_frame,width=36,textvariable=age_var)

# grid
name_label.grid(row=0,column=0,padx=5,pady=5,sticky=tk.W)
age_label.grid(row=0,column=1,padx=5,pady=5,sticky=tk.W)
name_entry.grid(row=1,column=0,padx=5,pady=5,sticky=tk.W)
age_entry.grid(row=1,column=1,padx=5,pady=5,sticky=tk.W)

def submit():
    #m_box.showinfo('title','content of this message box!!')
    name = name_var.get()
    age=age_var.get()
    if name=='' or age =='':
        m_box.showerror('Error,Please fill both name and age')
    else:
        print(f'{name}:{age}')
        try:
                #age ='' # valuje error
                # age ='20'
            age = int(age)
        except ValueError:
            m_box.showerror('only digits are allowed in age field ')
        else:
            if age < 18:
                m_box.showwarning('Warning','you are not 18, visit at your own risk')
submit_btn = ttk.Button(win,text='Submit',command=submit)
submit_btn.grid(row=1,columnspan=2,padx=40)
win.mainloop()