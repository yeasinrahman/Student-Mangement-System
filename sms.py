from tkinter import *
from tkinter import ttk
import pymysql 

win=Tk()
win.title("student management system")
win.geometry("1350x700+0+0")

title=Label(win,text="Student Management System",font=("times new roman",40,"bold"),bg='black',fg='white',bd=10,relief=GROOVE)
title.pack(fill=X)
frame1=Frame(win,bd=4,relief=RIDGE,bg='#2C3539')
frame1.place(x=30,y=100,width=450,height=560)

# variable
Roll_var=StringVar()
Name_var=StringVar()
Email_var=StringVar()
Gender_var=StringVar()
Contact_var=StringVar()
Dob_var=StringVar()
sby=StringVar()
s=StringVar()
# ?function
def add_():
    con=pymysql.connect(host="localhost",user='root',password='',database='stm')
    cur=con.cursor()
    cur.execute("insert into stu values(%s,%s,%s,%s,%s,%s,%s)",(Roll_var.get(),
    Name_var.get(),
    Email_var.get(),
    Gender_var.get(),
    Contact_var.get(),
    Dob_var.get(),
    title8_f.get('1.0',END) 
    ))
    con.commit()
    showdata()
    clear_()
    
    con.close()
    # print(Roll_var.get(),
    # Name_var.get(),
    # Email_var.get(),
    # Gender_var,
    # Contact_var,
    # Dob_var)
def showdata():
    con=pymysql.connect(host="localhost",user='root',password='',database='stm')
    cur=con.cursor()
    cur.execute("select * from stu")
    row=cur.fetchall()
    if len(row)!=0:
        stable.delete(*stable.get_children())
        for r in row:
            stable.insert('',END,values=r)
        con.commit()
    con.close()
def clear_():
    Roll_var.set(''),
    Name_var.set(''),
    Email_var.set(''),
    Gender_var.set(''),
    Contact_var.set(''),
    Dob_var.set(''),
    title8_f.delete('1.0',END) 
    
def info(even):
    row=stable.focus()
    content=stable.item(row)
    row1=content['values']
    # print(row)
    # print(row1)
    Roll_var.set(row1[0])
    Name_var.set(row1[1])
    Email_var.set(row1[2])
    Gender_var.set(row1[3])
    Contact_var.set(row1[4])
    Dob_var.set(row1[5])
    title8_f.delete('1.0',END) 
    title8_f.insert(END,row1[6]) 

def update_():
    con=pymysql.connect(host="localhost",user='root',password='',database='stm')
    cur=con.cursor()
    cur.execute("update  stu set name=%s,email=%s,gender=%s,contact=%s,Dob=%s,adress=%s where Roll=%s",(
    Name_var.get(),
    Email_var.get(),
    Gender_var.get(),
    Contact_var.get(),
    Dob_var.get(),
    title8_f.get('1.0',END),
    Roll_var.get()
    ))
    con.commit()
    showdata()
    clear_()
    
    con.close()
    # a
# Full texts	
# Roll
# name
# email
# gender
# contact
# Dob
# adress
# sql = "UPDATE customers SET address = %s WHERE address = %s"
# val = ("Valley 345", "Canyon 123")

def delete_():
    con=pymysql.connect(host="localhost",user='root',password='',database='stm')
    cur=con.cursor()
    cur.execute("delete from stu where Roll=%s",Roll_var.get())
    con.commit()
    showdata()
    clear_()
    
    con.close()



def search_():
    con=pymysql.connect(host="localhost",user='root',password='',database='stm')
    cur=con.cursor()
    cur.execute(f"SELECT * FROM stu WHERE {str(sby.get())}={str(s.get())}")
    row=cur.fetchall()
    if len(row)!=0:
        stable.delete(*stable.get_children())
        for r in row:
            stable.insert('',END,values=r)
        con.commit()
    con.close()


   

# ?part 1?
title1=Label(frame1,text='Manage student',font=("times new roman",30,'bold'),bg="#2C3539",fg='white')
title1.grid(row=0,column=2)

title2=Label(frame1,text='Roll Number',font=("times new roman",15,'bold'),bg="#2C3539",fg='white')
title2.grid(row=4,column=0)
title2_f=Entry(frame1,font=("times new roman",15,'bold'),bg="white",fg='black',bd=5,relief=GROOVE,textvariable=Roll_var)
title2_f.grid(row=4,column=2,pady=10)

title3=Label(frame1,text='Name',font=("times new roman",15,'bold'),bg="#2C3539",fg='white')
title3.grid(row=8,column=0)
title3_f=Entry(frame1,font=("times new roman",15,'bold'),bg="white",fg='black',bd=5,relief=GROOVE,textvariable=Name_var)
title3_f.grid(row=8,column=2,pady=10)

title4=Label(frame1,text='Email',font=("times new roman",15,'bold'),bg="#2C3539",fg='white')
title4.grid(row=12,column=0)
title4_f=Entry(frame1,font=("times new roman",15,'bold'),bg="white",fg='black',bd=5,relief=GROOVE,textvariable=Email_var)
title4_f.grid(row=12,column=2,pady=10)

title5=Label(frame1,text='Gender',font=("times new roman",15,'bold'),bg="#2C3539",fg='white')
title5.grid(row=16,column=0)
title5_f=ttk.Combobox(frame1,font=("times new roman",15,'bold'),width=19,state='readonly',textvariable=Gender_var)
title5_f['values']=['Male','Female','Other']
title5_f.grid(row=16,column=2,pady=10)



title6=Label(frame1,text='Contact',font=("times new roman",15,'bold'),bg="#2C3539",fg='white')
title6.grid(row=17,column=0)
title6_f=Entry(frame1,font=("times new roman",15,'bold'),bg="white",fg='black',bd=5,relief=GROOVE,textvariable=Contact_var)
title6_f.grid(row=17,column=2,pady=10)

title7=Label(frame1,text='D.O.B',font=("times new roman",15,'bold'),bg="#2C3539",fg='white')
title7.grid(row=18,column=0)
title7_f=Entry(frame1,font=("times new roman",15,'bold'),bg="white",fg='black',bd=5,relief=GROOVE,textvariable=Dob_var)
title7_f.grid(row=18,column=2,pady=10)

title8=Label(frame1,text='Adress',font=("times new roman",15,'bold'),bg="#2C3539",fg='white')
title8.grid(row=19,column=0)
title8_f=Text(frame1,font=("times new roman",15,'bold'),bg="white",fg='black',bd=5,relief=GROOVE,width=19,height=2)
title8_f.grid(row=19,column=2,pady=10)

button=Button(frame1,text='Add',cursor="hand2",font=("times new roman", 15 ,'bold'),bg='grey',fg='white',width=5,command=add_)
button.grid(row=20,column=0,pady=5)

button1=Button(frame1,text='Delete',cursor="hand2",font=("times new roman", 15 ,'bold'),bg='grey',fg='white',width=5,command=delete_)
button1.grid(row=20,column=2,pady=5)

button2=Button(frame1,text='Update',cursor="hand2",font=("times new roman", 15 ,'bold'),bg='grey',fg='white',width=5,command=update_)
button2.grid(row=21,column=0,pady=3)

button3=Button(frame1,text='Clear',cursor="hand2",font=("times new roman", 15,'bold'),bg='grey',fg='white',width=5,command=clear_)
button3.grid(row=21,column=2,pady=3)



frame2=Frame(win,bd=4,relief=RIDGE,bg='#2C3539')
frame2.place(x=600,y=100,width=700,height=560)

title9=Label(frame2,text='Search By',font=("times new roman",15,'bold'),bg="#2C3539",fg='white')
title9.grid(row=0,column=0,padx=3)
title9_f=ttk.Combobox(frame2,font=("times new roman",15,'bold'),state='readonly',width=10,textvariable=sby)
title9_f['values']=['Roll','contact','name']
title9_f.grid(row=0,column=1,pady=10,padx=3)

button4=Button(frame2,text='Serach',cursor="hand2",font=("times new roman", 13,'bold'),bg='grey',fg='white',width=5,command=search_)
button4.grid(row=0,column=2,pady=10,padx=30)
title10_f=Entry(frame2,font=("times new roman",12,'bold'),bg="white",fg='black',bd=5,relief=GROOVE,width=16,textvariable=s)
title10_f.grid(row=0,column=3,pady=10)

button5=Button(frame2,text='Show All',cursor="hand2",font=("times new roman", 13,'bold'),bg='grey',fg='white',width=16)
# button5.grid(row=0,column=4,pady=10,padx=3)
button5.place(x=90,y=500)

# table frame
frame3=Frame(frame2,bd=4,relief=RIDGE,bg='white')
frame3.place(x=90,y=70,width=500,height=420)

scroll_x=Scrollbar(frame3,orient=HORIZONTAL)
scroll_y=Scrollbar(frame3,orient=VERTICAL)

stable=ttk.Treeview(frame3,column=('Roll','Name','Email','Gender','Contact','D.O.B','Adress'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=stable.xview)
scroll_y.config(command=stable.yview)
stable.heading('Roll',text='Roll no')
stable.heading('Name',text='SName')
stable.heading('Email',text='SEmail')
stable.heading('Gender',text='SGender')
stable.heading('Contact',text='SContact')
stable.heading('D.O.B',text='D.O.B')
stable.heading('Adress',text='SAdress')
stable['show']='headings'

stable.column('Roll',width=100)
stable.column('Name',width=100)
stable.column('Email',width=100)
stable.column('Gender',width=100)
stable.column('Contact',width=100)
stable.column('D.O.B',width=100)
stable.column('Adress',width=100)

stable.pack(expand=1,fill=BOTH)
showdata()
stable.bind('<ButtonRelease-1>',info)
win.mainloop()