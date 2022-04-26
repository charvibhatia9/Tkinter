import sqlite3
from tkinter import *
from tkinter import ttk

window=Tk()
window['bg']='light yellow'
window.title('dbms project')
window.geometry('500x600')
conn=sqlite3.connect('project_dbms.db')
c= conn.cursor()

"""c.execute( '''CREATE TABLE stock(
    sid INT PRIMARY KEY,
    pid INT,
    pname TEXT,
    instock INT,
    CONSTRAINT fkpid FOREIGN KEY(pid) REFERENCES product(pid)
    );
    ''')
"""
def nextpg():
    window.destroy()
    import multipage

def save():
    conn=sqlite3.connect('project_dbms.db')
    c= conn.cursor()
    record_id = delete_box.get()
    c.execute('''
    UPDATE stock SET
    sid= :sid,
    pid= :pid,
    pname= :pname,
    instock= :instock

    WHERE oid = :oid''',

    {
    "sid": sid_e.get(),
    "pid":pid_e.get(),
    "pname":pname_e.get(),
    "instock": instock_e.get(),

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
    check=c.execute("SELECT COUNT(sid)FROM stock WHERE oid="+ delete_box.get())
    if delete_box.get()== "":
        print("Please Select An ID")
    elif check != 0:
        global editor
        editor.title('Update Window')
        editor.geometry('450x400')
        c.execute("SELECT * FROM stock WHERE oid = " + record_id)
        records=c.fetchall()

     
        global sid_e
        global pid_e
        global pname_e
        global instock_e

        #text boX
        sid_e = Entry(editor, width=30)
        sid_e.grid(row=2, column=1)
        
        pid_e = Entry(editor, width=30)
        pid_e.grid(row=3, column=1, padx=20)

        pname_e = Entry(editor, width=30)
        pname_e.grid(row=4, column=1)

        instock_e = Entry(editor, width=30)
        instock_e.grid(row=5, column=1)


        #Text Labels
        heading= ttk.Label(window, text="STOCK AVAILABILITY")
        heading.grid(row=0, column=1)
        
        sid_label = Label(editor, text="Stock ID")
        sid_label.grid(row=2, column=0)

        pid_label = ttk.Label(editor, text="Product ID")
        pid_label.grid(row=3, column=0)

        pname_label = Label(editor, text="Stock Name")
        pname_label.grid(row=4, column=0)

        instock_label = Label(editor, text="Instock")
        instock_label.grid(row=5, column=0)


        for each in records:
            sid_e.insert(0,each[0])
            pid_e.insert(0,each[1])
            pname_e.insert(0,each[2])
            instock_e.insert(0,each[3])

        #save button
        save_btn = ttk.Button(editor, text="Save Record", command=save)
        save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=50)
        
    else:
        print("ID DOESN'T EXIST")
    conn.commit()
    conn.close()

def delete():
    conn=sqlite3.connect('project_dbms.db')
    c= conn.cursor()
    if delete_box.get()== "":
        print("Please Select An ID")
    else:
        c.execute("DELETE from stock WHERE oid = " +delete_box.get())
    
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
    delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=50)

    #Update Button
    update_btn = ttk.Button(window, text="Update Record", command=update)
    update_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=50)

    conn.commit()
    conn.close()

#submit function
def submit():
    conn=sqlite3.connect('project_dbms.db')
    c= conn.cursor()
    c.execute("INSERT INTO stock VALUES(:sid, :pid, :pname, :instock)",
			{
                                'sid': sid.get(),
                                'pid': pid.get(),
				'pname': pname.get(),
				'instock': instock.get()
			})
    
    conn.commit()
    conn.close()
    
    sid.delete(0,END)
    pid.delete(0,END)
    pname.delete(0,END)
    instock.delete(0,END)


#query function(show records)
def query():
    conn=sqlite3.connect('project_dbms.db')
    c= conn.cursor()
    
    c.execute('SELECT * FROM stock')#oid is the primary key assigned by
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

sid = Entry(window, width=30)
sid.grid(row=2, column=1)

pid = Entry(window, width=30)
pid.grid(row=3, column=1, padx=20)

pname = Entry(window, width=30)
pname.grid(row=4, column=1)

instock = Entry(window, width=30)
instock.grid(row=5, column=1)


#Text Labels
heading= ttk.Label(window, text="STOCK AVAILABILITY")
heading.grid(row=0, column=1, padx=2, pady=2)

sid_label = ttk.Label(window, text="Stock ID")
sid_label.grid(row=2, column=0,pady=2,padx=2)

pid_label = ttk.Label(window, text="Product ID")
pid_label.grid(row=3, column=0, pady=2,padx=2)

pname_label = ttk.Label(window, text="Product Name")
pname_label.grid(row=4, column=0,padx=2)

instock_label = ttk.Label(window, text="Instock")
instock_label.grid(row=5, column=0,padx=2)

submit_btn=ttk.Button(window, text="SUBMIT",command= submit) 
submit_btn.grid(row=6,column=0,columnspan=2,pady=10, padx=10,ipadx=50)

#Show records Button
query_btn = ttk.Button(window, text="VIEW PREVIOUS DATA", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=5, padx=5, ipadx=25)

#select_id button
select_btn = ttk.Button(window, text="UPDATE DATA", command=select_id)
select_btn.grid(row=10, column=0, columnspan=2, pady=7, padx=7, ipadx=40)

next_btn = ttk.Button(window, text="NEXT", command=nextpg)
next_btn.grid(row=11, column=0, columnspan=2, pady=7, padx=7, ipadx=40)

conn.commit()
conn.close()
