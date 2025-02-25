import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "my_python",
)

cursorObject = dataBase.cursor()

update1 = "UPDATE Employee SET first_name = 'Kruti' WHERE first_name = 'Priya'"
cursorObject.execute(update1)
dataBase.commit()

print("Record updated successfully.........")

dataBase.close()