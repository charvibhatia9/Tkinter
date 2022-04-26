import sqlite3
from tkinter import *
from tkinter import ttk
window=Tk()
window['bg']='pink'

window.title('CUSTOMER INFORMATION')
window.geometry('500x630')
conn=sqlite3.connect('projectt_dbms.db')
c= conn.cursor()
"""
c.execute'''('''CREATE TABLE customer(
		customer_id integer PRIMARY KEY NOT NULL,
		first_name text NOT NULL,
		last_name text,
		phone_no integer
		
		)''')'''

c.execute("INSERT INTO customer\
      VALUES (1, 'amisha','goel',25000)");

c.execute("INSERT INTO customer\
      VALUES (2, 'kanika','yadav',258890)")
"""

def nextpg():
    window.destroy()
    import page2

def save():
    conn=sqlite3.connect('projectt_dbms.db')
    c= conn.cursor()
    record_id = delete_box.get()
    c.execute("""
    UPDATE customer SET
    customer_id= :cid,
    first_name= :first,
    last_name= :last,
    phone_no= :phone

    WHERE oid = :oid""",

    {
    "cid":cid_e.get(),
    "first":f_name_e.get(),
    "last": l_name_e.get(),
    "phone":phone_e.get(),

    "oid":record_id
    }
    )

    conn.commit()
    conn.close()
    editor.destroy()
    
def update():
    conn=sqlite3.connect('project_dbms.db')
    c= conn.cursor()
    record_id = delete_box.get()

    if delete_box.get()== "":
        print("Please Select An ID")
    else:
        global editor
        editor.title('Update Window')
        editor.geometry('450x400')
       
        
        c.execute("SELECT * FROM customer WHERE oid = " + record_id)
        records=c.fetchall()

     #global variables
        global cid_e
        global f_name_e
        global l_name_e
        global phone_e

        #text boxes
        cid_e = Entry(editor, width=30)
        cid_e.grid(row=0, column=1, padx=20)

        f_name_e = Entry(editor, width=30)
        f_name_e.grid(row=1, column=1)

        l_name_e = Entry(editor, width=30)
        l_name_e.grid(row=2, column=1)


        phone_e = Entry(editor, width=30)
        phone_e.grid(row=4, column=1)


        #Text Labels
        cid_label = ttk.Label(editor, text="Customer ID")
        cid_label.grid(row=0, column=0)

        f_name_label = Label(editor, text="First Name")
        f_name_label.grid(row=1, column=0)

        l_name_label = Label(editor, text="Last Name")
        l_name_label.grid(row=2, column=0)

    

        phone_label = Label(editor, text="Phone No.")
        phone_label.grid(row=4, column=0)

        for each in records:
            cid_e.insert(0,each[0])
            f_name_e.insert(0,each[1])
            l_name_e.insert(0,each[2])
            phone_e.insert(0,each[3])

        #save button
        save_btn = ttk.Button(editor, text="Save Record", command=save)
        save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=136)
    
    conn.commit()
    conn.close()

def delete():
    conn=sqlite3.connect('project_dbms.db')
    c= conn.cursor()
    if delete_box.get()== "":
        print("Please Select An ID")
    else:
        c.execute("DELETE from customer WHERE oid = " +delete_box.get())
    conn.commit()
    conn.close()
    delete_box.delete(0,END)

def select_id():
    conn=sqlite3.connect('project_dbms.db')
    c= conn.cursor()
    global delete_box
    delete_box= Entry(window,width=30)
    delete_box.grid(row=9,column=1)
    delete_box_label= Label(window,text="Select ID")
    delete_box_label.grid(row=9,column=0)
    #Delete Button
    delete_btn = ttk.Button(window, text="Delete Record", command=delete)
    delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

    #Update Button
    update_btn = ttk.Button(window, text="Update Record", command=update)
    update_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

    conn.commit()
    conn.close()

#submit function
def submit():
    conn=sqlite3.connect('project_dbms.db')
    c= conn.cursor()
    c.execute("INSERT INTO customer VALUES(:cid, :f_name, :l_name, :phone)",
			{
                                'cid': cid.get(),
				'f_name': f_name.get(),
				'l_name': l_name.get(),
			    
				'phone': phone.get()
			})
    
    conn.commit()
    conn.close()
    
    cid.delete(0,END)
    f_name.delete(0,END)
    l_name.delete(0,END)
    phone.delete(0,END)


#query function(show records)
def query():
    conn=sqlite3.connect('project_dbms.db')
    c= conn.cursor()
    
    c.execute('SELECT * FROM customer')#oid is the primary key assigned by
    #sqlite3(auto increment)
    records=c.fetchall()
    print(records)
    print_records=" "
    for each in records:
        print_records += str(each)+ "\n"
    query_label=Label(window,text=print_records)
    query_label.grid(row=14,column=0,columnspan=2)
    conn.commit()
    conn.close()

#text boxes
cid = Entry(window, width=30)
cid.grid(row=0, column=1, padx=20)

f_name = Entry(window, width=30)
f_name.grid(row=1, column=1)

l_name = Entry(window, width=30)
l_name.grid(row=2, column=1)

phone = Entry(window, width=30)
phone.grid(row=4, column=1)



#Text Labels
cid_label = ttk.Label(window, text="Customer ID")
cid_label.grid(row=0, column=0, pady=2,padx=2)

f_name_label = ttk.Label(window, text="First Name")
f_name_label.grid(row=1, column=0,padx=2)

l_name_label = ttk.Label(window, text="Last Name")
l_name_label.grid(row=2, column=0,pady=2,padx=2)


phone_label = ttk.Label(window, text="Phone No.")
phone_label.grid(row=4, column=0,pady=2,padx=2)


submit_btn=ttk.Button(window, text="SUBMIT",command= submit) 
submit_btn.grid(row=6,column=0,columnspan=2,pady=10, padx=10,ipadx=50)

#Show records Button
query_btn = ttk.Button(window, text="VIEW CUSTOMER DATA", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=5, padx=5, ipadx=20)

#select_id button
select_btn = ttk.Button(window, text="EDIT CUSTOMER DATA", command=select_id)
select_btn.grid(row=10, column=0, columnspan=2, pady=5, padx=5, ipadx=20)

next_btn = ttk.Button(window, text="NEXT PAGE", command=nextpg)
next_btn.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=50)

conn.commit()
conn.close()
