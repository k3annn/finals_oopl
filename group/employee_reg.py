import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3

def save_data_entry():
    FirstName = get_FirstName.get()
    MiddleName = get_MiddleName.get()
    LastName = get_LastName.get()
    Suffix = get_Suffix.get()
    DateOfBirth = DateOfBirth_entry.get()
    Gender = gender_box.get()
    Nationality = NationalityBox.get()
    CivilStats = CivilStatsBox.get()
    Department = get_Department.get()
    Designation = get_Designation.get()
    QualidDeptStats = QualidDeptStats_combobox.get()
    EmployeeStats = get_EmployeeStats.get()
    Paydate = get_Paydate.get()
    EmployeeNum = get_EmployeeNum.get()
    ContactNo = get_ContactNo.get()
    Email = get_Email.get()
    SocMed = getSocMed.get()
    AccIdNo = get_AccIdNo.get()
    AddLine1 = get_AddLine1.get()
    AddLine2 = get_AddLine2.get()
    MuniCity = get_MuniCity.get()
    StateProv = get_StateProv.get()
    Country = getCountry.get()
    Zip = get_Zip.get()
    PicPath = get_PicPath.get()


    con = sqlite3.connect("Employee_group")
    save_data_query = """
    INSERT INTO employee_group_TBL (first_name, middle_name, last_name, suffix, date_of_birth, gender, nationality, civil_status, department, designation, qualified_dep_status, employee_status, pay_date, employee_number, contact_no, email_address, social_media, social_media_account, address_line_1, address_line_2, municipality, state, country, zip_code, pic_path) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
    con.execute(save_data_query, (FirstName, MiddleName, LastName, Suffix, DateOfBirth, Gender, Nationality,
                                  CivilStats, Department, Designation, QualidDeptStats, EmployeeStats, Paydate,
                                  EmployeeNum, ContactNo, Email, SocMed, AccIdNo, AddLine1, AddLine2, MuniCity,
                                  StateProv, Country, Zip, PicPath))
    con.commit()
    con.close()
    tk.messagebox.showinfo("Data Saved", "Data has been saved to the database")


main = tk.Tk()
main.title("Registration Form")

mainframe = Frame(main, width=1200, height=1500, bg='white')
mainframe.grid(row=0, column=0, rowspan=20, columnspan=4)

frame = Frame(mainframe, width=1000, height=300, bg='light grey')
frame.grid(row=0, column=0, rowspan=4, columnspan=4, padx=30, pady=(5, 0), sticky='w')

frame2 = Frame(mainframe, width=1000, height=100, bg='light grey')
frame2.grid(row=4, column=0, rowspan=4, columnspan=4, padx=30, pady=(20, 0), sticky='w')

frame3 = Frame(mainframe, width=1000, height=100, bg='light grey')
frame3.grid(row=9, column=0, rowspan=4, columnspan=4, padx=30, pady=(0, 0), sticky='w')

frame4 = Frame(mainframe, width=1000, height=100, bg='light grey')
frame4.grid(row=15, column=0, rowspan=4, columnspan=4, padx=30, pady=(0, 0), sticky='w')

# IMAGE IMPORT
image = Image.open("adamson.jpg")
image = image.resize((100, 100))
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(frame, image=photo)
image_label.grid(row=0, column=0, rowspan=3, padx=(5, 5), pady=5)

choose_file_button = tk.Button(frame, text="Choose File")
choose_file_button.grid(row=3, column=0, padx=(0, 5), pady=5)

# FIRST FRAME
FirstName = tk.Label(frame, text="First Name", bg='light grey')
FirstName.grid(row=0, column=1, sticky="w",padx=10, pady=(10,0))
get_FirstName = tk.Entry(frame)
get_FirstName.grid(row=1, column=1, padx=10, pady=(0,10))

MiddleName = tk.Label(frame, text="Middle Name", bg='light grey')
MiddleName.grid(row=0, column=2, sticky="w",padx=10, pady=(10,0))
get_MiddleName = tk.Entry(frame)
get_MiddleName.grid(row=1, column=2, padx=10, pady=(0,10))

LastName = tk.Label(frame, text="Last Name", bg='light grey')
LastName.grid(row=0, column=3, sticky="w",padx=10, pady=(10,0))
get_LastName = tk.Entry(frame)
get_LastName.grid(row=1, column=3,padx=10, pady=(0,10))

Suffix = tk.Label(frame, text="Suffix", bg='light grey')
Suffix.grid(row=0, column=4, sticky="w",padx=10, pady=(10,0))
get_Suffix = tk.Entry(frame,width= 20)
get_Suffix.grid(row=1, column=4,padx=10, pady=(0,10))

DateOfBirth = tk.Label(frame, text="Date of Birth", bg='light grey')
DateOfBirth.grid(row=2, column=1, sticky="w")
DateOfBirth_entry = tk.Entry(frame)
DateOfBirth_entry.grid(row=3, column=1, padx=10, pady=1)

gender = tk.Label(frame, text="Gender", bg='light grey')
gender.grid(row=2, column=2, sticky="w")
gender_box = ttk.Combobox(frame, values=["Male", "Female", "Other"])
gender_box.insert(0, ' -- select one --')
gender_box.grid(row=3, column=2, padx=8, pady=1)

Nationality = tk.Label(frame, text="Nationality", bg='light grey')
Nationality.grid(row=2, column=3, sticky="w")
NationalityBox = ttk.Combobox(frame, values=["Filipino", "American", "Other"])
NationalityBox.grid(row=3, column=3, sticky="w", pady=1)
NationalityBox.insert(1, 'Filipino')

CivilStats = tk.Label(frame, text="Civil Status", bg='light grey')
CivilStats.grid(row=2, column=4, sticky="w", padx=10, pady=(5,0))
CivilStatsBox = ttk.Combobox(frame, values=["Married", "Single", "Other"],width=19)
CivilStatsBox.insert(1, '--select one--')
CivilStatsBox.grid(row=3, column=4, sticky="w", padx=10, pady=0)

# SECOND FRAME
Department = tk.Label(frame2, text="Department", bg='light grey')
Department.grid(row=1, column=0, sticky="w", padx=15, pady=(10, 0))
get_Department = tk.Entry(frame2, width=50)
get_Department.grid(row=2, column=0, padx=(15, 1), pady=0)

Designation = tk.Label(frame2, text="Designation", bg='light grey')
Designation.grid(row=1, column=1, sticky='w', padx=6, pady=(10, 0))
get_Designation = tk.Entry(frame2, width=25)
get_Designation.grid(row=2, column=1, padx=(6, 0), pady=0)

QualidDeptStats = tk.Label(frame2, text="Qualified Dep. Status", bg='light grey')
QualidDeptStats.grid(row=1, column=3, sticky='w', padx=15, pady=(10, 0))
QualidDeptStats_combobox = ttk.Combobox(frame2, values=["Pending", "Other"], width=32)
QualidDeptStats_combobox.insert(1, ' -- select one --')
QualidDeptStats_combobox.grid(row=2, column=3, padx=(10, 0), pady=0, sticky="w")

EmployeeStats = tk.Label(frame2, text="Employee Status", bg='light grey')
EmployeeStats.grid(row=3, column=0, sticky='w', padx=(15, 0), pady=(10, 0))
get_EmployeeStats = tk.Entry(frame2, width=50)
get_EmployeeStats.grid(row=4, column=0, padx=(15, 0), pady=5)

Paydate = tk.Label(frame2, text="Pay Date", bg='light grey')
Paydate.grid(row=3, column=1, sticky='w', padx=15, pady=(10, 0))
get_Paydate = tk.Entry(frame2, width=20)
get_Paydate.grid(row=4, column=1, padx=15, pady=5)

EmployeeNum = tk.Label(frame2, text="Employee Number", bg='light grey')
EmployeeNum.grid(row=3, column=3, sticky='w', padx=15, pady=(10, 0))
get_EmployeeNum = tk.Entry(frame2, width=34)
get_EmployeeNum.grid(row=4, column=3, padx=15, pady=5)

# CONTACT INFO
Contact = Label(mainframe, text="Contact Info", bg='white', font=('Times New Roman', 12, 'bold'))
Contact.grid(row=8, column=0, sticky='w', padx=30, pady=(10, 0))

ContactNo = Label(frame3, text="Contact No.", bg='light grey')
ContactNo.grid(row=1, column=0,padx=15, pady=(10, 0),sticky = 'w')
get_ContactNo = tk.Entry(frame3, width=50)
get_ContactNo.grid(row=2, column=0,sticky='w', padx=15, pady=(0, 0))

Email = Label(frame3, text="Email Address", bg='light grey')
Email.grid(row=1, column=1,padx=0, pady=(10, 0),sticky = 'w')
get_Email = tk.Entry(frame3, width=55)
get_Email.grid(row=2, column=1,padx=(0,30),pady=(0, 0))

SocMed = Label(frame3, text="Social Media", bg='light grey')
SocMed.grid(row=3, column=0,padx=15, pady=(10, 0),sticky = 'w')
getSocMed = ttk.Combobox(frame3, values=["Facebook", "Instagram","X"], width=50)
getSocMed.insert(1, ' -- select one --')
getSocMed.grid(row=4, column=0,sticky='w', padx=15, pady=(0, 10))

AccIdNo = Label(frame3, text="Social Media Account Id/No", bg='light grey')
AccIdNo.grid(row=3, column=1,padx=0, pady=(10, 0),sticky = 'w')
get_AccIdNo = tk.Entry(frame3, width=54)
get_AccIdNo.grid(row=4, column=1,sticky='w',padx=(0,30),pady=(0, 10))

Contact = Label(mainframe, text="Address", bg='white', font=('Times New Roman', 12, 'bold'))
Contact.grid(row=14, column=0, sticky='w', padx=30, pady=(10, 0))

# FOURTH FRAME
AddLine1 = Label(frame4, text="Address Line 1", bg='light grey')
AddLine1.grid(row=1, column=0,padx=15, pady=(10, 0),sticky = 'w')
get_AddLine1 = tk.Entry(frame4, width=114)
get_AddLine1.grid(row=2, column=0,columnspan=4,padx=(15,15),sticky ='w')

AddLine2 = Label(frame4, text="Address Line 2", bg='light grey')
AddLine2.grid(row=3, column=0,padx=15, pady=(10, 0),sticky = 'w')
get_AddLine2 = tk.Entry(frame4, width=114)
get_AddLine2.grid(row=4, column=0,columnspan=4,padx=(15,15),sticky ='w')

MuniCity = Label(frame4, text="Municipality/City", bg='light grey')
MuniCity.grid(row=5, column=0,padx=(15,0), pady=(10, 0),sticky = 'w')
get_MuniCity = tk.Entry(frame4, width=50)
get_MuniCity.grid(row=6, column=0,sticky='w', padx=(15,0), pady=(0, 0))

StateProv = Label(frame4, text="State/Province", bg='light grey')
StateProv.grid(row=5, column=1,padx=(15,0), pady=(10, 0),sticky = 'w')
get_StateProv = tk.Entry(frame4, width=57)
get_StateProv.grid(row=6, column=1,sticky='w', padx=(15,0), pady=(0, 0))

Country = Label(frame4, text="Country", bg='light grey')
Country.grid(row=7, column=0,padx=(15,0), pady=(10, 0),sticky = 'w')
getCountry = ttk.Combobox(frame4, values=["America", "Philippines","Others"], width=47)
getCountry.insert(1, ' -- select one --')
getCountry.grid(row=8, column=0,sticky='w', padx=15, pady=(0, 10))

Zip =Label(frame4, text="Zip Code", bg='light grey')
Zip.grid(row=7, column=1,padx=(15,0), pady=(10, 0),sticky = 'w')
get_Zip = tk.Entry(frame4, width=20)
get_Zip.grid(row=8, column=1,sticky='w', padx=(15,0), pady=(0, 0))

PicPath = Label(frame4, text="Picture Path", bg='light grey')
PicPath.grid(row=9, column=0,padx=15, pady=(5, 0),sticky = 'w')
get_PicPath = tk.Entry(frame4, width=114)
get_PicPath.grid(row=10, column=0,columnspan=4,padx=(15,15),pady=(0, 10),sticky ='w')

# BUTTONS
Save = tk.Button(mainframe, text="Save", bg="blue", fg='white', width=10,command = save_data_entry)
Save.grid(row=26, column=0, padx=(29, 0), pady=5, sticky='w')

Cancel = tk.Button(mainframe, text="Cancel", width=10)
Cancel.grid(row=26, column=0, padx=(115, 0), pady=5, sticky='w')

main.geometry('800x900')
main.mainloop()
