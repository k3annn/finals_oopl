import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3

window = Tk()
window.geometry("1200x799")
window.title("USER ACC INFO")

def save_data_query():
    # Extract data from GUI elements
    data = [
        first_name.get(),
        middle_name.get(),
        last_name.get(),
        suffix.get(),
        department.get(),
        designation.get(),
        username.get(),
        password.get(),
        confirm_password.get(),
        usertype.get(),
        userstatus.get(),
        employeenum.get()

    ]

    con = sqlite3.connect("USERACCINFOGROUP")
    save_data_query = """
    INSERT INTO user_acc_info_group_tbl (first_name, middle_name, last_name, suffix, department, 
    designation, username, password, confirm_password, usertype, user_status, employee_num) VALUES (?, ?, ?, ?, ?, ?, 
    ?, ?, ?, ?, ?, ?)"""
    con.execute(save_data_query, data)
    # Commit changes and close the connection
    con.commit()
    con.close()
    tk.messagebox.showinfo("Data Saved", "Data has been saved to the database")



    first_name.delete(0, "end")
    middle_name.delete(0, "end")
    last_name.delete(0, "end")
    suffix.delete(0, "end")
    department.delete(0, "end")
    designation.delete(0, "end")
    username.delete(0, "end")
    password.delete(0, "end")
    confirm_password.delete(0, "end")
    usertype.delete(0, "end")
    employeenum.delete(0, "end")


image = Image.open("adamson.jpg")
photo = ImageTk.PhotoImage(image)


image = Image.open("adamson.jpg")
image = image.resize((100, 100))
photo = ImageTk.PhotoImage(image)

frame = Frame(window, width=900, height=500, bg="light gray")
frame.place(relx=0.5, rely=0.5, anchor=CENTER)



label = Label(window, text="User Account Information", font=('serif', 25, 'bold'), bg="white")
label.place(x=165,y=130)

first_name = Label(window, text="First Name", font=(13), bg="white")
first_name.place(relx=.26, rely=.39)
first_name = Entry(window, bg="#FFFFFF")
first_name.place(relx=.26, rely=.43)

middle_name = Label(window, text="Middle Name", font=(13), bg="white")
middle_name.place(relx=.38, rely=.39)
middle_name = Entry(window, bg="#FFFFFF")
middle_name.place(relx=.38, rely=.43)

last_name = Label(window, text="Last Name", font=(13), bg="white")
last_name.place(relx=.51, rely=.39)
last_name = Entry(window, bg="#FFFFFF")
last_name.place(relx=.51, rely=.43)

suffix = Label(window, text="Suffix", font=(13), bg="white")
suffix.place(relx=.64, rely=.39)
suffix = Entry(window, bg="#FFFFFF")
suffix.place(relx=.64, rely=.43)

department = Label(window, text="Department", font=(20), bg="white")
department.place(relx=.76, rely=.39)
department = Entry(window, bg="#FFFFFF")
department.place(relx=.76, rely=.43)

designation = Label(window, text="Designation", font=(20), bg="white")
designation.place(relx=.15, rely=.50)
designation = Entry(window, bg="#FFFFFF", width=40)
designation.place(relx=.15, rely=.55)

username = Label(window, text="Username", font=(20), bg="white")
username.place(relx=.38, rely=.50)
username = Entry(window, bg="#FFFFFF", width=40)
username.place(relx=.38, rely=.55)

password: Label = Label(window, text="Password", font=(20), bg="white")
password.place(relx=.63, rely=.50)
password = Entry(window, bg="#FFFFFF", width=40, show="*")
password.place(relx=.63, rely=.55)

confirm_password = Label(window, text="Confirm Password", font=(20), bg="white")
confirm_password.place(relx=.15, rely=.61)
confirm_password = Entry(window, bg="#FFFFFF", width=40, show="*")
confirm_password.place(relx=.15, rely=.66)

usertype = Label(window, text="User Type", font=(20), bg="white")
usertype.place(relx=.38, rely=.61)
usertype = Entry(window, bg="#FFFFFF", width=29)
usertype.place(relx=.38, rely=.66)

userstatus = Label(window, text="User Status", font=(20), bg="white")
userstatus.place(relx=.55, rely=.61)
userstatus = Entry(window, bg="#FFFFFF", width=26)
userstatus.place(relx=.55, rely=.66)

employeenum = Label(window, text="Employee Number", font=(20), bg="white")
employeenum.place(relx=.70, rely=.61)
employeenum = Entry(window, bg="#FFFFFF", width=28)
employeenum.place(relx=.70, rely=.66)

update_button = Button(window, text="Update", bg="#3E64dA", font=("Arial", 16),
                       fg="#FFFFFF", width=10, command = save_data_query)
update_button.place(relx=.36, rely=.78, anchor=CENTER)

delete_button = Button(window, text="Delete", bg="#FFDB58", font=("Arial", 16),
                       fg="#000000", width=10)
delete_button.place(relx=.51, rely=.78, anchor=CENTER)

cancel_button = Button(window, text="Cancel", bg="#FFFFFF", font=("Arial, 16"),
                       fg="#000000", width=10)
cancel_button.place(relx=.66, rely=.78, anchor=CENTER)


window.mainloop()