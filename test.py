import mysql.connector
mydatabase =  mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "12345678"
)
mycursor = mydatabase.cursor()
mycursor.execute("SHOW DATABASES")
for i in mycursor:
    print(i)
    