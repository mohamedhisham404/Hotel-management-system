from tkinter import *
from PIL import ImageTk, Image
from customer import customer
from room import roombooking
from details import detailsRoom

class HotelManagmentSystem:
    def __init__(self):
        self.root = root
        root.title("Hotel Management System")
        root.geometry("1550x880+0+0")
        
        # ====================== logo ======================
        logo=Image.open("logo.png")
        logo=logo.resize((230,140),Image.ANTIALIAS)
        self.photologo=ImageTk.PhotoImage(logo)

        lbl_title=Label(image=self.photologo,bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=230,height=140) 
        # ====================== 1st image ======================
        img1=Image.open("hotel.jpg")
        img1=img1.resize((1550,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lbl_title=Label(image=self.photoimg1,bd=4,relief=RIDGE)
        lbl_title.place(x=230,y=0,width=1320,height=140) 
        # ====================== title ======================
        lbl_title=Label(text="Hotel Management System",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE) 
        lbl_title.place(x=0,y=140,width=1550,height=50)     

        # ====================== main frame ======================
        main_frame=Frame(root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=750)

        # ====================== menu ======================
        lbl_menu=Label(main_frame,text="Menu",font=("times new roman",20,"bold"),bg="black",fg="gold")
        lbl_menu.place(x=0,y=0,width=230)

        # ====================== btn frame ======================
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=115)

        cust_btn=Button(btn_frame,text="Customer",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,text="Book Room",command=self.roombooking,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        room_btn.grid(row=1,column=0,pady=1)

        detailes_btn=Button(btn_frame,text="Room Detailes",command=self.detailsRoom,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        detailes_btn.grid(row=2,column=0,pady=1) 
        

    def cust_details(self):
        self.new_window=Toplevel(root)
        self.app=customer(self.new_window)

    def roombooking(self):
        self.new_window=Toplevel(root)
        self.app=roombooking(self.new_window)

    def detailsRoom(self):
        self.new_window=Toplevel(root)
        self.app=detailsRoom(self.new_window)        


if __name__=="__main__":
    root = Tk()
    obj=HotelManagmentSystem()
    root.mainloop()

