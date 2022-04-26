import sqlite3
from tkinter import *
from tkinter import ttk
window=Tk()
window['bg']='light blue'
window.title('Product Information')
window.geometry('500x600')
conn=sqlite3.connect('project_dbms.db')
c= conn.cursor()
"""
c.execute( '''CREATE TABLE product(
    pid INT PRIMARY KEY,
    pname TEXT,
    brand TEXT,
    price INT NOT NULL);
    ''')

c.execute("INSERT INTO product( pid, pname, brand, price)\
        VALUES (1,'kurti','fabindia', 4000)");

c.execute("INSERT INTO product( pid, pname, brand, price)\
        VALUES (2,'shirt','peterengland', 5900)");

c.execute("INSERT INTO product( pid, pname, brand, price)\
        VALUES (3,'skirt','chanel', 56788)");
"""

def nextpg():
    window.destroy()
    import page3

def save():
    conn=sqlite3.connect('project_dbms.db')
    c= conn.cursor()
    record_id = delete_box.get()
    c.execute("""
    UPDATE product SET
    pid= :pid,
    pname= :pname,
    brand= :brand,
    price= :price

    WHERE oid = :oid""",

    {
    "pid":pid_e.get(),
    "pname":pname_e.get(),
    "brand": brand_e.get(),
    "price": price_e.get(),

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
        
        c.execute("SELECT * FROM product WHERE oid = " + record_id)
        records=c.fetchall()

        #global variables
        global heading
        global pid_e
        global pname_e
        global brand_e
        global price_e

        #text boxes
        pid_e = Entry(editor, width=30)
        pid_e.grid(row=2, column=1, padx=20)

        pname_e = Entry(editor, width=30)
        pname_e.grid(row=3, column=1)

        brand_e = Entry(editor, width=30)
        brand_e.grid(row=4, column=1)

        price_e = Entry(editor, width=30)
        price_e.grid(row=5, column=1)


        #Text Labels

        heading= ttk.Label(window, text="PRODUCT BOUGHT BY THE CONSUMER")
        heading.grid(row=0, column=1)
        
        pid_label = ttk.Label(editor, text="Product ID")
        pid_label.grid(row=2, column=0)

        pname_label = Label(editor, text="Product Name")
        pname_label.grid(row=3, column=0)

        brand_label = Label(editor, text="Brand Name")
        brand_label.grid(row=4, column=0)

        price_label = Label(editor, text="Price")
        price_label.grid(row=5, column=0)


        for each in records:
            pid_e.insert(0,each[0])
            pname_e.insert(0,each[1])
            brand_e.insert(0,each[2])
            price_e.insert(0,each[3])

        #save button
        save_btn = ttk.Button(editor, text="Save Product information", command=save)
        save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=136)
    
    conn.commit()
    conn.close()

def delete():
    conn=sqlite3.connect('project_dbms.db')
    c= conn.cursor()
    if delete_box.get()== "":
        print("Please Select An ID")
    else:
        c.execute("DELETE from product WHERE oid = " +delete_box.get())
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
    delete_btn = ttk.Button(window, text="Delete Data", command=delete)
    delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

    #Update Button
    update_btn = ttk.Button(window, text="Update Data", command=update)
    update_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

    conn.commit()
    conn.close()

#submit function
def submit():
    conn=sqlite3.connect('project_dbms.db')
    c= conn.cursor()
    c.execute("INSERT INTO product VALUES(:pid, :pname, :brand, :price)",
			{
                                'pid': pid.get(),
				'pname': pname.get(),
				'brand': brand.get(),
				'price': price.get()
			})
    
    conn.commit()
    conn.close()
    
    pid.delete(0,END)
    pname.delete(0,END)
    brand.delete(0,END)
    price.delete(0,END)


#query function(show records)
def query():
    conn=sqlite3.connect('project_dbms.db')
    c= conn.cursor()
    
    c.execute('SELECT * FROM product')#oid is the primary key assigned by
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
pid = Entry(window, width=30)
pid.grid(row=2, column=1, padx=20)

pname = Entry(window, width=30)
pname.grid(row=3, column=1)

brand = Entry(window, width=30)
brand.grid(row=4, column=1)

price = Entry(window, width=30)
price.grid(row=5, column=1)


#Text Labels
heading= ttk.Label(window, text="PRODUCT BOUGHT BY THE CONSUMER")
heading.grid(row=0, column=1, pady=2, padx=2)
        
pid_label = ttk.Label(window, text="Product ID")
pid_label.grid(row=2, column=0, pady=2,padx=2)

pname_label = ttk.Label(window, text="Product Name")
pname_label.grid(row=3, column=0,padx=2)

brand_label = ttk.Label(window, text="Brand Name")
brand_label.grid(row=4, column=0,pady=2,padx=2)

price_label = ttk.Label(window, text="Price")
price_label.grid(row=5, column=0,padx=2)

submit_btn=ttk.Button(window, text="SUBMIT PRODUCT INFORMATION",command= submit) 
submit_btn.grid(row=7,column=0,columnspan=2,pady=10, padx=10,ipadx=50)

#Show records Button
query_btn = ttk.Button(window, text="SHOW PREVIOUS DATA", command=query)
query_btn.grid(row=8, column=0, columnspan=2, pady=5, padx=5, ipadx=20)

#select_id button
select_btn = ttk.Button(window, text="UPDATE PREVIOUS DATA", command=select_id)
select_btn.grid(row=10, column=0, columnspan=2, pady=5, padx=5, ipadx=20)

next_btn = ttk.Button(window, text="NEXT PAGE", command=nextpg)
next_btn.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=50)

conn.commit()
conn.close()
