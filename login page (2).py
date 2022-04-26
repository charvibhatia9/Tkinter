import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
window=Tk()

window.title("Login")
window.geometry("500x500")
window['bg']='pink'

def login():
    UserID=entryUID.get()
    Password=entryPASS.get()

    if(UserID=="BDFT" and Password=="NSUT"):
        messagebox.showinfo("","You've been logged in successfully")
        window.destroy()
        import page1
    elif(UserID=="" and Password==""):
        messagebox.showinfo("","Please enter a UserID and Password to proceed")
        
    else:
        messagebox.showinfo("","Please enter a valid UserID and Passowrd")

global entryUID
global entryPASS

ttk.Label(window,text="Welcome to Customer database").place(x=70,y=10)
ttk.Label(window,text="UserID").place(x=70,y=50)
ttk.Label(window,text="Password").place(x=70,y=80)

entryUID=Entry(window)
entryUID.place(x=140,y=50)

entryPASS=Entry(window,show="*")
entryPASS.place(x=140,y=80)

button1=ttk.Button(window, text="Login", command=login).place(x=135,y=120)

window.mainloop()
