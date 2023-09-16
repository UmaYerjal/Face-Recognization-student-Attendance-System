from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1450x695+0+0")
        self.root.title("Face Recognition System")

        img_top=Image.open(r"collage_images\stulogin.jpg")
        img_top=img_top.resize((1450,695),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=0,width=1450,height=695)

        #frame
        main_frame=Frame(f_lbl,bd=2,bg="black")
        main_frame.place(x=870,y=80,width=400,height=500)

        img_top1=Image.open(r"collage_images\icon.jpg")
        img_top1=img_top1.resize((100,100),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        lblimg=Label(self.root,image=self.photoimg_top1,bg="black")
        lblimg.place(x=1030,y=82,width=100,height=100)

        title_label=Label(main_frame,text="Get started ",font=("times new roman",20,"bold"),bg="black",fg="white")
        title_label.place(x=130,y=90)

        #label
        name_label=Label(main_frame,text="Username",font=("times new roman",18,"bold"),bg="black",fg="white")
        name_label.place(x=60,y=130)

        self.txtuser=ttk.Entry(main_frame,font=("times new roman",18,"bold"),width=28)
        self.txtuser.place(x=30,y=160)

        pass_label=Label(main_frame,text="Password",font=("times new roman",18,"bold"),bg="black",fg="white")
        pass_label.place(x=60,y=210)

        self.txtupass=ttk.Entry(main_frame,font=("times new roman",18,"bold"),width=28)
        self.txtupass.place(x=30,y=240)

        #icon
        img_top2=Image.open(r"collage_images\icon.jpg")
        img_top2=img_top2.resize((25,25),Image.ANTIALIAS)
        self.photoimg_top2=ImageTk.PhotoImage(img_top2)

        icon=Label(main_frame,image=self.photoimg_top2,bg="black")
        icon.place(x=30,y=130,width=25,height=25)

        img_top3=Image.open(r"collage_images\pass.jpg")
        img_top3=img_top3.resize((25,25),Image.ANTIALIAS)
        self.photoimg_top3=ImageTk.PhotoImage(img_top3)

        icon1=Label(main_frame,image=self.photoimg_top3,bg="black")
        icon1.place(x=30,y=210,width=25,height=25)

        # ========================== login Button ============================
        login_btn=Button(main_frame,text="Login",width=11,font=("times new roman",15,"bold"),command=self.login,bd=3,relief=RIDGE,bg="red",activeforeground="white",activebackground="red",fg="white")
        login_btn.place(x=140,y=300)

        # ========================== register Button ============================
        register_btn=Button(main_frame,text="New User Register",command=self.register_window,font=("times new roman",15,"bold"),borderwidth=0,bg="black",activeforeground="white",activebackground="black",fg="white")
        register_btn.place(x=60,y=360)

        img_top4=Image.open(r"collage_images\reg.jpg")
        img_top4=img_top4.resize((25,25),Image.ANTIALIAS)
        self.photoimg_top4=ImageTk.PhotoImage(img_top4)

        icon1=Label(main_frame,image=self.photoimg_top4,bg="black")
        icon1.place(x=30,y=360,width=25,height=25)


        # ========================== forget Button ============================
        forget_btn=Button(main_frame,text="Forgate password",command=self.forgot_password,font=("times new roman",15,"bold"),borderwidth=0,bg="black",activeforeground="white",activebackground="black",fg="white")
        forget_btn.place(x=60,y=400)

        img_top5=Image.open(r"collage_images\pass.jpg")
        img_top5=img_top5.resize((25,25),Image.ANTIALIAS)
        self.photoimg_top5=ImageTk.PhotoImage(img_top5)

        icon1=Label(main_frame,image=self.photoimg_top5,bg="black")
        icon1.place(x=30,y=400,width=25,height=25)


    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)



    def login(self):
        if self.txtuser.get()=="" or self.txtupass.get()=="":
            messagebox.showerror("Error","All fields are Required")

        elif self.txtuser.get()=="uma" and self.txtupass.get()=="1234":
            messagebox.showinfo("Success","Welcome to Face Recognition management system")

        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                        self.txt_email.get(),
                                                                                        self.var_pass.get()
                                                                                        ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.new_window)
                    self.app=Face_Recognition(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    # ====================== reset password ==========================
    def reset_pass(self):
        if self.var_.get()=="Select Question":
            messagebox.showerror("Error","Select Security Question")
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Plese Enter the Answer")
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Plese enter the new Password")

    # ============================== forget passward =========================
    
    def forgot_password(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Plese enter the email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)
            if row==None:
                messagebox.showerror("My Error","Plese enter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                
                title_label=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),bg="white",fg="green")
                title_label.place(x=0,y=10,relwidth=1)

                #select security question
                question_label=Label(self.root2,text="Select Security Questions",font=("times new roman",13,"bold"),bg="white",fg="black")
                question_label.place(x=50,y=50)

                question_combo=ttk.Combobox(self.root2,font=("times new roman",11,"bold"),state="read only",width=25)
                question_combo["values"]=("Select Question","Your Birth Palce","Best Friend Name","Your Pet Name")
                question_combo.current(0)
                question_combo.place(x=50,y=75)

                #security answer
                answer_label=Label(self.root2,text="Security Answer",font=("times new roman",13,"bold"),bg="white",fg="black")
                answer_label.place(x=50,y=120)

                answer_entry=ttk.Entry(self.root2,width=28,font=("times new roman",11,"bold"))
                answer_entry.place(x=50,y=145)

                #password
                pass_label=Label(self.root2,text="New Password",font=("times new roman",13,"bold"),bg="white",fg="black")
                pass_label.place(x=50,y=185)

                pass_entry=ttk.Entry(self.root2,width=28,font=("times new roman",11,"bold"))
                pass_entry.place(x=50,y=210)

                #button
                btn=Button(self.root2,text="Reset",width=15,font=("times new roman",13,"bold"),bg="green",fg="white")
                btn.place(x=90,y=270)
















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
            conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="mydata")
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
    main()