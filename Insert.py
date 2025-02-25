import mysql.connector


dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="my_python",
)

cursorObject = dataBase.cursor()


department_query = "INSERT INTO Department (dep_id, dep_name) VALUES (%s, %s)"
departments = [
    (1, "IT"),
    (2, "HR"),
    (3, "Finance"),
    (4, "Marketing"),
    (5, "Operations"),
]

cursorObject.executemany(department_query, departments)
dataBase.commit()


employee_query = """
    INSERT INTO Employee (emp_id, birth_date, first_name, last_name, gender, hire_date, dep_id) 
    VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

employees = [
    (101, '2001-11-15', 'Ronak', 'Patel', 'Male', '2025-01-14', 1), 
    (102, '1995-06-25', 'Amit', 'Sharma', 'Male', '2023-07-20', 2),
    (103, '1998-12-10', 'Priya', 'Verma', 'Female', '2024-05-01', 3),
    (104, '2000-04-18', 'Vikram', 'Singh', 'Male', '2025-02-10', 4),
    (105, '1997-09-30', 'Anjali', 'Nair', 'Female', '2024-08-15', 5),
]

cursorObject.executemany(employee_query, employees)
dataBase.commit()


dataBase.close()
print("Record inserted successfully!")
