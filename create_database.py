import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
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

label_birthdate = tk.Label(root, text="Birthdate")
label_birthdate.grid(row=2, column=0)

# Use DateEntry from tkcalendar for birthdate
entry_birthdate = DateEntry(root, date_pattern='yyyy-mm-dd')
entry_birthdate.grid(row=2, column=1)

label_age = tk.Label(root, text="Age")
label_age.grid(row=3, column=0)
entry_age = tk.Entry(root)
entry_age.grid(row=3, column=1)

label_gender = tk.Label(root, text="Gender")
label_gender.grid(row=4, column=0)

# Variable to store gender value
gender_var = tk.StringVar()

# Radiobuttons for gender
male_button = tk.Radiobutton(root, text="Male", variable=gender_var, value="Male")
male_button.grid(row=4, column=1, sticky="w")

female_button = tk.Radiobutton(root, text="Female", variable=gender_var, value="Female")
female_button.grid(row=4, column=1, sticky="w", padx=80)

other_button = tk.Radiobutton(root, text="Other", variable=gender_var, value="Other")
other_button.grid(row=4, column=1, sticky="w", padx=160)

label_civilstat = tk.Label(root, text="Civil Status")
label_civilstat.grid(row=5, column=0)

# Variable to store civil status value
civilstat_var = tk.StringVar()

# Radiobuttons for civil status
single_button = tk.Radiobutton(root, text="Single", variable=civilstat_var, value="Single")
single_button.grid(row=5, column=1, sticky="w")

married_button = tk.Radiobutton(root, text="Married", variable=civilstat_var, value="Married")
married_button.grid(row=5, column=1, sticky="w", padx=80)

separated_button = tk.Radiobutton(root, text="Separated", variable=civilstat_var, value="Separated")
separated_button.grid(row=5, column=1, sticky="w", padx=160)

widowed_button = tk.Radiobutton(root, text="Widowed", variable=civilstat_var, value="Widowed")
widowed_button.grid(row=5, column=1, sticky="w", padx=240)

label_contactnum = tk.Label(root, text="Contact Number")
label_contactnum.grid(row=6, column=0)
entry_contactnum = tk.Entry(root)
entry_contactnum.grid(row=6, column=1)

label_salary = tk.Label(root, text="Salary")
label_salary.grid(row=7, column=0)
entry_salary = tk.Entry(root)
entry_salary.grid(row=7, column=1)

# Function to check if the input is numeric
def is_numeric(value):
    return value.isdigit()

# Function to clear the date picker
def clear_date_picker():
    entry_birthdate.set_date(None)  # Reset the date picker to the default (None)

# Create a function to insert data into the database
def insert_data():
    # Get data from input fields
    fullname = entry_fullname.get()
    address = entry_address.get()
    birthdate = entry_birthdate.get_date()  # Get selected date from DateEntry widget
    age = entry_age.get()
    gender = gender_var.get()  # Get the selected gender
    civilstat = civilstat_var.get()  # Get the selected civil status
    contactnum = entry_contactnum.get()
    salary = entry_salary.get()

    if not fullname or not address or not birthdate or not age or not gender or not civilstat or not contactnum or not salary:
        messagebox.showerror("Input Error", "All fields are required!")
        return

    if not is_numeric(contactnum):
        messagebox.showerror("Input Error", "Contact number must be numeric!")
        return

    if not is_numeric(age):
        messagebox.showerror("Input Error", "Age must be numeric!")
        return

    if not is_numeric(salary):
        messagebox.showerror("Input Error", "Salary must be numeric!")
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
    clear_date_picker()  # Clear the date picker
    entry_age.delete(0, tk.END)
    gender_var.set("")  # Clear gender selection
    civilstat_var.set("")  # Clear civil status selection
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

# Create a function to populate fields for updating an employee
def select_employee(event):
    # Get the selected employee from the listbox
    selected_employee = listbox.get(listbox.curselection())
    selected_employee_id = selected_employee.split(',')[0].split(':')[1].strip()  # Extract ID from the selection

    # Connect to the database
    conn = sqlite3.connect('employeedb.db')
    cursor = conn.cursor()

    # Fetch the selected employee record
    cursor.execute("SELECT * FROM employeefile WHERE recid = ?", (selected_employee_id,))
    employee = cursor.fetchone()

    # Populate fields with the selected employee's data
    entry_fullname.delete(0, tk.END)
    entry_fullname.insert(0, employee[1])
    entry_address.delete(0, tk.END)
    entry_address.insert(0, employee[2])
    entry_birthdate.set_date(employee[3])  # Set the birthdate picker
    entry_age.delete(0, tk.END)
    entry_age.insert(0, employee[4])
    gender_var.set(employee[5])  # Set the gender
    civilstat_var.set(employee[6])  # Set the civil status
    entry_contactnum.delete(0, tk.END)
    entry_contactnum.insert(0, employee[7])
    entry_salary.delete(0, tk.END)
    entry_salary.insert(0, employee[8])

    conn.close()

    # Enable the update button once an employee is selected
    update_button.config(state=tk.NORMAL)
    update_button.config(command=lambda: update_employee(employee[0]))

    # Enable the delete button once an employee is selected
    delete_button.config(state=tk.NORMAL)
    delete_button.config(command=lambda: delete_employee(employee[0]))

# Create a function to update the employee details
def update_employee(employee_id):
    # Get updated data from input fields
    fullname = entry_fullname.get()
    address = entry_address.get()
    birthdate = entry_birthdate.get_date()  # Get selected date from DateEntry widget
    age = entry_age.get()
    gender = gender_var.get()  # Get the selected gender
    civilstat = civilstat_var.get()  # Get the selected civil status
    contactnum = entry_contactnum.get()
    salary = entry_salary.get()

    if not fullname or not address or not birthdate or not age or not gender or not civilstat or not contactnum or not salary:
        messagebox.showerror("Input Error", "All fields are required!")
        return

    if not is_numeric(contactnum):
        messagebox.showerror("Input Error", "Contact number must be numeric!")
        return

    if not is_numeric(age):
        messagebox.showerror("Input Error", "Age must be numeric!")
        return

    if not is_numeric(salary):
        messagebox.showerror("Input Error", "Salary must be numeric!")
        return

    # Connect to the database
    conn = sqlite3.connect('employeedb.db')
    cursor = conn.cursor()

    # Update employee data in the database
    cursor.execute('''
    UPDATE employeefile
    SET fullname = ?, address = ?, birthdate = ?, age = ?, gender = ?, civilstat = ?, contactnum = ?, salary = ?
    WHERE recid = ?
    ''', (fullname, address, birthdate, age, gender, civilstat, contactnum, salary, employee_id))

    conn.commit()
    conn.close()

    # Clear the input fields
    entry_fullname.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    clear_date_picker()  # Clear the date picker
    entry_age.delete(0, tk.END)
    gender_var.set("")  # Clear gender selection
    civilstat_var.set("")  # Clear civil status selection
    entry_contactnum.delete(0, tk.END)
    entry_salary.delete(0, tk.END)

    messagebox.showinfo("Success", "Employee updated successfully!")

# Create a function to delete an employee
def delete_employee(employee_id):
    # Connect to the database
    conn = sqlite3.connect('employeedb.db')
    cursor = conn.cursor()

    # Delete the selected employee
    cursor.execute("DELETE FROM employeefile WHERE recid = ?", (employee_id,))
    conn.commit()
    conn.close()

    # Refresh the employee list
    view_employees()

    # Clear the input fields
    entry_fullname.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    clear_date_picker()  # Clear the date picker
    entry_age.delete(0, tk.END)
    gender_var.set("")  # Clear gender selection
    civilstat_var.set("")  # Clear civil status selection
    entry_contactnum.delete(0, tk.END)
    entry_salary.delete(0, tk.END)

    messagebox.showinfo("Success", "Employee deleted successfully!")

# Create Insert, View, Update, Delete buttons
insert_button = tk.Button(root, text="Insert Employee", command=insert_data)
insert_button.grid(row=8, column=0, columnspan=2)

view_button = tk.Button(root, text="View Employees", command=view_employees)
view_button.grid(row=9, column=0, columnspan=2)

update_button = tk.Button(root, text="Update Employee", state=tk.DISABLED)
update_button.grid(row=10, column=0, columnspan=2)

delete_button = tk.Button(root, text="Delete Employee", state=tk.DISABLED)
delete_button.grid(row=11, column=0, columnspan=2)

# Create Listbox to display employees
listbox = tk.Listbox(root, height=10, width=80)
listbox.grid(row=12, column=0, columnspan=2, padx=10, pady=10)

# Bind the listbox selection to the select_employee function
listbox.bind("<Double-1>", select_employee)

# Start the GUI
root.mainloop()
