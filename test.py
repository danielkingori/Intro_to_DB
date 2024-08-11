import mysql.connector
mydatabase =  mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "12345678",
    database = "mydatabase" 
)
mycursor = mydatabase.cursor()
# mycursor.execute("SHOW DATABASES")
# # mycursor.execute("SELECT * FROM demo")
# for i in mycursor:
#     print(i)
    
def create_record(employee_id, first_name, last_name, department, hire_date):
    # create = "CREATE TABLE employees(firstname VARCHAR(50), lastname VARCHAR(50), position VARCHAR(100) UNIQUE, salary)"
    check_query = "SELECT * FROM Employees where employee_id = %s AND first_name = %s AND last_name = %s AND department = %s AND hire_date = %s"
    mycursor.execute(check_query, (employee_id, first_name, last_name, department, hire_date))
    result = mycursor.fetchone()
    if result:
        print("Record already exists")
    else:
        query = "INSERT INTO Employees(employee_id, first_name, last_name, department, hire_date) VALUES(%s, %s, %s, %s, %s)"
        values = (employee_id, first_name, last_name, department, hire_date) #tuple
        mycursor.execute(query, values )
        mydatabase.commit()
        print("record added successifully")
    
create_record(6, "D5au", "K5spn", "Idd", '2012-10-21')
    

def update_record(employee_id, department):
    query = "UPDATE Employees SET department = %s WHERE employee_id = %s"
    values = (department, employee_id)
    mycursor.execute(query, values)
    mydatabase.commit()
    print("Update successiful")
update_record(4, 'It')


def delete_record(employee_id):
    query = "DELETE FROM Employees WHERE employee_id = %s"
    values = (employee_id)
    mycursor.execute(query, (values,))
    mydatabase.commit()
    print("record deleted")
delete_record(6)


def read():
    query = "SELECT * FROM Employees"
    mycursor.execute(query)
    output = mycursor.fetchall()
    for rows in output:
        print(rows)
read()

mycursor.close()
mydatabase.close()