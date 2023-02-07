from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import sqlite3

class detailsRoom:
    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1310x645+235+255")
    # ====================== title ======================
        lbl_title=Label(text="Room Booking Details",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE) 
        lbl_title.place(x=0,y=0,width=1315,height=50)
    # ====================== label frame ======================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Add New Room",font=("times new roman",12,"bold"),fg="black")
        labelframeleft.place(x=5,y=50,width=540,height=350)
        
        #floor
        lblfloor=Label(labelframeleft,text="Floor",font=("times new roman",12,"bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")

        self.var_floor = StringVar()
        entry_ref=Entry(labelframeleft,width=29,textvariable=self.var_floor,font=("times new roman",12,"bold"),bd=5)
        entry_ref.grid(row=0,column=1,padx=10,pady=10,sticky="w") 

        #room type
        lbl_room_type=Label(labelframeleft,text="Room Type",font=("times new roman",12,"bold")).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        
        self.var_RoomType = StringVar()
        combo_room_type=ttk.Combobox(labelframeleft,width=29,textvariable=self.var_RoomType,font=("times new roman",12,"bold"),state="readonly")
        combo_room_type["values"]=("Single","Double","Triple")
        combo_room_type.grid(row=2,column=1)

        #room no
        lbl_room_no=Label(labelframeleft,text="Room No",font=("times new roman",12,"bold")).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        self.var_room_no = StringVar()
        entry_room_no=Entry(labelframeleft,width=29,textvariable=self.var_room_no,font=("times new roman",12,"bold"),bd=5)
        entry_room_no.grid(row=1,column=1,padx=10,pady=10,sticky="w")

        #===================== btns ======================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=350,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,width=8,font=("times new roman",11,"bold"),bg="black",fg="gold").grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,width=8,font=("times new roman",11,"bold"),bg="black",fg="gold").grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.delete,width=8,font=("times new roman",11,"bold"),bg="black",fg="gold").grid(row=0,column=2,padx=1)

        btnClear=Button(btn_frame,text="Clear",command=self.reset,width=8,font=("times new roman",11,"bold"),bg="black",fg="gold").grid(row=0,column=3,padx=1)

        # ====================== label frame search sys ======================
        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",font=("times new roman",12,"bold"),padx=2)
        Table_frame.place(x=600,y=55,width=600,height=350)

        scroll_x=Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_frame,orient=VERTICAL)
        self.details_Table_frame=ttk.Treeview(Table_frame,columns=("Floor","RoomNumber","RoomType"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y) 

        scroll_x.config(command=self.details_Table_frame.xview)
        scroll_y.config(command=self.details_Table_frame.yview)

        self.details_Table_frame.heading("Floor",text="Floor")
        self.details_Table_frame.heading("RoomNumber",text="Room Number")
        self.details_Table_frame.heading("RoomType",text="Room Type")
        
        self.details_Table_frame["show"]="headings"
        
        self.details_Table_frame.column("Floor",width=100)
        self.details_Table_frame.column("RoomNumber",width=100)
        self.details_Table_frame.column("RoomType",width=100)

        self.details_Table_frame.pack(fill=BOTH,expand=1)
        self.details_Table_frame.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_floor.get()=="" and self.var_RoomType=="" and self.var_room_no.get()=="":
            messagebox.showerror("Error","Customer contact is required")
        else:
            try:
                conn=sqlite3.connect('database.db')
                cursor=conn.cursor()
                sqlite_insert_with_param='''INSERT INTO Details(Floor,RoomNumber,RoomType)
                                                                VALUES(?,?,?);'''

                data_tuble=(self.var_floor.get(),
                            self.var_room_no.get(),
                            self.var_RoomType.get())
                cursor.execute(sqlite_insert_with_param,data_tuble)
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room added successfully",parent=self.root)
            except sqlite3.Error as error:
                messagebox.showerror("Error",f"Error due to {error}",parent=self.root)

    def fetch_data(self):
        conn=sqlite3.connect('database.db')
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM Details")
        rows=cursor.fetchall()
        if len(rows)!=0:
            self.details_Table_frame.delete(*self.details_Table_frame.get_children())
            for row in rows:
                self.details_Table_frame.insert('',END,values=row)
            conn.commit()
        conn.close()

    def get_cursor(self,evnet=""):
        cursor_row=self.details_Table_frame.focus()
        contents=self.details_Table_frame.item(cursor_row)
        row=contents['values']
        self.var_floor.set(row[0])
        self.var_room_no.set(row[1])
        self.var_RoomType.set(row[2])

        

    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error","Floor is required",parent=self.root)
        else:
            conn=sqlite3.connect('database.db')
            cursor=conn.cursor()
            cursor.execute("update Details set Floor=?,RoomNumber=?,RoomType=?",(self.var_floor.get(),
                                                                                self.var_room_no.get(),
                                                                                self.var_RoomType.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Room details updated successfully",parent=self.root)
     
    def delete(self):
        mDelete=messagebox.askyesno("Delete","Do you want to delete this room?",parent=self.root)
        if mDelete>0:
            conn=sqlite3.connect('database.db')
            cursor=conn.cursor()
            cursor.execute("delete from Details where Floor=?",(self.var_floor.get(),))
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
        self.var_floor.set("")
        self.var_room_no.set("")
        self.var_RoomType.set("")
           

if __name__=="__main__":
    root = Tk()
    obj=detailsRoom(root)
    root.mainloop()
