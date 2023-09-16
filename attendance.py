from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog



mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1450x695+0+0")
        self.root.title("Face Recognition System")

        # variables
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()


        #first image
        img=Image.open(r"collage_images\studentA.jpg")
        img=img.resize((715,150),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=715,height=150)

        #second image
        img1=Image.open(r"collage_images\atte.jpg")
        img1=img1.resize((715,150),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=715,y=0,width=715,height=150)

        #bg image
        img3=Image.open(r"collage_images\back.jpg")
        img3=img3.resize((1490,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_lbl=Label(self.root,image=self.photoimg3)
        bg_lbl.place(x=0,y=150,width=1490,height=710)

        title_label=Label(bg_lbl,text="ATTENDANCE MANAGEMENT SYSTEM ",font=("times new roman",35,"bold"),bg="white",fg="green" )
        title_label.place(x=0,y=0,width=1490,height=45)

        # frame
        main_frame=Frame(bg_lbl,bd=2,bg="white")
        main_frame.place(x=10,y=50,width=1330,height=500)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg="#D9D9D9",text="Student Attendance Details",font=("times new roman",12,"bold"),fg="blue")
        Left_frame.place(x=20,y=10,width=640,height=470)

        img_left=Image.open(r"collage_images\stub.jpg")
        img_left=img_left.resize((600,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=15,y=5,width=600,height=100)
        
        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="#D9D9D9")
        left_inside_frame.place(x=12,y=120,width=600,height=320)

        #label entry
        #AattendaceId Id
        attendaceId_label=Label(left_inside_frame,text="AttendanceID:",font=("times new roman",11,"bold"),bg="#D9D9D9")
        attendaceId_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        attendaceId_entry=ttk.Entry(left_inside_frame,width=18,textvariable=self.var_atten_id,font=("times new roman",11,"bold"))
        attendaceId_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        #Roll No
        roll_no_label=Label(left_inside_frame,text="Roll:",font=("times new roman",11,"bold"),bg="#D9D9D9")
        roll_no_label.grid(row=0,column=2,padx=10,pady=10,sticky=W)

        roll_no_entry=ttk.Entry(left_inside_frame,width=18,textvariable=self.var_atten_roll,font=("times new roman",11,"bold"))
        roll_no_entry.grid(row=0,column=3,padx=10,pady=10,sticky=W)

        #Student name
        studentname_label=Label(left_inside_frame,text="Student Name:",font=("times new roman",11,"bold"),bg="#D9D9D9")
        studentname_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        studentname_entry=ttk.Entry(left_inside_frame,width=18,textvariable=self.var_atten_name,font=("times new roman",11,"bold"))
        studentname_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Depaertment
        dep_label=Label(left_inside_frame,text="Department:",font=("times new roman",10,"bold"),bg="#D9D9D9")
        dep_label.grid(row=1,column=2,padx=2,pady=5,sticky=W)

        studentname_entry=ttk.Entry(left_inside_frame,width=18,textvariable=self.var_atten_dep,font=("times new roman",11,"bold"))
        studentname_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        

        #Time
        time_label=Label(left_inside_frame,text="Time:",font=("times new roman",10,"bold"),bg="#D9D9D9")
        time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        timename_entry=ttk.Entry(left_inside_frame,width=18,textvariable=self.var_atten_time,font=("times new roman",11,"bold"))
        timename_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #Date
        date_label=Label(left_inside_frame,text="Date:",font=("times new roman",10,"bold"),bg="#D9D9D9")
        date_label.grid(row=2,column=2,padx=2,pady=5,sticky=W)

        date_entry=ttk.Entry(left_inside_frame,width=18,textvariable=self.var_atten_date,font=("times new roman",11,"bold"))
        date_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #attendace
        attendace_label=Label(left_inside_frame,text="Attendance Status:",font=("times new roman",11,"bold"),bg="#D9D9D9")
        attendace_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        attendace_combo=ttk.Combobox(left_inside_frame,state="read only",textvariable=self.var_atten_attendance,font=("times new roman",11,"bold"),width=16)
        attendace_combo["values"]=("Status","Present","Absent")
        attendace_combo.current(0)
        attendace_combo.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #buttons frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="#D9D9D9")
        btn_frame.place(x=5,y=250,width=585,height=35)

        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,font=("times new roman",13,"bold"),width=13,bg="green",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,font=("times new roman",13,"bold"),width=14,bg="green",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",font=("times new roman",13,"bold"),width=14,bg="green",fg="white")
        delete_btn.grid(row=0,column=3)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,font=("times new roman",13,"bold"),width=13,bg="green",fg="white")
        reset_btn.grid(row=0,column=4)

        


        #Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg="#D9D9D9",text="Attendance Details",font=("times new roman",12,"bold"),fg="blue")
        Right_frame.place(x=670,y=10,width=640,height=470)

        right_inside_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="#D9D9D9")
        right_inside_frame.place(x=10,y=5,width=615,height=435)

        # ================================= scroll bar table ============================
        scroll_x=ttk.Scrollbar(right_inside_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(right_inside_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(right_inside_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll NO")
        self.AttendanceReportTable.heading("name",text="Student Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=150)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)


        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    #====================== fetch data ==========================
    def fetch_data(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    #import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV file","*.csv"),("ALl file","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)

    #export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("NO Data","No data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV file","*.csv"),("ALl file","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data Export to"+os.path.basename(fln)+"Successfully Export data")
        except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])
    # reset data
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")

        
        






if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()