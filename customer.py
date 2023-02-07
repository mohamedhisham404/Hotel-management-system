from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import sqlite3

class customer:
    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1310x645+235+255")

        #=====================================================Variables=====================================================
        self.var_ref = StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_name = StringVar()
        self.var_gender = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_idProofType = StringVar()
        self.var_idNumber = StringVar()
        self.var_address = StringVar()

        # ====================== title ======================
        lbl_title=Label(text="Add customer Details",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE) 
        lbl_title.place(x=0,y=0,width=1315,height=50)

        # ====================== label frame ======================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman",12,"bold"),fg="black")
        labelframeleft.place(x=0,y=50,width=425,height=510)

        # ====================== labels and entrys ======================
        #cust_ref
        lbl_cust_ref=Label(labelframeleft,text="Customer reference",font=("times new roman",12,"bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")

        entry_ref=Entry(labelframeleft,textvariable=self.var_ref,width=29,font=("times new roman",12,"bold"),bd=5,state="readonly")
        entry_ref.grid(row=0,column=1,padx=10,pady=10,sticky="w") 

        #cust_name
        lbl_cust_name=Label(labelframeleft,text="Customer Name",font=("times new roman",12,"bold")).grid(row=1,column=0,padx=10,pady=10,sticky="w")
         
        entry_cust_name=Entry(labelframeleft,textvariable=self.var_name,width=29,font=("times new roman",12,"bold"),bd=5)
        entry_cust_name.grid(row=1,column=1,padx=10,pady=10,sticky="w")

        #gender
        lbl_gender=Label(labelframeleft,text="Gender",font=("times new roman",12,"bold")).grid(row=2,column=0,padx=10,pady=10,sticky="w")

        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=29)
        combo_gender["values"]=("Male","Female")
        combo_gender.grid(row=2,column=1,padx=10,pady=10,sticky="w")
        
        #phone number
        lbl_phone_number=Label(labelframeleft,text="Phone Number",font=("times new roman",12,"bold")).grid(row=3,column=0,padx=10,pady=10,sticky="w")

        entry_phone_number=Entry(labelframeleft,textvariable=self.var_mobile,width=29,font=("times new roman",12,"bold"),bd=5)
        entry_phone_number.grid(row=3,column=1,padx=10,pady=10,sticky="w")

        #email
        lbl_email=Label(labelframeleft,text="Email",font=("times new roman",12,"bold")).grid(row=4,column=0,padx=10,pady=10,sticky="w")

        entry_email=Entry(labelframeleft,textvariable=self.var_email,width=29,font=("times new roman",12,"bold"),bd=5)
        entry_email.grid(row=4,column=1,padx=10,pady=10,sticky="w")

        #nationality
        lbl_nationality=Label(labelframeleft,text="Nationality",font=("times new roman",12,"bold")).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        entry_nationality=Entry(labelframeleft,textvariable=self.var_nationality,width=29,font=("times new roman",12,"bold"),bd=5)
        entry_nationality.grid(row=5,column=1,padx=10,pady=10,sticky="w")
        
        #id proof type
        lbl_id_proof_type=Label(labelframeleft,text="ID Proof Type",font=("times new roman",12,"bold")).grid(row=6,column=0,padx=10,pady=10,sticky="w")
        
        combo_id_proof_type=ttk.Combobox(labelframeleft,textvariable=self.var_idProofType,font=("times new roman",12,"bold"),width=29)
        combo_id_proof_type["values"]=("ID Card","Passport","Driving License")
        combo_id_proof_type.grid(row=6,column=1,padx=10,pady=10,sticky="w")
        #id number
        lbl_id_number=Label(labelframeleft,text="ID Number",font=("times new roman",12,"bold")).grid(row=7,column=0,padx=10,pady=10,sticky="w")

        entry_id_number=Entry(labelframeleft,textvariable=self.var_idNumber,width=29,font=("times new roman",12,"bold"),bd=5)
        entry_id_number.grid(row=7,column=1,padx=10,pady=10,sticky="w")

        #address
        lbl_address=Label(labelframeleft,text="Address",font=("times new roman",12,"bold")).grid(row=8,column=0,padx=10,pady=10,sticky="w")

        entry_address=Entry(labelframeleft,textvariable=self.var_address,width=29,font=("times new roman",12,"bold"),bd=5)
        entry_address.grid(row=8,column=1,padx=10,pady=10,sticky="w")

        #===================== btns ======================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=450,width=350,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,width=8,font=("times new roman",11,"bold"),bg="black",fg="gold").grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,width=8,font=("times new roman",11,"bold"),bg="black",fg="gold").grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,width=8,font=("times new roman",11,"bold"),bg="black",fg="gold").grid(row=0,column=2,padx=1)

        btnClear=Button(btn_frame,text="Clear",command=self.reset,width=8,font=("times new roman",11,"bold"),bg="black",fg="gold").grid(row=0,column=3,padx=1)

        # ====================== label frame search sys ======================
        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And search System",font=("times new roman",12,"bold"),padx=2)
        Table_frame.place(x=435,y=50,width=860,height=490)

        lblseachby=Label(Table_frame,text="Search By",font=("times new roman",12,"bold"),bg="red",fg="white").grid(row=0,column=0,padx=10,pady=10,sticky="w")

        self.search_var=StringVar()
        combo_searchby=ttk.Combobox(Table_frame,textvariable=self.search_var,font=("times new roman",12,"bold"),width=29)
        combo_searchby["values"]=("Mobile","Ref")
        combo_searchby.current(0)
        combo_searchby.grid(row=0,column=1,padx=10,pady=10,sticky="w")

        self.txt_search=StringVar()
        txtsearch=Entry(Table_frame,textvariable=self.txt_search,width=29,font=("times new roman",12,"bold"),bd=5)
        txtsearch.grid(row=0,column=2,padx=10,pady=10,sticky="w")

        btnsearch=Button(Table_frame,text="Search",command=self.search,width=8,font=("times new roman",11,"bold"),bg="black",fg="gold").grid(row=0,column=3,padx=10,pady=10)

        btnShowall=Button(Table_frame,text="Show All",command=self.fetch_data,width=8,font=("times new roman",11,"bold"),bg="black",fg="gold").grid(row=0,column=4,padx=10,pady=10)

        # ====================== show data table ======================
        details_table=Frame(Table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)

        scroll_x=Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_table=ttk.Treeview(details_table,columns=("ref","name","gender","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y) 

        scroll_x.config(command=self.Cust_Details_table.xview)
        scroll_y.config(command=self.Cust_Details_table.yview)
            
        self.Cust_Details_table.heading("ref",text="Reference")
        self.Cust_Details_table.heading("name",text="Name")
        self.Cust_Details_table.heading("gender",text="Gender")
        self.Cust_Details_table.heading("mobile",text="Mobile")
        self.Cust_Details_table.heading("email",text="Email")
        self.Cust_Details_table.heading("nationality",text="Nationality")
        self.Cust_Details_table.heading("idproof",text="ID Proof")
        self.Cust_Details_table.heading("idnumber",text="ID Number")
        self.Cust_Details_table.heading("address",text="Address")
        self.Cust_Details_table["show"]="headings"
        self.Cust_Details_table.pack(fill=BOTH,expand=1)
        
        self.Cust_Details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_name.get()=="":
            messagebox.showerror("Error","Please Enter Customer Name")
        elif self.var_gender.get()=="":
            messagebox.showerror("Error","Please Select Gender")
        elif self.var_mobile.get()=="":
            messagebox.showerror("Error","Please Enter Mobile Number")
        elif self.var_email.get()=="":
            messagebox.showerror("Error","Please Enter Email")
        elif self.var_nationality.get()=="":
            messagebox.showerror("Error","Please Select Nationality")
        elif self.var_idProofType.get()=="":
            messagebox.showerror("Error","Please Select ID Proof Type")
        elif self.var_idNumber.get()=="":
            messagebox.showerror("Error","Please Enter ID Number")
        elif self.var_address.get()=="":
            messagebox.showerror("Error","Please Enter Address")
        else:
            try:
                conn=sqlite3.connect('database.db')
                cursor=conn.cursor()
                sqlite_insert_with_param='''INSERT INTO Customer(Ref,Name,Gender,Mobile,e_mail,Nationality,ID_proof_Type,ID_Number,Address)
                                                                VALUES(?,?,?,?,?,?,?,?,?);'''

                data_tuble=(self.var_ref.get(),
                            self.var_name.get(),
                            self.var_gender.get(),
                            self.var_mobile.get(),
                            self.var_email.get(),
                            self.var_nationality.get(),
                            self.var_idProofType.get(),
                            self.var_idNumber.get(),
                            self.var_address.get())
                cursor.execute(sqlite_insert_with_param,data_tuble)
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","customer details added successfully",parent=self.root)
            except sqlite3.Error as error:
                messagebox.showerror("Error",f"Error due to {error}",parent=self.root)


    def fetch_data(self):
        conn=sqlite3.connect('database.db')
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM Customer")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_table.delete(*self.Cust_Details_table.get_children())
            for row in rows:
                self.Cust_Details_table.insert('',END,values=row)
            conn.commit()
        conn.close()    

    def get_cursor(self,evnet=""):
        cursor_row=self.Cust_Details_table.focus()
        contents=self.Cust_Details_table.item(cursor_row)
        row=contents['values']
        self.var_ref.set(row[0])
        self.var_name.set(row[1])
        self.var_gender.set(row[2])
        self.var_mobile.set(row[3])
        self.var_email.set(row[4])
        self.var_nationality.set(row[5])
        self.var_idProofType.set(row[6])
        self.var_idNumber.set(row[7])
        self.var_address.set(row[8])                                                                                                                    
                
    def update(self):
        if self.var_ref.get()=="":
            messagebox.showerror("Error","Please Enter Customer Reference",parent=self.root)
        else:
            conn=sqlite3.connect('database.db')
            cursor=conn.cursor()
            cursor.execute("update customer set Ref=?,Name=?,Gender=?,Mobile=?,e_mail=?,Nationality=?,ID_Proof_Type=?,ID_Number=?,Address=? where Ref=?",(
                                                                                                                                                  self.var_ref.get(),
                                                                                                                                                  self.var_name.get(),
                                                                                                                                                  self.var_gender.get(),
                                                                                                                                                  self.var_mobile.get(),
                                                                                                                                                  self.var_email.get(),
                                                                                                                                                  self.var_nationality.get(),
                                                                                                                                                  self.var_idProofType.get(),
                                                                                                                                                  self.var_idNumber.get(),
                                                                                                                                                  self.var_address.get(),
                                                                                                                                                  self.var_ref.get()
                                                                                                                                                  ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","customer details updated successfully",parent=self.root)


    def mDelete(self):
        mDelete=messagebox.askyesno("Delete","Do you want to delete this customer?",parent=self.root)
        if mDelete>0:
            conn=sqlite3.connect('database.db')
            cursor=conn.cursor()
            cursor.execute("delete from customer where Ref=?",(self.var_ref.get(),))
            messagebox.showinfo("Success","customer details deleted successfully",parent=self.root)        
        elif not mDelete:
            return
        conn.commit()
        self.fetch_data()
        conn.close()
        
    def reset(self):
        self.var_name.set("")
        self.var_gender.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        self.var_nationality.set("")
        self.var_idProofType.set("")
        self.var_idNumber.set("")
        self.var_address.set("")
        
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
            
    def search(self):
        conn=sqlite3.connect('database.db')
        cursor=conn.cursor()

        cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_table.delete(*self.Cust_Details_table.get_children())
            for row in rows:
                self.Cust_Details_table.insert('',END,values=row)
            conn.commit()
        else:
            messagebox.showerror("Error","No data found",parent=self.root)    
        conn.close()

if __name__=="__main__":
    root = Tk()
    obj=customer(root)
    root.mainloop()
