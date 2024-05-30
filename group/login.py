import tkinter as tk
from tkinter import messagebox
import payroll
import user_info
import employee_reg


class loginApp:
    def __init__(self,master):
        self.master = master
        self.master.title("Login System")
        self.master.geometry("600x350")
        self.master.configure(bg='pink')

        self.accounts={
            "admin": "123",
            "accounting": "123",
            "hr": "123"
        }

        self.label1 = tk.Label(self.master, text='Login',
    bg='gray', fg='black', font=('Times New Roman', 30))
        self.label1.place(x=250, y=15)

        self.label2 = tk.Label(self.master, text='Username',
    bg='gray', fg='black', font=('Arial', 20, 'bold'))
        self.label2.place(x=155, y=95)

        self.label3 = tk.Label(self.master, text='Password',
    bg='gray', fg='black', font=('Arial', 20, 'bold'))
        self.label3.place(x=155, y=170)

        self.entry1 = tk.Entry(self.master, font=('Arial', 15))
        self.entry1.place(x=300, y=100)

        self.entry2 = tk.Entry(self.master, font=('Arial', 15))
        self.entry2.place(x=300, y=175)

        self.button = tk.Button(self.master, text='Login', bg='red',
    font=('Arial', 15), bd=5, fg='white', command=self.login)
        self.button.place(x=300, y=250)

    def login(self):
        username = self.entry1.get()
        password = self.entry2.get()
        if username in self.accounts and self.accounts[username] == password:
            messagebox.showinfo("Welcome", "You have successfully logged in.")
            if username == "accounting":
                self.open_payroll()
            elif username == "hr":
                self.open_employee_reg()
            elif username == "admin":
                self.open_menu()
            else:
                self.open_menu()
        else:
            messagebox.showerror("Login failed", "Invalid Username or Password")

    def open_menu(self):
        self.master.destroy()  # Destroy the previous window
        self.menu_window = tk.Toplevel(self.master)  # Create a new window as a child of the existing one
        self.menu_window.configure(bg='light gray')

        button1 = tk.Button(self.menu_window, text='Employee Registration',
                            bg='light gray', fg='black', font=('Arial', 15), bd=5,
                            command=self.open_employee_reg)
        button1.pack(pady=20)

        button2 = tk.Button(self.menu_window, text='Payroll',
                            bg='light gray', fg='black', font=('Arial', 15), bd=5,
                            command=self.open_payroll)
        button2.pack(pady=20)

        button3 = tk.Button(self.menu_window, text='User Info',
                            bg='light gray', fg='black', font=('Arial', 15), bd=5,
                            command=self.open_user_info)
        button3.pack(pady=20)

    def open_employee_reg(self):
        employee_window = tk.Toplevel(self.master)
        self.open_employee_reg(employee_window)

    def open_payroll(self):
        payroll_window = tk.Toplevel(self.master)
        self.open_payroll(payroll_window)

    def open_user_info(self):
        user_info_window = tk.Toplevel(self.master)
        self.open_user_info(user_info_window)

if __name__ == "__main__":
    root = tk.Tk()
    app = loginApp(root)
    root.mainloop()