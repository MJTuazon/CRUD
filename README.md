Employee CRUD Application
This is a Python-based Employee CRUD (Create, Read, Update, Delete) Application using Tkinter for the GUI and SQLite for the database.

Features:
Add employee data (Full name, Address, Birthdate, Age, Gender, Civil Status, Contact Number, Salary)
View employee list
Update existing employee data
Delete employee data
Prerequisites:
Before running this application, make sure you have the following installed:

Python 3.x
Tkinter (Usually comes pre-installed with Python)
tkcalendar for date picker functionality
SQLite (included with Python's standard library)

To install tkcalendar, run:
pip install tkcalendar


1.Run the Application:
Clone the repository or download the files to your local machine.
Open a terminal or command prompt and navigate to the folder where the program is stored.
Run the script:
python create_database.py

2.Insert Employee Data:
Fill out the form with the employee’s details.
Click on the Insert Employee button to save the employee to the database.

3.View Employee List:
Click on the View Employees button to display the list of all employees.
The list will show ID, Name, Address, Birthdate, Age, Gender, Civil Status, Contact, and Salary.

4.Update Employee:
Double-click on an employee in the list to populate the fields with the employee’s information.
Make changes to the fields and click Update Employee to save the updated information.

5.Delete Employee:
Select an employee from the list and click Delete Employee to remove that employee from the database.

Database:
This application uses SQLite to store employee data. The database is saved as employeedb.db in the same directory.
