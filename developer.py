from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1450x695+0+0")
        self.root.title("Face Recognition System")

        title_label=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="#FFFCCC",fg="BLUE" )
        title_label.place(x=0,y=0,width=1490,height=45)

        img_top=Image.open(r"collage_images\deve.jpg")
        img_top=img_top.resize((1450,695),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1450,height=695)

        #frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=900,y=50,width=400,height=500)

        img_dev=Image.open(r"collage_images\dev.jpg")
        img_dev=img_dev.resize((200,200),Image.ANTIALIAS)
        self.photoimg_dev=ImageTk.PhotoImage(img_dev)

        f_lbl=Label(main_frame,image=self.photoimg_dev)
        f_lbl.place(x=200,y=0,width=200,height=200)

        #Developer info
        dev_label=Label(main_frame,text='"Final Year Project"',font=("times new roman",13,"bold"),bg="white",fg="blue")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame,text="Computer Enginnering",font=("times new roman",12,"bold"),bg="white",fg="blue")
        dev_label.place(x=0,y=25)

        dev_label=Label(main_frame,text="Developed By,",font=("times new roman",12,"bold"),bg="white",fg="blue")
        dev_label.place(x=0,y=45)

        dev_label=Label(main_frame,text="1.Uma Yerjal",font=("times new roman",12,"bold"),bg="white",fg="blue")
        dev_label.place(x=0,y=65)

        dev_label=Label(main_frame,text="2.Nehashri Raccha",font=("times new roman",12,"bold"),bg="white",fg="blue")
        dev_label.place(x=0,y=85)

        dev_label=Label(main_frame,text="3.Ashwini Bandari",font=("times new roman",12,"bold"),bg="white",fg="blue")
        dev_label.place(x=0,y=105)

        dev_label=Label(main_frame,text="4.Sagar Mane",font=("times new roman",12,"bold"),bg="white",fg="blue")
        dev_label.place(x=0,y=125)

        dev_label=Label(main_frame,text="5.Shreya Chavan",font=("times new roman",12,"bold"),bg="white",fg="blue")
        dev_label.place(x=0,y=145)

        dev_label=Label(main_frame,text="6.Prachi Vittalkar",font=("times new roman",12,"bold"),bg="white",fg="blue")
        dev_label.place(x=0,y=165)

        img_top1=Image.open(r"collage_images\dev1.jpg")
        img_top1=img_top1.resize((400,300),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=0,y=210,width=400,height=300)


if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()