import mysql.connector

dataBase = mysql.connector.connect(
    host ="localhost",
    user ="root",
    password ="root",
    database = "my_python",
)

cursorObject = dataBase.cursor()

query = "DELETE FROM Employee WHERE first_name='Anjali'"
cursorObject.execute(query)
dataBase.commit()

dataBase.close()