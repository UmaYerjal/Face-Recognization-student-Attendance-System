from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2
from mysql.connector.fabric import connect

class Register:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1450x695+0+0")
        self.root.title("Face Recognition System")

        # =====================variable =========================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_ques=StringVar()
        self.var_ans=StringVar()
        self.var_pass=StringVar()
        self.var_cpass=StringVar()
        self.var_check=StringVar()

        #backgraound image
        img_top=Image.open(r"collage_images\regback.jpg")
        img_top=img_top.resize((1450,695),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=0,width=1450,height=695)

        #frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=300,y=100,width=900,height=500)

        #left side image
        img_top1=Image.open(r"collage_images\reg1.jpg")
        img_top1=img_top1.resize((300,500),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        lblimg=Label(main_frame,image=self.photoimg_top1)
        lblimg.place(x=0,y=0,width=300,height=500)

        title_label=Label(main_frame,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="green")
        title_label.place(x=320,y=5)

        #first name
        name_label=Label(main_frame,text="First Name",font=("times new roman",13,"bold"),bg="white",fg="black")
        name_label.place(x=340,y=50)

        name_entry=ttk.Entry(main_frame,width=28,textvariable=self.var_fname,font=("times new roman",11,"bold"))
        name_entry.place(x=340,y=75)

        #last name
        name_label=Label(main_frame,text="Last Name",font=("times new roman",13,"bold"),bg="white",fg="black")
        name_label.place(x=620,y=50)

        name_entry=ttk.Entry(main_frame,width=28,textvariable=self.var_lname,font=("times new roman",11,"bold"))
        name_entry.place(x=620,y=75)

        #contact
        contact_label=Label(main_frame,text="Contact No",font=("times new roman",13,"bold"),bg="white",fg="black")
        contact_label.place(x=340,y=120)

        contact_entry=ttk.Entry(main_frame,width=28,textvariable=self.var_contact,font=("times new roman",11,"bold"))
        contact_entry.place(x=340,y=145)

        #Email
        email_label=Label(main_frame,text="Email",font=("times new roman",13,"bold"),bg="white",fg="black")
        email_label.place(x=620,y=120)

        email_entry=ttk.Entry(main_frame,width=28,textvariable=self.var_email,font=("times new roman",11,"bold"))
        email_entry.place(x=620,y=145)

        #select security question
        question_label=Label(main_frame,text="Select Security Questions",font=("times new roman",13,"bold"),bg="white",fg="black")
        question_label.place(x=340,y=190)

        question_combo=ttk.Combobox(main_frame,font=("times new roman",11,"bold"),textvariable=self.var_ques,state="read only",width=26)
        question_combo["values"]=("Select Question","Your Birth Palce","Best Friend Name","Your Pet Name")
        question_combo.current(0)
        question_combo.place(x=340,y=218)

        #security answer
        answer_label=Label(main_frame,text="Security Answer",font=("times new roman",13,"bold"),bg="white",fg="black")
        answer_label.place(x=620,y=190)

        answer_entry=ttk.Entry(main_frame,width=28,textvariable=self.var_ans,font=("times new roman",11,"bold"))
        answer_entry.place(x=620,y=218)

        #password
        pass_label=Label(main_frame,text="Password",font=("times new roman",13,"bold"),bg="white",fg="black")
        pass_label.place(x=340,y=265)

        pass_entry=ttk.Entry(main_frame,width=28,textvariable=self.var_pass,font=("times new roman",11,"bold"))
        pass_entry.place(x=340,y=290)

        #conform password
        con_pass_label=Label(main_frame,text="Confirm Password",font=("times new roman",13,"bold"),bg="white",fg="black")
        con_pass_label.place(x=620,y=265)

        con_pass_entry=ttk.Entry(main_frame,width=28,textvariable=self.var_cpass,font=("times new roman",11,"bold"))
        con_pass_entry.place(x=620,y=290)
        
        #check button
        checkbtn=Checkbutton(main_frame,text="I Agree The Terms & Conditions",variable=self.var_check,font=("times new roman",11,"bold"),onvalue=1,offvalue=0,bg="#D9D9D9")
        checkbtn.place(x=340,y=330)

        #register Button
        img=Image.open(r"collage_images\regbtn.jpg")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        b1=Button(main_frame,image=self.photoimg,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=340,y=360,width=200,height=100)

        #login btn
        img_reg=Image.open(r"collage_images\loginbtn.jpg")
        img_reg=img_reg.resize((200,90),Image.ANTIALIAS)
        self.photoimg_reg=ImageTk.PhotoImage(img_reg)

        b1=Button(main_frame,image=self.photoimg_reg,borderwidth=0,cursor="hand2")
        b1.place(x=620,y=380,width=200,height=90)

    #=============================function declaration=================

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_ques.get()=="Select Question":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_cpass.get():
            messagebox.showerror("Error","Password and Confirm Password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Plese agree our Terms and Condition")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Um@kom@l05",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already Exits, plese try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(

                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_ques.get(),
                                                                                        self.var_ans.get(),
                                                                                        self.var_pass.get()
                                                                                        ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Suceess","Register Successfully")


    





        

        

if __name__ == "__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()