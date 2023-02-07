from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from time import strftime
from datetime import datetime
import sqlite3

class roombooking:
    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1310x645+235+255")
        #=====================================================Variables=====================================================
        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable = StringVar()
        self.var_meal = StringVar()
        self.var_noOffdays= StringVar()
        self.var_paidtax= StringVar()
        self.var_actualtotal= StringVar()
        self.var_total= StringVar()

        # ====================== title ====================== 
        lbl_title=Label(text="Room Booking Details",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE) 
        lbl_title.place(x=0,y=0,width=1315,height=50)

        # ====================== label frame ======================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking Details",font=("times new roman",12,"bold"),fg="black")
        labelframeleft.place(x=0,y=50,width=425,height=530)

        # ====================== labels and entrys ======================
        #cust_con
        lbl_cust_contant=Label(labelframeleft,text="Customer Contact",font=("times new roman",12,"bold")).grid(row=0,column=0,sticky="w")

        entry_contant=Entry(labelframeleft,textvariable=self.var_contact,width=20,font=("times new roman",12,"bold"))
        entry_contant.grid(row=0,column=1,sticky='w') 

        #fetched data button
        btn_fetch_data=Button(labelframeleft,command=self.fetch_contact,text="Fetch Data",font=("times new roman",10,"bold"),bg="black",fg="gold",width=8)
        btn_fetch_data.place(x=300,y=0,height=27)

        #check in date
        lbl_check_in_date=Label(labelframeleft,text="Check In Date",font=("times new roman",12,"bold")).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        entry_check_in_date=Entry(labelframeleft,textvariable=self.var_checkin,width=29,font=("times new roman",12,"bold"),bd=5)
        entry_check_in_date.grid(row=1,column=1)

        #check out date
        lbl_check_out_date=Label(labelframeleft,text="Check Out Date",font=("times new roman",12,"bold")).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        entry_check_out_date=Entry(labelframeleft,textvariable=self.var_checkout,width=29,font=("times new roman",12,"bold"),bd=5)
        entry_check_out_date.grid(row=2,column=1)

        #roomType
        lbl_room_type=Label(labelframeleft,text="Room Type",font=("times new roman",12,"bold")).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        conn=sqlite3.connect("database.db")
        mycursor=conn.cursor()
        mycursor.execute("select RoomType from Details") 
        ide=mycursor.fetchone()

        combo_roomty=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,width=29,font=("times new roman",12,"bold"),state="readonly")
        combo_roomty["values"]=ide
        combo_roomty.current(0)
        combo_roomty.grid(row=3,column=1)


        #Avaialble room
        lbl_avaialble_room=Label(labelframeleft,text="Available Room",font=("times new roman",12,"bold")).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        conn=sqlite3.connect("database.db")
        cursor=conn.cursor()
        cursor.execute("select RoomNumber from Details") 
        row=cursor.fetchone()

        combo_roomNo=ttk.Combobox(labelframeleft,textvariable=self.var_roomavailable,width=29,font=("times new roman",12,"bold"),state="readonly")
        combo_roomNo["values"]=row
        combo_roomNo.current(0)
        combo_roomNo.grid(row=4,column=1)

        #combo meal
        lbl_meal=Label(labelframeleft,text="Meal",font=("times new roman",12,"bold")).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        combo_room_type=ttk.Combobox(labelframeleft,textvariable=self.var_meal,width=29,font=("times new roman",12,"bold"),state="readonly")
        combo_room_type["values"]=("BreakFast","Lunche","Dinner")
        combo_room_type.grid(row=5,column=1)

        #No of days
        lbl_no_of_days=Label(labelframeleft,text="No of Days",font=("times new roman",12,"bold")).grid(row=6,column=0,padx=10,pady=10,sticky="w")
        entry_no_of_days=Entry(labelframeleft,textvariable=self.var_noOffdays,width=29,font=("times new roman",12,"bold"),bd=5,state="readonly")
        entry_no_of_days.grid(row=6,column=1)

        #paid tax
        lbl_paid_tax=Label(labelframeleft,text="Paid Tax",font=("times new roman",12,"bold")).grid(row=7,column=0,padx=10,pady=10,sticky="w")
        entry_paid_tax=Entry(labelframeleft,textvariable=self.var_paidtax,width=29,font=("times new roman",12,"bold"),bd=5,state="readonly")
        entry_paid_tax.grid(row=7,column=1)

        #sub total
        lbl_sub_total=Label(labelframeleft,text="Sub Total",font=("times new roman",12,"bold")).grid(row=8,column=0,padx=10,pady=10,sticky="w")
        entry_sub_total=Entry(labelframeleft,textvariable=self.var_actualtotal,width=29,font=("times new roman",12,"bold"),bd=5,state="readonly")
        entry_sub_total.grid(row=8,column=1)

        #total cost
        lbl_total_cost=Label(labelframeleft,text="Total Cost",font=("times new roman",12,"bold")).grid(row=9,column=0,padx=10,pady=10,sticky="w")
        entry_total_cost=Entry(labelframeleft,textvariable=self.var_total,width=29,font=("times new roman",12,"bold"),bd=5,state="readonly")
        entry_total_cost.grid(row=9,column=1)

        #===================== bill button ======================
        btn_bill=Button(labelframeleft,command=self.total,text="Bill",font=("times new roman",10,"bold"),bg="black",fg="gold",width=8)
        btn_bill.grid(row=10,column=0,padx=10,pady=10,sticky="w")
        #===================== Buttons ======================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=470,width=350,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,width=8,font=("times new roman",11,"bold"),bg="black",fg="gold").grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,width=8,font=("times new roman",11,"bold"),bg="black",fg="gold").grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.delete,width=8,font=("times new roman",11,"bold"),bg="black",fg="gold").grid(row=0,column=2,padx=1)

        btnClear=Button(btn_frame,text="Clear",command=self.reset,width=8,font=("times new roman",11,"bold"),bg="black",fg="gold").grid(row=0,column=3,padx=1)

        # ====================== tabel frame search sys ======================
        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And search System",font=("times new roman",12,"bold"),padx=2)
        Table_frame.place(x=435,y=280,width=860,height=260)

        lblseachby=Label(Table_frame,text="Search By",font=("times new roman",12,"bold"),bg="red",fg="white").grid(row=0,column=0,padx=2,pady=10,sticky="w")

        self.search_var=StringVar()
        combo_searchby=ttk.Combobox(Table_frame,textvariable=self.search_var,font=("times new roman",12,"bold"),width=29)
        combo_searchby["values"]=("Contact","RoomAvaiable")
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

        self.Room_table=ttk.Treeview(details_table,columns=("contact","checkin","checkout","roomtype","roomavailable","meal","noOfdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y) 

        scroll_x.config(command=self.Room_table.xview)
        scroll_y.config(command=self.Room_table.yview)
            
        self.Room_table.heading("contact",text="Mobile")
        self.Room_table.heading("checkin",text="Check In")
        self.Room_table.heading("checkout",text="Check Out")
        self.Room_table.heading("roomtype",text="Room Type")
        self.Room_table.heading("roomavailable",text="Room Number")
        self.Room_table.heading("meal",text="Meal")
        self.Room_table.heading("noOfdays",text="Number Of Days")
         
        self.Room_table["show"]="headings"
        self.Room_table.pack(fill=BOTH,expand=1)

        self.Room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    # ====================== add data table ======================
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin=="":
            messagebox.showerror("Error","Customer contact is required")
        else:
            try:
                conn=sqlite3.connect('database.db')
                cursor=conn.cursor()
                sqlite_insert_with_param='''INSERT INTO Room(Contact,Chech_in,Check_out,RoomType,RoomAvaiable,Meal,NoOfDays)
                                                                VALUES(?,?,?,?,?,?,?);'''

                data_tuble=(self.var_contact.get(),
                            self.var_checkin.get(),
                            self.var_checkout.get(),
                            self.var_roomtype.get(),
                            self.var_roomavailable.get(),
                            self.var_meal.get(),
                            self.var_noOffdays.get())
                cursor.execute(sqlite_insert_with_param,data_tuble)
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room details added successfully",parent=self.root)
            except sqlite3.Error as error:
                messagebox.showerror("Error",f"Error due to {error}",parent=self.root)

     
    def fetch_data(self):
        conn=sqlite3.connect('database.db')
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM Room")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.Room_table.delete(*self.Room_table.get_children())
            for row in rows:
                self.Room_table.insert('',END,values=row)
            conn.commit()
        conn.close()   

    def get_cursor(self,even=""):
        cursor_row=self.Room_table.focus()
        contents=self.Room_table.item(cursor_row)
        row=contents['values']
        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noOffdays.set(row[6])     
    
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Contact is required",parent=self.root)
        else:
            conn=sqlite3.connect('database.db')
            cursor=conn.cursor()
            cursor.execute("update Room set chech_in=?,check_out=?,RoomType=?,RoomAvaiable=?,Meal=?,NoOfDays=? WHERE Contact=?",(self.var_checkin.get(),
                                                                                                                                    self.var_checkout.get(),
                                                                                                                                    self.var_roomtype.get(),
                                                                                                                                    self.var_roomavailable.get(),
                                                                                                                                    self.var_meal.get(),
                                                                                                                                    self.var_noOffdays.get(),
                                                                                                                                    self.var_contact.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Room details updated successfully",parent=self.root)


    def delete(self):
        mDelete=messagebox.askyesno("Delete","Do you want to delete this room?",parent=self.root)
        if mDelete>0:
            conn=sqlite3.connect('database.db')
            cursor=conn.cursor()
            cursor.execute("delete from Room where Contact=?",(self.var_contact.get(),))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Room details deleted successfully",parent=self.root)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close() 

    def reset(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_noOffdays.set("")  
        self.var_paidtax.set(""),
        self.var_actualtotal.set(""),
        self.var_total.set("")                    
    # ====================== all data fetch ======================
    def fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please Enter Contact Number",parent=self.root)
        else:
            con=sqlite3.connect("database.db")
            cur=con.cursor()
            cur.execute("select Name from customer where Mobile=?",(self.var_contact.get(),))
            rows=cur.fetchone()

            if rows==None:
                messagebox.showerror("Error","Contact Not Found",parent=self.root)
            else:
                con.commit()
                con.close()
                #===================== name ======================
                showDataFrame=Frame(self.root,bd=2,relief=RIDGE)
                showDataFrame.place(x=455,y=55,width=300,height=180) 

                lblname=Label(showDataFrame,text="Name",font=("times new roman",12,"bold"))
                lblname.place(x=0,y=0)

                lbl=Label(showDataFrame,text=rows[0],font=("times new roman",12,"bold"))
                lbl.place(x=90,y=0)
                #===================== gender ======================
                con=sqlite3.connect("database.db")
                cur=con.cursor()
                cur.execute("select Gender from customer where Mobile=?",(self.var_contact.get(),))
                rows=cur.fetchone()

                lblname=Label(showDataFrame,text="Gender",font=("times new roman",12,"bold"))
                lblname.place(x=0,y=30)

                lbl=Label(showDataFrame,text=rows,font=("times new roman",12,"bold"))
                lbl.place(x=90,y=30)
                #===================== email ======================
                con=sqlite3.connect("database.db")
                cur=con.cursor()
                cur.execute("select e_mail from customer where Mobile=?",(self.var_contact.get(),))
                rows=cur.fetchone()

                lblname=Label(showDataFrame,text="Email",font=("times new roman",12,"bold"))
                lblname.place(x=0,y=60)

                lbl=Label(showDataFrame,text=rows,font=("times new roman",12,"bold"))
                lbl.place(x=90,y=60)

                #===================== Nationality ======================
                con=sqlite3.connect("database.db")
                cur=con.cursor()
                cur.execute("select Nationality from customer where Mobile=?",(self.var_contact.get(),))
                rows=cur.fetchone()

                lblname=Label(showDataFrame,text="Nationality",font=("times new roman",12,"bold"))
                lblname.place(x=0,y=90)

                lbl=Label(showDataFrame,text=rows,font=("times new roman",12,"bold"))
                lbl.place(x=90,y=90)

                #===================== Address ======================
                con=sqlite3.connect("database.db")
                cur=con.cursor()
                cur.execute("select Address from customer where Mobile=?",(self.var_contact.get(),))
                rows=cur.fetchone()

                lblname=Label(showDataFrame,text="Address",font=("times new roman",12,"bold"))
                lblname.place(x=0,y=120)

                lbl=Label(showDataFrame,text=rows,font=("times new roman",12,"bold"))
                lbl.place(x=90,y=120)

    #search sys
    def search(self):
        conn=sqlite3.connect('database.db')
        cursor=conn.cursor()

        cursor.execute("select * from Room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.Room_table.delete(*self.Room_table.get_children())
            for row in rows:
                self.Room_table.insert('',END,values=row)
            conn.commit()
        else:
            messagebox.showerror("Error","No data found",parent=self.root)    
        conn.close()



        

    def total(self):
        inData=self.var_checkin.get()
        outData=self.var_checkout.get()
        inDate=datetime.strptime(inData,"%d/%m/%Y")
        outDate=datetime.strptime(outData,"%d/%m/%Y")
        self.var_noOffdays.set(abs(outDate-inDate).days)

        if(self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Triple"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noOffdays.get())
            q4=float(q1+q2)
            q5=float(q4+q3)
            Tax =str('%.2f'%((q5*0.1)))
            ST=str('%.2f'%((q5)))
            TT=str('%.2f'%((q5+((q5*0.1)))))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Double"):
            q1=float(200)
            q2=float(500)
            q3=float(self.var_noOffdays.get())
            q4=float(q1+q2)
            q5=float(q4+q3)
            Tax =str('%.2f'%((q5*0.1)))
            ST=str('%.2f'%((q5)))
            TT=str('%.2f'%((q5+((q5*0.1)))))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Single"):
            q1=float(100)
            q2=float(200)
            q3=float(self.var_noOffdays.get())
            q4=float(q1+q2)
            q5=float(q4+q3)
            Tax =str('%.2f'%((q5*0.1)))
            ST=str('%.2f'%((q5)))
            TT=str('%.2f'%((q5+((q5*0.1)))))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif(self.var_meal.get()=="Lunche" and self.var_roomtype.get()=="Triple"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noOffdays.get())
            q4=float(q1+q2)
            q5=float(q4+q3)
            Tax =str('%.2f'%((q5*0.1)))
            ST=str('%.2f'%((q5)))
            TT=str('%.2f'%((q5+((q5*0.1)))))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)    
        elif(self.var_meal.get()=="Lunche" and self.var_roomtype.get()=="Double"):
            q1=float(200)
            q2=float(500)
            q3=float(self.var_noOffdays.get())
            q4=float(q1+q2)
            q5=float(q4+q3)
            Tax =str('%.2f'%((q5*0.1)))
            ST=str('%.2f'%((q5)))
            TT=str('%.2f'%((q5+((q5*0.1)))))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif(self.var_meal.get()=="Lunche" and self.var_roomtype.get()=="Single"):  
            q1=float(100)
            q2=float(200)
            q3=float(self.var_noOffdays.get())
            q4=float(q1+q2)
            q5=float(q4+q3)
            Tax =str('%.2f'%((q5*0.1)))
            ST=str('%.2f'%((q5)))
            TT=str('%.2f'%((q5+((q5*0.1)))))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif(self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Single"):
            q1=float(100)
            q2=float(200)
            q3=float(self.var_noOffdays.get())
            q4=float(q1+q2)
            q5=float(q4+q3)
            Tax =str('%.2f'%((q5*0.1)))
            ST=str('%.2f'%((q5)))
            TT=str('%.2f'%((q5+((q5*0.1)))))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif(self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Double"):
            q1=float(200)
            q2=float(500)
            q3=float(self.var_noOffdays.get())
            q4=float(q1+q2)
            q5=float(q4+q3)
            Tax =str('%.2f'%((q5*0.1)))
            ST=str('%.2f'%((q5)))
            TT=str('%.2f'%((q5+((q5*0.1)))))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif(self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Triple"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noOffdays.get())
            q4=float(q1+q2)
            q5=float(q4+q3)
            Tax =str('%.2f'%((q5*0.1)))
            ST=str('%.2f'%((q5)))
            TT=str('%.2f'%((q5+((q5*0.1)))))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)      

if __name__=="__main__":
    root = Tk()
    obj=roombooking(root)
    root.mainloop()        