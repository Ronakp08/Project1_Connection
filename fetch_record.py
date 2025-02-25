import mysql.connector

dataBase = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "root",
    database = "my_python"
)

cursorObject = dataBase.cursor()


# Whole Record Fetching

print("\n" + "-" * 50)    
print("DEPARTMENT RECORDS: ")
print("-" * 50) 

query = "Select * FROM Department"
cursorObject.execute(query)

myResult = cursorObject.fetchall()

for i in myResult:
    print(i)

    
print("\n" + "-" * 50)    
print("EMPLOYEE RECORDS: ")
print("-" * 50) 
    

Employee = "Select * FROM Employee"
cursorObject.execute(Employee)

myEmployee = cursorObject.fetchall()

for i in myEmployee:
    print(i)
    

#Clauses

whereClause = "SELECT * FROM Employee WHERE first_name = 'Ronak'"
cursorObject.execute(whereClause)

whereResult = cursorObject.fetchall()

print("\n" + "-" * 50)    
print("WHERE CLAUSE: ")
print("-" * 50) 
    
for x in whereResult:
    print(x)

#WHERE 2

whereClause2 = "SELECT * FROM Employee WHERE gender = 'male'"
cursorObject.execute(whereClause2)

whereResult2 = cursorObject.fetchall()

print("\n" + "-" * 50)    
print("WHERE CLAUSE 2: ")
print("-" * 50) 
    
for x in whereResult2:
    print(x)
    
    
#Order by clause

orderBy = "SELECT * FROM Employee ORDER BY first_name DESC"  
cursorObject.execute(orderBy)

orderResult = cursorObject.fetchall()

print("\n" + "-" * 50)    
print("ORDER BY CLAUSE: ")
print("-" * 50) 

for i in orderResult:
    print(i) 
    
    
    
#Limit 

limit = "SELECT * FROM Employee LIMIT 2 OFFSET 1"
cursorObject.execute(limit)

limitResult = cursorObject.fetchall()

print("\n" + "-" * 50)    
print("LIMIT CLAUSE: ")
print("-" * 50) 


for i in limitResult:
    print(i)
    
    
dataBase.close()