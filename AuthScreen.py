import tkinter as tk
from tkinter import messagebox

#login function
def login(username, password):
    if username == "admin" and password == "admin":
        messagebox.showinfo("User Authentication Success", "Welcome to TedgridyManager!")
    else:
        messagebox.showinfo("User Authentication Failure", "Invalid Username or Password")

class Authorize(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("User Authentication")
        self.geometry("300x200")
        self.configure(bg="lavender", padx=20, pady=10)
        self.resizable(False, False)
        label1=tk.Label(self, text="Username:", background="lavender") #username label
        label1.grid(row=0, column=0, padx=20, pady=20)
        userbox=tk.Entry(self, bd=5) #entrybox
        userbox.grid(row=0, column=1, padx=20, pady=20)
        label2=tk.Label(self, text="Password:", background="lavender") #password label
        label2.grid(row=1, column=0, padx=10, pady=10)
        passwbox=tk.Entry(self, bd=5, show="*") #entrybox
        passwbox.grid(row=1, column=1, padx=10, pady=10)
        btn_login=tk.Button(self, text="Login", width=10, command=login) #login button
        btn_login.grid(row=3, column=0, pady=20)
        btn_exit=tk.Button(self, text="Exit", width=10, command=self.quit) #exit button
        btn_exit.grid(row=3, column=1, pady=20)


if __name__ == '__main__':
    app=Authorize()
    app.mainloop()
