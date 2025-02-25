import mysql.connector


dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "my_python",
)

cursorObject = dataBase.cursor()

Department_query = """CREATE TABLE Department(dep_id INT PRIMARY KEY AUTO_INCREMENT,
dep_name VARCHAR(100) NOT NULL)"""

cursorObject.execute(Department_query)

Employess_query = """CREATE TABLE Employee (
    emp_id INT PRIMARY KEY,
    birth_date DATE NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    gender VARCHAR(10) NOT NULL,
    hire_date DATE NOT NULL,
    dep_id INT,
    FOREIGN KEY (dep_id) REFERENCES Department(dep_id)
)"""
cursorObject.execute(Employess_query)

dataBase.close()

print("Table Created successfully!")