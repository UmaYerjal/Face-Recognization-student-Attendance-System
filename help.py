from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1450x695+0+0")
        self.root.title("Face Recognition System")

        title_label=Label(self.root,text="Help Desk",font=("times new roman",35,"bold"),bg="#FFFCCC",fg="BLUE" )
        title_label.place(x=0,y=0,width=1490,height=45)

        img_top=Image.open(r"collage_images\help.jpg")
        img_top=img_top.resize((1450,695),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1450,height=695)

        dev_label=Label(f_lbl,text='Email: yerjaluma2003@gmail.com',font=("times new roman",18,"bold"),bg="white",fg="green")
        dev_label.place(x=550,y=200)

if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()