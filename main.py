from time import strftime
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
from tkinter import messagebox
import tkinter
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x780+0+0") #Window Screen Size
        self.root.title("Face Recognition System")

        #first image
        img=Image.open(r"collage_images\b.jpg")
        img=img.resize((480,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=480,height=130)

        #second image
        img1=Image.open(r"collage_images\a.jpg")
        img1=img1.resize((480,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=480,y=0,width=480,height=130)

        #third image
        img2=Image.open(r"collage_images\c.jpg")
        img2=img2.resize((480,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=960,y=0,width=480,height=130)

        #bg image
        img3=Image.open(r"collage_images\bg.jpg")
        img3=img3.resize((1490,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_lbl=Label(self.root,image=self.photoimg3)
        bg_lbl.place(x=0,y=130,width=1490,height=710)

        title_label=Label(bg_lbl,text="FACE RECOGNITION ATTENDANCE SYSTEM ",font=("times new roman",35,"bold"),bg="white",fg="red",)
        title_label.place(x=0,y=0,width=1490,height=45)

        # =============== time ================
        def time():
            string=strftime('%H:%M:%S %p')
            f_lbl.config(text = string)
            f_lbl.after(1000, time)

        f_lbl=Label(title_label,font=('times new roman',14,'bold'),bg="white",fg="blue")
        f_lbl.place(x=0,y=0,width=110,height=50)
        time()

        #student button
        img4=Image.open(r"collage_images\sb.jpg")
        img4=img4.resize((200,180),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_lbl,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=80,width=200,height=180)

        b1_1=Button(bg_lbl,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=260,width=200,height=40)

        #Detect Face button
        img5=Image.open(r"collage_images\fb.jpg")
        img5=img5.resize((200,180),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_lbl,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=450,y=80,width=200,height=180)

        b1_1=Button(bg_lbl,text="Fece Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=450,y=260,width=200,height=40)

        #Attendance button
        img6=Image.open(r"collage_images\sa.jpg")
        img6=img6.resize((200,180),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_lbl,image=self.photoimg6,cursor="hand2",command=self.attendatnce_data)
        b1.place(x=700,y=80,width=200,height=180)

        b1_1=Button(bg_lbl,text="Attendance",cursor="hand2",command=self.attendatnce_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=700,y=260,width=200,height=40)

        
        #Helf button
        img7=Image.open(r"collage_images\hd.jpg")
        img7=img7.resize((200,180),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_lbl,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=950,y=80,width=200,height=180)

        b1_1=Button(bg_lbl,text="Helf Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=950,y=260,width=200,height=40)

        #Train button
        img8=Image.open(r"collage_images\train.jpg")
        img8=img8.resize((200,180),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_lbl,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=330,width=200,height=180)

        b1_1=Button(bg_lbl,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=500,width=200,height=40)

        
        #Photo button
        img9=Image.open(r"collage_images\photo.jpg")
        img9=img9.resize((200,180),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_lbl,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=450,y=330,width=200,height=180)

        b1_1=Button(bg_lbl,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=450,y=500,width=200,height=40)

        #Developer button
        img10=Image.open(r"collage_images\dev.jpg")
        img10=img10.resize((200,180),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_lbl,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=700,y=330,width=200,height=180)

        b1_1=Button(bg_lbl,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=700,y=500,width=200,height=40)

        #Exit button
        img11=Image.open(r"collage_images\exit.jpg")
        img11=img11.resize((200,180),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_lbl,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=950,y=330,width=200,height=180)

        b1_1=Button(bg_lbl,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=950,y=500,width=200,height=40)

    def open_img(self):
        os.startfile("data")


        # ================================ Function Button=====================

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    # ========================================= train button==============
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    # ========================face button ==================
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    # ======================== attendance button ==================
    def attendatnce_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    # ======================== Developer button ==================
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    # ======================== Help Desk button ==================
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

    # =============== Exit Button ======================
    def iExit(self):
        self.iExit=messagebox.askyesno("Face Recognition","Are you sure exit this Project",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return



if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()