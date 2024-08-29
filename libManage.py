from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("LIBRARY MANAGEMENT SYSTEM")
        self.root.geometry("1550x800+0+0")

        ######################### VARIABLE #########################################################

        self.member_variable = StringVar()
        self.srn_variable = StringVar()
        self.id_variable = StringVar()
        self.first_variable = StringVar()
        self.second_variable = StringVar()
        self.add1_variable = StringVar()
        self.add2_variable = StringVar()
        self.postcode_variable = StringVar()
        self.mobile_variable = StringVar()
        self.bookId_variable = StringVar()
        self.bookTitle_variable = StringVar()
        self.author_variable = StringVar()
        self.dateBorrowed_variable = StringVar()
        self.dateDue_variable = StringVar()
        self.days_on_book_variable = StringVar()
        self.lateFine_variable = StringVar()
        self.dueOverDate_variable = StringVar()
        self.finalPrice_variable = StringVar()

        lbtitle = Label(self.root, text='LIBRARY MANAGEMENT SYSTEM', bg="light blue", fg="blue", font=("times new roman", 50, 'bold'), padx=2, pady=6)
        lbtitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd=12, relief=RIDGE, padx=30, bg='light blue')
        frame.place(x=0, y=100, width=1530, height=450)

        DataFrameLeft = LabelFrame(frame, text='LIB. MEMBERSHIP INFORMATION', bg="light blue", fg="green", font=("times new roman", 10, 'bold'), padx=2, pady=20)
        DataFrameLeft.place(x=0, y=10, width=750, height=400)

        lblMember = Label(DataFrameLeft, bg='light blue', text='Member Type', font=("times new roman", 13, 'bold'), padx=2, pady=6)
        lblMember.grid(row=0, column=0, sticky=W)

        comMember = ttk.Combobox(DataFrameLeft, font=("times new roman", 13, 'bold'), textvariable=self.member_variable, width=27, state="readonly")
        comMember["value"] = ("Admin staff", "Student", "Lecturer")
        comMember.grid(row=0, column=1)

        def only_numbers(char):
            return char.isdigit()

        def only_date(char):
            return char.isdigit() or char == '/'

        validate_number = self.root.register(only_numbers)
        validate_date = self.root.register(only_date)

        SRNNO = Label(DataFrameLeft, bg='light blue', text='SRN Number', font=("times new roman", 13, 'bold'), padx=2, pady=6)
        SRNNO.grid(row=1, column=0, sticky=W)
        txtSRNNO = Entry(DataFrameLeft, font=("times new roman", 13, 'bold'), width=29, validate="key", validatecommand=(validate_number, '%S'), textvariable=self.srn_variable)
        txtSRNNO.grid(row=1, column=1, sticky=W)

        title = Label(DataFrameLeft, bg='light blue', text='ID No:', font=("arial", 13, 'bold'), padx=2, pady=6)
        title.grid(row=2, column=0, sticky=W)
        txttitle = Entry(DataFrameLeft, font=("arial", 13, 'bold'), textvariable=self.id_variable, width=29)
        txttitle.grid(row=2, column=1, sticky=W)

        firstName = Label(DataFrameLeft, bg='light blue', text='First Name', font=("arial", 13, 'bold'), padx=2, pady=6)
        firstName.grid(row=3, column=0, sticky=W)
        txtFirstName = Entry(DataFrameLeft, font=("arial", 13, 'bold'), textvariable=self.first_variable, width=29)
        txtFirstName.grid(row=3, column=1, sticky=W)

        LastName = Label(DataFrameLeft, bg='light blue', text='Last Name', font=("arial", 13, 'bold'), padx=2, pady=6)
        LastName.grid(row=4, column=0, sticky=W)
        txtLastName = Entry(DataFrameLeft, font=("arial", 13, 'bold'), textvariable=self.second_variable, width=29)
        txtLastName.grid(row=4, column=1, sticky=W)

        Address_1 = Label(DataFrameLeft, bg='light blue', text='Address 1', font=("arial", 13, 'bold'), padx=2, pady=6)
        Address_1.grid(row=5, column=0, sticky=W)
        txtAddress1 = Entry(DataFrameLeft, font=("arial", 13, 'bold'), textvariable=self.add1_variable, width=29)
        txtAddress1.grid(row=5, column=1, sticky=W)

        Address_2 = Label(DataFrameLeft, bg='light blue', text='Address 2', font=("arial", 13, 'bold'), padx=2, pady=6)
        Address_2.grid(row=6, column=0, sticky=W)
        txtAddress2 = Entry(DataFrameLeft, font=("arial", 13, 'bold'), textvariable=self.add2_variable, width=29)
        txtAddress2.grid(row=6, column=1, sticky=W)

        PostCode = Label(DataFrameLeft, bg='light blue', text='Post Code', font=("arial", 13, 'bold'), padx=2, pady=6)
        PostCode.grid(row=7, column=0, sticky=W)
        txtPostCode = Entry(DataFrameLeft, font=("arial", 13, 'bold'), textvariable=self.postcode_variable, width=29, validate="key", validatecommand=(validate_number, '%S'))
        txtPostCode.grid(row=7, column=1, sticky=W)

        MobileNumber = Label(DataFrameLeft, bg='light blue', text='Mobile Number', font=("arial", 13, 'bold'), padx=2, pady=6)
        MobileNumber.grid(row=8, column=0, sticky=W)
        txtMobileNumber = Entry(DataFrameLeft, font=("arial", 13, 'bold'), textvariable=self.mobile_variable, width=29, validate="key", validatecommand=(validate_number, '%S'))
        txtMobileNumber.grid(row=8, column=1, sticky=W)

        DataFrameRight = LabelFrame(frame, text='BOOK DETAILS', bg="light blue", fg="green", font=("times new roman", 10, 'bold'), padx=2, pady=20)
        DataFrameRight.place(x=751, y=10, width=700, height=400)

        Id = Label(DataFrameRight, bg='light blue', text='Book Id', font=("arial", 13, 'bold'), padx=2, pady=6)
        Id.grid(row=1, column=0, sticky=W)
        txtId = Entry(DataFrameRight, font=("arial", 13, 'bold'), textvariable=self.bookId_variable, width=29)
        txtId.grid(row=1, column=1, sticky=W)

        Title = Label(DataFrameRight, bg='light blue', text='Book Title', font=("arial", 13, 'bold'), padx=2, pady=6)
        Title.grid(row=2, column=0, sticky=W)
        txtTitle = Entry(DataFrameRight, font=("arial", 13, 'bold'), textvariable=self.bookTitle_variable, width=29)
        txtTitle.grid(row=2, column=1, sticky=W)

        AuthorName = Label(DataFrameRight, bg='light blue', text='Author Name', font=("arial", 13, 'bold'), padx=2, pady=6)
        AuthorName.grid(row=3, column=0, sticky=W)
        txtAuthorName = Entry(DataFrameRight, font=("arial", 13, 'bold'), textvariable=self.author_variable, width=29)
        txtAuthorName.grid(row=3, column=1, sticky=W)

        Date_Borrowed = Label(DataFrameRight, bg='light blue', text='Date Borrowed', font=("arial", 13, 'bold'), padx=2, pady=6)
        Date_Borrowed.grid(row=4, column=0, sticky=W)
        txtDate_Borrowed = Entry(DataFrameRight, font=("arial", 13, 'bold'), textvariable=self.dateBorrowed_variable, width=29, validate="key", validatecommand=(validate_date, '%S'))
        txtDate_Borrowed.grid(row=4, column=1, sticky=W)

        Date_due = Label(DataFrameRight, bg='light blue', text='Date Due', font=("arial", 13, 'bold'), padx=2, pady=6)
        Date_due.grid(row=5, column=0, sticky=W)
        txtDate_due = Entry(DataFrameRight, font=("arial", 13, 'bold'), textvariable=self.dateDue_variable, width=29, validate="key", validatecommand=(validate_date, '%S'))
        txtDate_due.grid(row=5, column=1, sticky=W)

        Days_on_book = Label(DataFrameRight, bg='light blue', text='Days On Book', font=("arial", 13, 'bold'), padx=2, pady=6)
        Days_on_book.grid(row=6, column=0, sticky=W)
        txtDays_on_book = Entry(DataFrameRight, font=("arial", 13, 'bold'), textvariable=self.days_on_book_variable, width=29)
        txtDays_on_book.grid(row=6, column=1, sticky=W)

        LateReturnFine = Label(DataFrameRight, bg='light blue', text='Late Return Fine', font=("arial", 13, 'bold'), padx=2, pady=6)
        LateReturnFine.grid(row=7, column=0, sticky=W)
        txtLateReturnFine = Entry(DataFrameRight, font=("arial", 13, 'bold'), textvariable=self.lateFine_variable, width=29)
        txtLateReturnFine.grid(row=7, column=1, sticky=W)

        DateOverDue = Label(DataFrameRight, bg='light blue', text='Date Over Due', font=("arial", 13, 'bold'), padx=2, pady=6)
        DateOverDue.grid(row=8, column=0, sticky=W)
        txtDateOverDue = Entry(DataFrameRight, font=("arial", 13, 'bold'), textvariable=self.dueOverDate_variable, width=29, validate="key", validatecommand=(validate_date, '%S'))
        txtDateOverDue.grid(row=8, column=1, sticky=W)

        FinalPrice = Label(DataFrameRight, bg='light blue', text='Final Price', font=("arial", 13, 'bold'), padx=2, pady=6)
        FinalPrice.grid(row=9, column=0, sticky=W)
        txtFinalPrice = Entry(DataFrameRight, font=("arial", 13, 'bold'), textvariable=self.finalPrice_variable, width=29)
        txtFinalPrice.grid(row=9, column=1, sticky=W)

        FrameDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="light blue")
        FrameDetails.place(x=0, y=550, width=1530, height=195)

        Table_frame = Frame(FrameDetails, bd=6, relief=RIDGE, bg="light blue")
        Table_frame.place(x=0, y=2, width=1460, height=170)

        xscroll = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.library_table = ttk.Treeview(Table_frame, columns=('memberType', 'SRNNO', 'ID', 'fName', 'sName', 'address1', 'address2', 'postID', 'mobile', 'bookid', 'title', 'author', 'borrowed', 'due', 'days', 'lateFine', 'overDue', 'finalPrice'), xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("memberType", text="Member Type")
        self.library_table.heading("SRNNO", text="SRN No.")
        self.library_table.heading("ID", text="ID")
        self.library_table.heading("fName", text="First Name")
        self.library_table.heading("sName", text="Last Name")
        self.library_table.heading("address1", text="Address 1")
        self.library_table.heading("address2", text="Address 2")
        self.library_table.heading("postID", text="Post Code")
        self.library_table.heading("mobile", text="Mobile No.")
        self.library_table.heading("bookid", text="Book ID")
        self.library_table.heading("title", text="Title")
        self.library_table.heading("author", text="Author")
        self.library_table.heading("borrowed", text="Borrowed")
        self.library_table.heading("due", text="Due Date")
        self.library_table.heading("days", text="DaysOnBook")
        self.library_table.heading("lateFine", text="LateFine")
        self.library_table.heading("overDue", text="DateOverDue")
        self.library_table.heading("finalPrice", text="FinalPrice")

        self.library_table["show"] = "headings"

        self.library_table.column("memberType", width=100)
        self.library_table.column("SRNNO", width=100)
        self.library_table.column("ID", width=100)
        self.library_table.column("fName", width=100)
        self.library_table.column("sName", width=100)
        self.library_table.column("address1", width=100)
        self.library_table.column("address2", width=100)
        self.library_table.column("postID", width=100)
        self.library_table.column("mobile", width=100)
        self.library_table.column("bookid", width=100)
        self.library_table.column("title", width=100)
        self.library_table.column("author", width=100)
        self.library_table.column("borrowed", width=100)
        self.library_table.column("due", width=100)
        self.library_table.column("days", width=100)
        self.library_table.column("lateFine", width=100)
        self.library_table.column("overDue", width=100)
        self.library_table.column("finalPrice", width=100)

        self.library_table.pack(fill=BOTH, expand=1)

        def add_data():
            if self.member_variable.get() == "" or self.srn_variable.get() == "":
                messagebox.showerror("Error", "All fields are required")
            else:
                try:
                    conn = mysql.connector.connect()
                    conn.connect(host="localhost", user="root", password="Password", database="lib_manager")
                    cursor = conn.cursor()
                    cursor.execute(
                        "INSERT INTO library (Member, SRN,id, idFirst Name, Second Name, Address 1, Address 2, Post ID, Mobile Number, Book ID, Book Title, Author, Date of borrow, Date Due, Days On Book, Late Fine Return, Date Over Dur, final price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s)",
                        (
                            self.member_variable.get(),
                            self.srn_variable.get(),
                            self.id_variable.get(),
                            self.first_variable.get(),
                            self.second_variable.get(),
                            self.add1_variable.get(),
                            self.add2_variable.get(),
                            self.postcode_variable.get(),
                            self.mobile_variable.get(),
                            self.bookId_variable.get(),
                            self.bookTitle_variable.get(),
                            self.author_variable.get(),
                            self.dateBorrowed_variable.get(),
                            self.dateDue_variable.get(),
                            self.days_on_book_variable.get(),
                            self.lateFine_variable.get(),
                            self.dueOverDate_variable.get(),
                            self.finalPrice_variable.get()
                        )
                    )
                    conn.commit()
                    cursor.close()
                    conn.close()

                    messagebox.showinfo("Success", "Record has been inserted successfully")
                    fetch_data()
                except Exception as e:
                    messagebox.showerror("Error", f"Error due to {str(e)}")

        def fetch_data():
            pass 

        
        btnFrame = Frame(frame, bd=4, relief=RIDGE, bg="light blue")
        btnFrame.place(x=0, y=400, width=1500, height=60)  # Adjust width to fit all buttons

        # Add buttons to the frame with adjusted placement
        btnAddData = Button(btnFrame, text="Add Data", command=add_data, font=("arial", 12, "bold"), width=15, bg="blue", fg="white")
        btnAddData.grid(row=0, column=0, padx=10, pady=10)

        btnShowData = Button(btnFrame, text="Show Data", font=("arial", 12, "bold"), width=15, bg="blue", fg="white")
        btnShowData.grid(row=0, column=1, padx=10, pady=10)

        btnUpdate = Button(btnFrame, text="Update", font=("arial", 12, "bold"), width=15, bg="blue", fg="white")
        btnUpdate.grid(row=0, column=2, padx=10, pady=10)

        btnDelete = Button(btnFrame, text="Delete", font=("arial", 12, "bold"), width=15, bg="blue", fg="white")
        btnDelete.grid(row=0, column=3, padx=10, pady=10)

        btnReset = Button(btnFrame, text="Reset", font=("arial", 12, "bold"), width=15, bg="blue", fg="white")
        btnReset.grid(row=0, column=4, padx=10, pady=10)

        btnExit = Button(btnFrame, text="Exit", command=self.root.quit, font=("arial", 12, "bold"), width=15, bg="blue", fg="white")
        btnExit.grid(row=0, column=5, padx=10, pady=10)

if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()
