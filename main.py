import tkinter as tk
from UserDash import open_user_dashboard
from AdminDash import open_admin_dashboard

def open_admin():
    root.withdraw()  # Hide the login window
    open_admin_dashboard(root)  # Call the admin dashboard function

def open_user():
    root.withdraw()  # Hide the login window
    open_user_dashboard(root)  # Call the user dashboard function

# Main Tkinter Window
root = tk.Tk()
root.title("Login Page")
root.geometry("400x300")

tk.Label(root, text="Login as:").pack(pady=20)
tk.Button(root, text="Admin", command=open_admin).pack()
tk.Button(root, text="User", command=open_user).pack()

root.mainloop()

#login function
#def login(username, password):
#    if username == "admin" and password == "admin":
#        messagebox.showinfo("User Authentication Success", "Welcome to TedgridyManager!")
#    else:
#        messagebox.showinfo("User Authentication Failure", "Invalid Username or Password")
#