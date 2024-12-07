import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3

# Create the main window
root = tk.Tk()
root.title("Employee CRUD Application")

# Set window size
root.geometry("600x600")

# Define input fields and labels
label_fullname = tk.Label(root, text="Full Name")
label_fullname.grid(row=0, column=0)
entry_fullname = tk.Entry(root)
entry_fullname.grid(row=0, column=1)

label_address = tk.Label(root, text="Address")
label_address.grid(row=1, column=0)
entry_address = tk.Entry(root)
entry_address.grid(row=1, column=1)

label_birthdate = tk.Label(root, text="Birthdate (YYYY-MM-DD)")
label_birthdate.grid(row=2, column=0)
entry_birthdate = tk.Entry(root)
entry_birthdate.grid(row=2, column=1)

label_age = tk.Label(root, text="Age")
label_age.grid(row=3, column=0)
entry_age = tk.Entry(root)
entry_age.grid(row=3, column=1)

label_gender = tk.Label(root, text="Gender")
label_gender.grid(row=4, column=0)
entry_gender = tk.Entry(root)
entry_gender.grid(row=4, column=1)

label_civilstat = tk.Label(root, text="Civil Status")
label_civilstat.grid(row=5, column=0)
entry_civilstat = tk.Entry(root)
entry_civilstat.grid(row=5, column=1)

label_contactnum = tk.Label(root, text="Contact Number")
label_contactnum.grid(row=6, column=0)
entry_contactnum = tk.Entry(root)
entry_contactnum.grid(row=6, column=1)

label_salary = tk.Label(root, text="Salary")
label_salary.grid(row=7, column=0)
entry_salary = tk.Entry(root)
entry_salary.grid(row=7, column=1)

# Create a function to insert data into the database
def insert_data():
    # Get data from input fields
    fullname = entry_fullname.get()
    address = entry_address.get()
    birthdate = entry_birthdate.get()
    age = entry_age.get()
    gender = entry_gender.get()
    civilstat = entry_civilstat.get()
    contactnum = entry_contactnum.get()
    salary = entry_salary.get()

    if not fullname or not address or not birthdate or not age or not gender or not civilstat or not contactnum or not salary:
        messagebox.showerror("Input Error", "All fields are required!")
        return

    # Connect to the database
    conn = sqlite3.connect('employeedb.db')
    cursor = conn.cursor()

    # Insert data into the database
    cursor.execute('''
    INSERT INTO employeefile (fullname, address, birthdate, age, gender, civilstat, contactnum, salary, isactive)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (fullname, address, birthdate, age, gender, civilstat, contactnum, salary, 1))

    conn.commit()
    conn.close()

    # Clear the input fields
    entry_fullname.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    entry_birthdate.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_gender.delete(0, tk.END)
    entry_civilstat.delete(0, tk.END)
    entry_contactnum.delete(0, tk.END)
    entry_salary.delete(0, tk.END)

    messagebox.showinfo("Success", "Employee added successfully!")

# Create a function to view all employees
def view_employees():
    # Clear the listbox before adding new entries
    listbox.delete(0, tk.END)

    # Connect to the database
    conn = sqlite3.connect('employeedb.db')
    cursor = conn.cursor()

    # Fetch all employee records
    cursor.execute("SELECT * FROM employeefile")
    employees = cursor.fetchall()

    # Add each employee to the listbox
    for employee in employees:
        listbox.insert(tk.END, f"ID: {employee[0]}, Name: {employee[1]}, Address: {employee[2]}, Birthdate: {employee[3]}, Age: {employee[4]}, Gender: {employee[5]}, Civil Status: {employee[6]}, Contact: {employee[7]}, Salary: {employee[8]}, Active: {employee[9]}")

    conn.close()

# Create an Insert Button
insert_button = tk.Button(root, text="Insert Employee", command=insert_data)
insert_button.grid(row=8, column=0, columnspan=2)

# Create a View Button
view_button = tk.Button(root, text="View Employees", command=view_employees)
view_button.grid(row=9, column=0, columnspan=2)

# Create a Listbox to display employee records
listbox = tk.Listbox(root, width=80, height=10)
listbox.grid(row=10, column=0, columnspan=2)

# Start the GUI
root.mainloop()
