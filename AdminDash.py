import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import mysql.connector

# Function to establish the database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="Tegridy"
    )

# Function to create a new user
def create_user(email, first, last, phone, title):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Calling the stored procedure
        cursor.callproc('CreateUser', [email, first, last, phone, title])
        conn.commit()  # Commit the transaction
        messagebox.showinfo("Success", "User created successfully!")
        return
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        cursor.close()
        conn.close()


#Function to load the adduser screen when the button is clicked
def adduser():
    #Window settings
    root = tk.Toplevel()
    root.title("Add Users and Cases")
    root.geometry("300x400")
    root.configure(bg="lavender", padx=20, pady=20)
    root.resizable(False, False)
    #Widgets - textboxes and labels
    email_label = tk.Label(root, text="Email:", bg="lavender")
    email_label.pack()
    email_entry = tk.Entry(root, bd=5)
    email_entry.pack()
    fn_label = tk.Label(root, text="First Name:", bg="lavender")
    fn_label.pack()
    fn_entry = tk.Entry(root, bd=5)
    fn_entry.pack()
    ln_label = tk.Label(root, text="Last Name:", bg="lavender")
    ln_label.pack()
    ln_entry = tk.Entry(root, bd=5)
    ln_entry.pack()
    phone_label = tk.Label(root, text="Phone Number:", bg="lavender")
    phone_label.pack()
    phone_entry = tk.Entry(root, bd=5)
    phone_entry.pack()
    title_label = tk.Label(root, text="Title:", bg="lavender")
    title_label.pack()
    title_entry = tk.Entry(root, bd=5)
    title_entry.pack()
    #Buttons to add user to database or exit
    btn_adduser = tk.Button(root, text="Add User", command=lambda: create_user(email_entry.get(), fn_entry.get(), ln_entry.get(), phone_entry.get(), title_entry.get()), width=10)
    btn_adduser.place(x=25, y=280)
    btn_cancel = tk.Button(root, text="Exit", command=root.withdraw, width=10)
    btn_cancel.place(x=150, y=280)

def case():
    root = tk.Tk()
    root.title("Assign Case Files")
    root.geometry("800x400")
    root.configure(bg="lavender", padx=20, pady=10)
    root.resizable(False, False)

def hashes():
    root = tk.Tk()
    root.title("Verify Hashes")
    root.geometry("800x400")
    root.configure(bg="lavender", padx=20, pady=10)
    root.resizable(False, False)

#Function to grab user data to display
def fetch_and_display_data():
    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Query to fetch user data (You can change this query for other tables)
        query = "SELECT UserID, Email, FirstName, LastName, Phone, Title FROM Users"
        cursor.execute(query)

        # Fetch all results
        rows = cursor.fetchall()

        # Create a new window for the data viewer
        viewer_window = tk.Toplevel()
        viewer_window.title("View System Data")
        viewer_window.geometry("800x400")
        viewer_window.configure(bg="lavender", padx=20, pady=10)

        # Create Treeview widget
        tree = ttk.Treeview(viewer_window, columns=("User ID", "Email", "First Name", "Last Name", "Phone", "Title"), show="headings")

        # Define columns and headings
        tree.heading("User ID", text="User ID")
        tree.heading("Email", text="Email")
        tree.heading("First Name", text="First Name")
        tree.heading("Last Name", text="Last Name")
        tree.heading("Phone", text="Phone")
        tree.heading("Title", text="Title")

        # Set column widths
        tree.column("User ID", width=50)
        tree.column("Email", width=200)
        tree.column("First Name", width=100)
        tree.column("Last Name", width=150)
        tree.column("Phone", width=150)
        tree.column("Title", width=100)

        # Insert rows into the Treeview widget
        for row in rows:
            tree.insert("", "end", values=row)

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(viewer_window, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        tree.pack(padx=10, pady=10, fill="both", expand=True)

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error fetching data: {err}")

    finally:
        cursor.close()
        conn.close()


def open_admin_dashboard(root):
    admin_window=tk.Toplevel(root)
    admin_window.title("TM Dashboard")
    admin_window.geometry("1000x500")
    admin_window.configure(bg="lavender") #padding can be added here
    admin_window.resizable(False, False)
    btn_user=tk.Button(admin_window, text="Manage Users", width=20, command=adduser)
    btn_user.place(x=60, y=280)
    btn_case=tk.Button(admin_window, text="Assign Cases", width=20, command=case)
    btn_case.place(x=300, y=280)
    btn_hashes=tk.Button(admin_window, text="Verify Hash Values", width=20, command=hashes)
    btn_hashes.place(x=540, y=280)
    btn_viewer=tk.Button(admin_window, text="View Stored Data", width=20, command=fetch_and_display_data)
    btn_viewer.place(x=780, y=280)

