import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE My_Python")

dataBase.close()

print("Database Created successfully!")