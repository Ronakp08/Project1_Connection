import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root"
)


print(dataBase)

dataBase.close()


print("Connection Established successfully!")