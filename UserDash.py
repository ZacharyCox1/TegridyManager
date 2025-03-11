
import tkinter as tk


#Function to load the adduser screen when the button is clicked
def add():
    root=tk.Tk()
    root.title("Add Evidence")
    root.geometry("300x400")
    root.configure(bg="lavender", padx=20, pady=20)
    root.resizable(False, False)
    email_label=tk.Label(root, text="Email:",bg= "lavender")
    email_label.pack()
    email_entry=tk.Entry(root, bd=5)
    email_entry.pack()
    fn_label=tk.Label(root, text="First Name:", bg="lavender")
    fn_label.pack()
    fn_entry=tk.Entry(root, bd=5)
    fn_entry.pack()
    ln_label=tk.Label(root, text="Last Name:", bg="lavender")
    ln_label.pack()
    ln_entry=tk.Entry(root, bd=5)
    ln_entry.pack()
    phone_label=tk.Label(root, text="Phone Number:", bg="lavender")
    phone_label.pack()
    phone_entry=tk.Entry(root, bd=5)
    phone_entry.pack()
    title_label=tk.Label(root, text="Title:", bg="lavender")
    title_label.pack()
    title_entry=tk.Entry(root, bd=5)
    title_entry.pack()
    btn_adduser=tk.Button(root, text="Add User", width=10) #MUST DEFINE COMMAND PARAMETER BEFORE BUTTON WILL WORK
    btn_adduser.place(x=25, y=280)
    btn_cancel=tk.Button(root, text="Cancel", command=root.withdraw, width=10)
    btn_cancel.place(x=150, y=280)

def view():
    root=tk.Tk()
    root.title("View Case Assignment")
    root.geometry("800x400")
    root.configure(bg="lavender", padx=20, pady=10)
    root.resizable(False, False)

def hashes():
    root=tk.Tk()
    root.title("Verify Hash Values")
    root.geometry("800x400")
    root.configure(bg="lavender", padx=20, pady=10)
    root.resizable(False, False)

def data():
    root=tk.Tk()
    root.title("Database Viewer")
    root.geometry("800x400")
    root.configure(bg="lavender", padx=20, pady=10)
    root.resizable(False, False)


def open_user_dashboard(root):
    user_window=tk.Toplevel(root)
    user_window.title("TM Dashboard")
    user_window.geometry("1000x500")
    user_window.configure(bg="lavender") #padding can be added here
    user_window.resizable(False, False)
    btn_view=tk.Button(user_window, text="View Case Assignment", width=20, command=view)
    btn_view.place(x=60, y=280)
    btn_add=tk.Button(user_window, text="Add Evidence Items", width=20, command=add)
    btn_add.place(x=300, y=280)
    btn_hashes=tk.Button(user_window, text="Verify Hash Values", width=20, command=hashes)
    btn_hashes.place(x=540, y=280)
    btn_data=tk.Button(user_window,text="View Stored Data", width=20, command=data)
    btn_data.place(x=780, y=280)





#bgText=tk.Text(root, bg="lavender", x=20, y=20)
#bgText.insert(root, "Welcome to TegridyManager")



