from os import close, terminal_size
from pathlib import WindowsPath
from tkinter import*
from tkinter import ttk
from tkinter import font
import tkinter
from tkinter.font import Font
from typing import Literal
from PIL import Image,ImageTk
from tkinter import messagebox
from cv2 import data
import mysql.connector
from mysql.connector import cursor 
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1450x695+0+0")
        self.root.title("Face Recognition System")

        title_label=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="#FFFCCC",fg="#CA151B" )
        title_label.place(x=0,y=0,width=1490,height=45)

        img_top=Image.open(r"collage_images\a.jpg")
        img_top=img_top.resize((1450,300),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1450,height=300)

        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="GREEN",fg="white")
        b1_1.place(x=0,y=350,width=1450,height=50)

        img_bottom=Image.open(r"collage_images\photo.jpg")
        img_bottom=img_bottom.resize((1450,300),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=400,width=1450,height=300)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]    

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')    #Gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        # ================== train the classifier and save =================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed")



if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()