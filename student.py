
from email import message
from sqlite3 import Row
from tkinter import *
from tkinter import ttk
from tokenize import String
import pymysql
from tkinter import messagebox
class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Management System")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root, text = "Record Management System", bd=15, relief = GROOVE, font=("times new roman", 30, "bold"), bg="green", fg="#fff")
        title.pack(side = TOP, fill=X)

        #============All Variables===============================================

        self.admission_No_var = StringVar()
        self.name_var = StringVar()
        self.admission_No_var = StringVar()
        self.department_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        
        
        self.search_by=StringVar()
        self.search_txt=StringVar()


        #============Manage Frame===============================================
        Management_Frame = Frame(self.root, bd = 8, relief = RIDGE, bg="grey")
        Management_Frame.place(x = 20, y = 90, width=390, height=590)


        m_title = Label(Management_Frame, text ="Manage Students", bg="magenta",fg="#fff",font=("times new roman", 20, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        lbl_admission = Label(Management_Frame, text = "Admission No.", bg="grey", fg="#fff", font=("times new roman",15, "bold" ))
        lbl_admission.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        txt_admission = Entry(Management_Frame, textvariable=self.admission_No_var, font=("times new roman",13, "bold" ), bd = 5, relief=GROOVE)
        txt_admission.grid(row=1, column=1, pady=10, padx=2, sticky="w")

        lbl_department = Label(Management_Frame, text = "Department", bg="grey", fg="#fff", font=("times new roman",15, "bold" ))
        lbl_department.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        combo_department = ttk.Combobox(Management_Frame, textvariable= self.department_var, font=("times new roman",12, "bold" ), state="readonly")
        combo_department['values'] = ("ICT", "Business", "Tecnicals", "Humanity", "Hospitality")
        combo_department.grid(row=2, column=1, pady=10, padx=2, sticky="w")

        lbl_name = Label(Management_Frame, text = "Name", bg="grey", fg="#fff", font=("times new roman",15, "bold" ))
        lbl_name.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_name = Entry(Management_Frame,textvariable= self.name_var, font=("times new roman",13, "bold" ), bd = 5, relief=GROOVE)
        txt_name.grid(row=3, column=1, pady=10, padx=2, sticky="w")

        lbl_email = Label(Management_Frame, text = "Email", bg="grey", fg="#fff", font=("times new roman",15, "bold" ))
        lbl_email.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        txt_email = Entry(Management_Frame, textvariable= self.email_var, font=("times new roman",13, "bold" ), bd = 5, relief=GROOVE)
        txt_email.grid(row=4, column=1, pady=10, padx=2, sticky="w")

        lbl_gender = Label(Management_Frame, text = "Gender", bg="grey", fg="#fff", font=("times new roman",15, "bold" ))
        lbl_gender.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        combo_gender = ttk.Combobox(Management_Frame,textvariable= self.gender_var, font=("times new roman",12, "bold" ), state="readonly")
        combo_gender['values'] = ("male", "female", "other")
        combo_gender.grid(row=5, column=1, pady=10, padx=2, sticky="w")

        lbl_contact = Label(Management_Frame, text = "Contact", bg="grey", fg="#fff", font=("times new roman",15, "bold" ))
        lbl_contact.grid(row=6, column=0, pady=10,  padx=20,sticky="w")

        txt_contact = Entry(Management_Frame,textvariable= self.contact_var, font=("times new roman",13, "bold" ), bd = 5, relief=GROOVE)
        txt_contact.grid(row=6, column=1, pady=10, padx=2, sticky="w")

        lbl_dob = Label(Management_Frame, text = "D.O.B", bg="grey", fg="#fff", font=("times new roman",15, "bold" ))
        lbl_dob.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        txt_dob = Entry(Management_Frame,textvariable= self.dob_var, font=("times new roman",13, "bold" ), bd = 5, relief=GROOVE)
        txt_dob.grid(row=7, column=1, pady=10, padx=2, sticky="w")

        lbl_address = Label(Management_Frame, text = "Address", bg="grey", fg="#fff", font=("times new roman",15, "bold" ))
        lbl_address.grid(row=8, column=0, pady=10, padx=20, sticky="w")

        self.txt_address = Text(Management_Frame, width=23, height=4)
        self.txt_address.grid(row=8, column=1, pady=10, padx=2, sticky="w")

        #============Detail Frame===============================================
        btn_Frame = Frame(Management_Frame, bd=8, relief=RIDGE,bg="black")
        btn_Frame.place(x=0, y=537, width=380)

        Addbtn=Button(btn_Frame, text="Add", command=self.add_students, bg="orange", width=9).grid(row=0, column=0, padx=7)
        Updatebtn=Button(btn_Frame, text="Update", bg="blue", width=9,command=self.update_data).grid(row=0, column=1, padx=10)
        deletebtn=Button(btn_Frame, text="Delete", bg="yellow", width=9,command=self.delete_data).grid(row=0, column=2, padx=10)
        Clearbtn=Button(btn_Frame, text="Clear", bg="crimson", width=9, command=self.clear).grid(row=0, column=3, padx=10)

        #============Detail Frame===============================================
        Detail_Frame = Frame(self.root, bd = 4, relief = RIDGE, bg="black")
        Detail_Frame.place(x = 460, y = 90, width=800, height=590)

        lbl_search = Label(Detail_Frame, text = "Search By", bg="grey", fg="#fff", font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame,textvariable=self.search_by, width="15",font=("times new roman", 13, "bold"), state='readonly')
        combo_search['values'] = ("Admission_No", "Name", "Contact")
        combo_search.grid(row=0,column=1,padx=15,pady=0)

        txt_Search = Entry(Detail_Frame,textvariable=self.search_txt, width="15", font=("times new roman", 14, "bold"), bd=5, relief=GROOVE)
        txt_Search.grid(row=0, column=2, pady=10,padx=20, sticky="w")

        searchbtn = Button(Detail_Frame, text="Search", width=10, bg="cyan",command=self.search_data).grid(row=0, column=3, padx=10, pady=10)
        showallbtn = Button(Detail_Frame, text="Show All", bg="lime", width=10,command=self.fetch_data).grid(row=0, column=4, padx=10, pady=10)
        

        #============Table Frame===============================================

        Table_Frame = Frame(Detail_Frame, bd=6, relief=RIDGE, bg="grey")
        Table_Frame.place(x=10, y = 70, width=760, height=500)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Student_table = ttk.Treeview(Table_Frame, columns=("admission", "name", "department", "email", "gender", "contact", "dob", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y )
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("admission", text = "Admission No.")
        self.Student_table.heading("name", text = "Name")
        self.Student_table.heading("department", text = "Department")
        self.Student_table.heading("email", text = "Email")
        self.Student_table.heading("gender", text = "Gender")
        self.Student_table.heading("contact", text = "Contact")
        self.Student_table.heading("dob", text = "D.O.B")
        self.Student_table.heading("address", text = "Address")
        self.Student_table['show']='headings'
        self.Student_table.column("admission", width=100)
        self.Student_table.column("name", width=100)
        self.Student_table.column("department", width=100)
        self.Student_table.column("email", width=150)
        self.Student_table.column("gender", width=100)
        self.Student_table.column("contact", width=100)
        self.Student_table.column("dob", width=100)
        self.Student_table.column("address", width=150)
        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind("<ButtonRelease-1>", self.get_cursor)
        
        self.fetch_data()
    def add_students(self):
        if self.admission_No_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error","All fields are required!!")
        else:    
            
            con = pymysql.connect(host = "localhost", user = "root", password = "", database = "stm") 
            cur = con.cursor()
            cur.execute("insert into students values(%s, %s, %s, %s, %s, %s, %s, %s )",(self.admission_No_var.get(),
                                                                                        self.name_var.get(),
                                                                                        self.department_var.get(),
                                                                                        self.email_var.get(),
                                                                                        self.gender_var.get(),
                                                                                        self.contact_var.get(),
                                                                                        self.dob_var.get(),
                                                                                        self.txt_address.get('1.0',END)
                                                                                        ))   
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()  
            messagebox.showinfo("Success","Record added successfully") 

    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("select * from Students")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END, values = row)
            con.commit()
        con.close()   
    
    def clear(self):  
          if self.admission_No_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error","Can't clear blank fields!!")
          else:  
            self.admission_No_var.set("")
            self.name_var.set("")
            self.department_var.set("")
            self.email_var.set("")
            self.gender_var.set("")
            self.contact_var.set("")
            self.dob_var.set("")
            self.txt_address.delete('1.0',END)
            messagebox.showinfo("Success","Record cleared successfully") 
    def get_cursor(self,ev):
        curosor_row=self.Student_table.focus()
        contents=self.Student_table.item(curosor_row)
        row=contents['values']
        
        self.admission_No_var.set(row[0])
        self.name_var.set(row[1])
        self.department_var.set(row[2])
        self.email_var.set(row[3])
        self.gender_var.set(row[4])
        self.contact_var.set(row[5])
        self.dob_var.set(row[6])
        self.txt_address.delete('1.0',END)
        self.txt_address.insert(END,row[7])      
                 
    def update_data(self):
         if self.admission_No_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error","Can't update an empty field!!")
         else:  
        
            con = pymysql.connect(host = "localhost", user = "root", password = "", database = "stm") 
            cur = con.cursor()
            cur.execute("update  students set name=%s,department=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where admission_no=%s",(
                                                                                                                            self.name_var.get(),
                                                                                                                            self.department_var.get(),
                                                                                                                            self.email_var.get(),
                                                                                                                            self.gender_var.get(),
                                                                                                                            self.contact_var.get(),
                                                                                                                            self.dob_var.get(),
                                                                                                                            self.txt_address.get('1.0',END),
                                                                                                                            self.admission_No_var.get()
                                                                                                                            ))   
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()   
            messagebox.showinfo("Success","Record updated successfully") 
            
        
    def delete_data(self):
        if self.admission_No_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error","Can't delete blank fields!!")
        else:  
        
            con = pymysql.connect(host = "localhost", user = "root", password = "", database = "stm") 
            cur = con.cursor()
            cur.execute("delete from students where admission_no=%s",self.admission_No_var.get())
            con.commit()
            con.close()
            self.fetch_data()
            self.clear() 
            messagebox.showinfo("Success","Record deleted successfully") 
    
    def search_data(self):
         
        
            con = pymysql.connect(host="localhost", user="root", password="", database="stm")
            cur = con.cursor()
            cur.execute("select * from students where "+str(self.search_by.get()) + " Like '%" + str(self.search_txt.get()) + "%'")
            rows = cur.fetchall()
            if len(rows)!=0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                    self.Student_table.insert('',END, values=row)
                con.commit()
            con.close() 
            messagebox.showinfo("Success","Record retrieved successfully") 
                

root = Tk()
ob = Student(root)
root.mainloop()
