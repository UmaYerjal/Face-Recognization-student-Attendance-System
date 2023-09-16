from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1450x695+0+0")
        self.root.title("Face Recognition System")


        # ============================= variable ===============================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()

        


        #first image
        img=Image.open(r"collage_images\studentA.jpg")
        img=img.resize((480,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=480,height=130)

        #second image
        img1=Image.open(r"collage_images\s2.jpg")
        img1=img1.resize((480,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=480,y=0,width=480,height=130)

        #third image
        img2=Image.open(r"collage_images\s3.jpg")
        img2=img2.resize((480,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=960,y=0,width=480,height=130)

        #bg image
        img3=Image.open(r"collage_images\back.jpg")
        img3=img3.resize((1490,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_lbl=Label(self.root,image=self.photoimg3)
        bg_lbl.place(x=0,y=130,width=1490,height=710)

        title_label=Label(bg_lbl,text="STUDENT MANAGEMENT SYSTEM ",font=("times new roman",35,"bold"),bg="white",fg="BLUE" )
        title_label.place(x=0,y=0,width=1490,height=45)

        main_frame=Frame(bg_lbl,bd=2,bg="white")
        main_frame.place(x=10,y=50,width=1330,height=520)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg="#D9D9D9",text="Student Details",font=("times new roman",12,"bold"),fg="green")
        Left_frame.place(x=20,y=10,width=640,height=490)

        img_left=Image.open(r"collage_images\stub.jpg")
        img_left=img_left.resize((600,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=15,y=5,width=600,height=100)

        #currentcourse
        current_course_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,bg="#D9D9D9",text="Current Course Information",font=("times new roman",12,"bold"),fg="green")
        current_course_frame.place(x=12,y=105,width=600,height=100)
        
        #Depaertment
        dep_label=Label(current_course_frame,text="Department:",font=("times new roman",10,"bold"),bg="#D9D9D9")
        dep_label.grid(row=0,column=0,padx=2,pady=5,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",10,"bold"),state="read only",width=20)
        dep_combo["values"]=("Select Department","Computer","Electronic","Mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        #Course
        course_label=Label(current_course_frame,text="Course:",font=("times new roman",11,"bold"),bg="#D9D9D9")
        course_label.grid(row=0,column=2,padx=20,pady=5,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",11,"bold"),state="read only",width=20)
        course_combo["values"]=("Select Course","First Year","Secong year","Third Year")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=0,pady=5,sticky=W)

        #Year
        year_label=Label(current_course_frame,text="Year:",font=("times new roman",11,"bold"),bg="#D9D9D9")
        year_label.grid(row=1,column=0,padx=2,pady=5,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",11,"bold"),state="read only",width=20)
        year_combo["values"]=("Select Year","2020-12","2021-22","2022-23")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W)

        #semester
        semester_label=Label(current_course_frame,text="Semester:",font=("times new roman",11,"bold"),bg="#D9D9D9")
        semester_label.grid(row=1,column=2,padx=20,pady=5,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",11,"bold"),state="read only",width=20)
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=0,pady=10,sticky=W)


        #Class informatin
        class_student_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,bg="#D9D9D9",text="Class Student Information",font=("times new roman",12,"bold"),fg="green")
        class_student_frame.place(x=12,y=205,width=600,height=260)

        #Student Id
        studentId_label=Label(class_student_frame,text="StudentId:",font=("times new roman",11,"bold"),bg="#D9D9D9")
        studentId_label.grid(row=0,column=0,padx=10,sticky=W)

        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=18,font=("times new roman",11,"bold"))
        studentId_entry.grid(row=0,column=1,padx=0,pady=5,sticky=W)

        #Student name
        studentname_label=Label(class_student_frame,text="Student Name:",font=("times new roman",11,"bold"),bg="#D9D9D9")
        studentname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentname_entry=ttk.Entry(class_student_frame,textvariable=self.var_name,width=18,font=("times new roman",11,"bold"))
        studentname_entry.grid(row=0,column=3,padx=0,pady=5,sticky=W)

        #Class Division
        class_division_label=Label(class_student_frame,text="Class Division:",font=("times new roman",11,"bold"),bg="#D9D9D9")
        class_division_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)


        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",11,"bold"),state="read only",width=16)
        div_combo["values"]=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=0,pady=5,sticky=W)

        #Roll No
        roll_no_label=Label(class_student_frame,text="Roll No:",font=("times new roman",11,"bold"),bg="#D9D9D9")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=18,font=("times new roman",11,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=0,pady=5,sticky=W)

        #Gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",11,"bold"),bg="#D9D9D9")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",11,"bold"),state="read only",width=16)
        gender_combo["values"]=("Male","Female","other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=0,pady=5,sticky=W)

        #DOB
        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",11,"bold"),bg="#D9D9D9")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=18,font=("times new roman",11,"bold"))
        dob_entry.grid(row=2,column=3,padx=0,pady=5,sticky=W)

        #Email
        email_label=Label(class_student_frame,text="Email:",font=("times new roman",11,"bold"),bg="#D9D9D9")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=18,font=("times new roman",11,"bold"))
        email_entry.grid(row=3,column=1,padx=0,pady=5,sticky=W)

        #Address
        adress_label=Label(class_student_frame,text="Address:",font=("times new roman",11,"bold"),bg="#D9D9D9")
        adress_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        adress_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=18,font=("times new roman",11,"bold"))
        adress_entry.grid(row=3,column=3,padx=0,pady=5,sticky=W)

        #radio Button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=4,column=0)

        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=4,column=1,padx=10,pady=0,sticky=W)

        #buttons frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="#D9D9D9")
        btn_frame.place(x=5,y=158,width=585,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=13,font=("times new roman",13,"bold"),bg="green",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=14,font=("times new roman",13,"bold"),bg="green",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=14,font=("times new roman",13,"bold"),bg="green",fg="white")
        delete_btn.grid(row=0,column=3)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=13,font=("times new roman",13,"bold"),bg="green",fg="white")
        reset_btn.grid(row=0,column=4)

        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="#D9D9D9")
        btn_frame.place(x=5,y=193,width=585,height=35)

        take_photo_btn=Button(btn_frame,text="Take Photo Sample",width=28,command=self.generate_dataset,font=("times new roman",13,"bold"),bg="green",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame,text="Update Photo Sample",width=28,font=("times new roman",13,"bold"),bg="green",fg="white")
        update_photo_btn.grid(row=0,column=1)


        #Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg="#D9D9D9",text="Student Details",font=("times new roman",12,"bold"),fg="green")
        Right_frame.place(x=670,y=10,width=640,height=490)

        img_right=Image.open(r"collage_images\stu.jpg")
        img_right=img_right.resize((600,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=15,y=5,width=600,height=100)


        # ===============Search System==================
        search_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,bg="#D9D9D9",text="Search System",font=("times new roman",12,"bold"),fg="green")
        search_frame.place(x=12,y=105,width=610,height=65)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="#60C5F1")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="read only",width=13)
        search_combo["values"]=("Select ","Roll_No","StudentId")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=0,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=16,font=("times new roman",11,"bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",width=11,font=("times new roman",11,"bold"),bg="green",fg="white")
        search_btn.grid(row=0,column=3,padx=2)

        showAll_btn=Button(search_frame,text="Show All",width=11,font=("times new roman",11,"bold"),bg="green",fg="white")
        showAll_btn.grid(row=0,column=4,padx=2)

        # ===================== Tabel Frame ==================
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="#D9D9D9")
        table_frame.place(x=12,y=175,width=610,height=285)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","roll","gender","dob","email","address","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll_No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("photo",text="Photos")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # ============================= Fuction Declaration ==================================

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="admin",database="face_recognization",auth_plugin='mysql_native_password')
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(                                                                                  
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_course.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_semester.get(),
                                                                                                        self.var_std_id.get(),
                                                                                                        self.var_name.get(),
                                                                                                        self.var_div.get(),
                                                                                                        self.var_roll.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_radio1.get()
                                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","student details has been added successfully",parent=self.root)                                                                                  
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)    

    # =================================== fetch data ==================================           
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="admin",database="face_recognization",auth_plugin='mysql_native_password')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # ========================================= get cursor ====================================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_address.set(data[11]),
        self.var_radio1.set(data[12])

    # =========================== update data ===========================
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Upadate=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Upadate>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="admin",database="face_recognization",auth_plugin='mysql_native_password')
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Address=%s,PhotoSample=%s where Student_id=%s",(

                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                            self.var_semester.get(),
                                                                                                                                                                            self.var_name.get(),
                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                            self.var_std_id.get()

                                                                                                                                                                                         ))
                else:
                    if not Upadate:
                        return
                messagebox.showinfo("Success","student details successfully Updated completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)   




    # ============================== Delete Function ===================================
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student data",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="admin",database="face_recognization",auth_plugin='mysql_native_password')
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted Student Details",parent=self.root)
            except Exception as es:
                    messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    # ========================================= Reset data ============================================
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_radio1.set("")              

    # ============================== Generate data set Take Photo Samples ======================
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="admin",database="face_recognization",auth_plugin='mysql_native_password')
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Address=%s,PhotoSample=%s where Student_id=%s",(

                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                            self.var_semester.get(),
                                                                                                                                                                            self.var_name.get(),
                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                            self.var_std_id.get()==id+1

                                                                                                                                                                         ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
            
                #=================== Load predifiend data on face frontal from opencv =====================

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    # scaling factor=1.3
                    # Minimun neighbor=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("crooped face",face)
                                                                                                                             
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets Completed!!!!!")
            except Exception as es:
                    messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

        


if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()