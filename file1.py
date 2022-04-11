from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x400+0+0")
        self.root.title("Title")
        
        #Image_1
        img=Image.open(r'student.jpg')        
        img=img.resize((540,160),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        self.btn_1=Button(self.root,image=self.photoimg,cursor="hand2")
        self.btn_1.place(x=0,y=0,width=440,height=160)
        
        #Image_2
        img_2=Image.open(r'student.jpg')        
        img_2=img_2.resize((540,160),Image.ANTIALIAS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)
        
        self.btn_2=Button(self.root,image=self.photoimg_2,cursor="hand2")
        self.btn_2.place(x=440,y=0,width=540,height=160)
        
        #Image_3
        img_3=Image.open(r'student.jpg')        
        img_3=img_3.resize((540,160),Image.ANTIALIAS)
        self.photoimg_3=ImageTk.PhotoImage(img_3)
        
        self.btn_3=Button(self.root,image=self.photoimg_3,cursor="hand2")
        self.btn_3.place(x=900,y=0,width=540,height=160)
        
        #Background
        img_4=Image.open(r'student.jpg')        
        img_4=img_4.resize((540,160),Image.ANTIALIAS)
        self.photoimg_4=ImageTk.PhotoImage(img_4)
        
        bg_lbl=Label(self.root,image=self.photoimg_4,bd=2,relief=RIDGE)
        bg_lbl.place(x=0,y=160,width=1530,height=710)
        
        lbl_title=Label(bg_lbl,text="Student Management System",font=("times new roman",37,"bold"),fg="blue",bg="white")
        lbl_title.place(x=0,y=0,width=1530,height=50)
        
        #manage Frame
        Manage_Frame=Frame(bg_lbl,bd=2,relief=RIDGE,bg="white")
        Manage_Frame.place(x=15,y=55,width=1500,height=560)
        
        #left Frame
        DataLeftFrame=LabelFrame(Manage_Frame,bd=4,relief=RIDGE,padx=2,text="Student Information",font=("times new roman",20))
        DataLeftFrame.place(x=10,y=10,width=660,height=540)
        
        img_5=Image.open(r'student.jpg')        
        img_5=img_5.resize((650,120),Image.ANTIALIAS)
        self.photoimg_5=ImageTk.PhotoImage(img_5)
        
        my_img=Label(DataLeftFrame,image=self.photoimg_5,bd=2,relief=RIDGE)
        my_img.place(x=0,y=80,width=650,height=120)
        
        #Current Course LabelFrame Information
        std_lbl_info_frame=LabelFrame(Manage_Frame,bd=4,relief=RIDGE,padx=2,text="Current Course Information",font=("times new roman",20))
        std_lbl_info_frame.place(x=16,y=36,width=650,height=115)
        
        #Department
        lbl_dep=Label(std_lbl_info_frame,text="Department",font=("arial",12,"bold"),bg="white")
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)
        
        combo_dep=ttk.Combobox(std_lbl_info_frame,font=("arial",12,"bold"),width=17,state="readonly")
        combo_dep["value"]=("Select Department","Computer","IT","Civil")
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        #Course 
        course_std=Label(std_lbl_info_frame,text="Courses",font=("arial",12,"bold"),bg="white")
        course_std.grid(row=0,column=2,padx=2,pady=10,sticky=W)
        
        com_txtcourse_std=ttk.Combobox(std_lbl_info_frame,font=("arial",12,"bold"),width=17,state="readonly")
        com_txtcourse_std["value"]=("Select Courses","FE","SE","TE","BE")
        com_txtcourse_std.current(0)
        com_txtcourse_std.grid(row=0,column=3,sticky=W,padx=2,pady=10)
        
        #Year 
        current_year=Label(std_lbl_info_frame,font=("arial",12,"bold"),text="Year",bg="white")
        current_year.grid(row=1,column=0,sticky=W,padx=2,pady=10)
        
        com_txt_current_year=ttk.Combobox(std_lbl_info_frame,font=("arial",12,"bold"),width=17,state="readonly")
        com_txt_current_year["value"]=("Select Year","2021","2020","2019","2018","2017","2016","2015","2014")
        com_txt_current_year.current(0)
        com_txt_current_year.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        
        #Semester 
        label_Semester=Label(std_lbl_info_frame,text="Semester",font=("arial",12,"bold"),bg="white")
        label_Semester.grid(row=1,column=2,padx=2,pady=10,sticky=W)
        
        comSemester=ttk.Combobox(std_lbl_info_frame,font=("arial",12,"bold"),width=17,state="readonly")
        comSemester["value"]=("Select Semester","Semester-1","Semester-2")
        comSemester.current(0)
        comSemester.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        
        #Current Course LabelFrame Information
        std_lbl_class_frame=LabelFrame(DataLeftFrame,bd=4,relief=RIDGE,padx=2,text="Class Course Information",font=("times new roman",20))
        std_lbl_class_frame.place(x=0,y=160,width=650,height=250)
        
        #Labels Entry
        
        #ID
        lbl_id=Label(std_lbl_class_frame,text="Student ID",font=("arial",12,"bold"),bg="white")
        lbl_id.grid(row=0,column=0,padx=2,sticky=W,pady=7)
        
        id_entry=ttk.Entry(std_lbl_class_frame,font=("arial",12,"bold"),width=22)
        id_entry.grid(row=0,column=1,sticky=W,padx=2,pady=7)
        
        #Name
        lbl_name=Label(std_lbl_class_frame,text="Name",font=("arial",12,"bold"),bg="white")
        lbl_name.grid(row=0,column=2,padx=2,sticky=W,pady=7)
        
        txt_name=ttk.Entry(std_lbl_class_frame,font=("arial",12,"bold"),width=22)
        txt_name.grid(row=0,column=3,sticky=W,padx=2,pady=7)
        
        #Divison
        lbl_div=Label(std_lbl_class_frame,text="Class Divison",font=("arial",12,"bold"),bg="white")
        lbl_div.grid(row=1,column=0,padx=2,sticky=W,pady=7)
        
        com_txt_div=ttk.Combobox(std_lbl_class_frame,font=("arial",12,"bold"),width=18,state="readonly")
        com_txt_div["value"]=("Select Division","A","B","C")
        com_txt_div.current(0)
        com_txt_div.grid(row=1,column=1,padx=2,sticky=W,pady=7)
        
        #Roll
        lbl_roll=Label(std_lbl_class_frame,text="Roll No:",font=("arial",12,"bold"),bg="white")
        lbl_roll.grid(row=1,column=2,padx=2,sticky=W,pady=7)
        
        txt_roll=ttk.Entry(std_lbl_class_frame,font=("arial",12,"bold"),width=22)
        txt_roll.grid(row=1,column=3,sticky=W,padx=2,pady=7)
        
        #Gender
        lbl_gender=Label(std_lbl_class_frame,text="Gender:",font=("arial",12,"bold"),bg="white")
        lbl_gender.grid(row=2,column=0,padx=2,sticky=W,pady=7)
        
        com_txt_gender=ttk.Combobox(std_lbl_class_frame,font=("arial",12,"bold"),width=18,state="readonly")
        com_txt_gender["value"]=("Male","Female","Other")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=2,column=1,sticky=W,padx=2,pady=7)
        
        #DOB
        lbl_dob=Label(std_lbl_class_frame,text="DOB:",font=("arial",12,"bold"),bg="white")
        lbl_dob.grid(row=2,column=2,padx=2,sticky=W,pady=7)
        
        txt_dob=ttk.Entry(std_lbl_class_frame,font=("arial",12,"bold"),width=22)
        txt_dob.grid(row=2,column=3,sticky=W,padx=2,pady=7)
        
        #Email
        lbl_email=Label(std_lbl_class_frame,text="Email",font=("arial",12,"bold"),bg="white")
        lbl_email.grid(row=3,column=0,padx=2,sticky=W,pady=7)
        
        txt_email=ttk.Entry(std_lbl_class_frame,font=("arial",12,"bold"),width=22)
        txt_email.grid(row=3,column=1,sticky=W,padx=2,pady=7)
        
        #Phone
        lbl_phone=Label(std_lbl_class_frame,text="Phone No:",font=("arial",12,"bold"),bg="white")
        lbl_phone.grid(row=3,column=2,padx=2,sticky=W,pady=7)
        
        txt_phone=ttk.Entry(std_lbl_class_frame,font=("arial",12,"bold"),width=22)
        txt_phone.grid(row=3,column=3,sticky=W,padx=2,pady=7)
        
        #Address
        lbl_address=Label(std_lbl_class_frame,text="Address:",font=("arial",12,"bold"),bg="white")
        lbl_address.grid(row=4,column=0,padx=2,sticky=W,pady=7)
        
        txt_address=ttk.Entry(std_lbl_class_frame,font=("arial",12,"bold"),width=22)
        txt_address.grid(row=4,column=1,sticky=W,padx=2,pady=7)
        
        #Teacher
        lbl_teacher=Label(std_lbl_class_frame,text="Teacher Name:",font=("arial",12,"bold"),bg="white")
        lbl_teacher.grid(row=4,column=2,padx=2,sticky=W,pady=7)
        
        txt_teacher=ttk.Entry(std_lbl_class_frame,font=("arial",12,"bold"),width=22)
        txt_teacher.grid(row=4,column=3,sticky=W,padx=2,pady=7)
        
        #Button Frame
        btn_frame=Frame(DataLeftFrame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=388,width=650,height=38)
        
        btn_Add=Button(btn_frame,text="Save",font=("arial",11,"bold"),width=17,bg="blue",fg="white")
        btn_Add.grid(row=0,column=0,padx=1)        
        
        
        btn_Update=Button(btn_frame,text="Update",font=("arial",11,"bold"),width=17,bg="blue",fg="white")
        btn_Update.grid(row=0,column=1,padx=1)        
        
        
        btn_Delete=Button(btn_frame,text="Delete",font=("arial",11,"bold"),width=17,bg="blue",fg="white")
        btn_Delete.grid(row=0,column=2,padx=1)        
        
        
        btn_reset=Button(btn_frame,text="Reset",font=("arial",11,"bold"),width=17,bg="blue",fg="white")
        btn_reset.grid(row=0,column=3,padx=1)        
        
        #Right Frame
        DataRightFrame=LabelFrame(Manage_Frame,bd=4,relief=RIDGE,padx=2,text="Student Information",font=("times new roman",20))
        DataRightFrame.place(x=680,y=10,width=870,height=540)
        
        #Image1
        img_6=Image.open(r"student.jpg")
        img_6=img_6.resize((780,200),Image.ANTIALIAS)
        self.photoimg_6=ImageTk.PhotoImage(img_6)
        
        my_img=Label(DataRightFrame,image=self.photoimg_6,bd=2,relief=RIDGE)
        my_img.place(x=0,y=0,width=790,height=200)
        
        #Right Frame
        Search_Frame=LabelFrame(DataRightFrame,bd=4,relief=RIDGE,padx=2,text="Search Student Information",font=("times new roman",11,"bold"),fg="red",bg="white")
        Search_Frame.place(x=0,y=250,width=790,height=70)
        
        
        

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
 

