import mysql.connector

# Database connection details (replace with your own)
mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="alx_book_store"
)

mycursor = mydb.cursor()

# Create a table named `books` (if it doesn't exist)
mycursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(130) NOT NULL,
    author_id INT NOT NULL,
    price DOUBLE NOT NULL,
    publication_date DATE NOT NULL,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
)
""")

print("Table created successfully!")

# Insert some book data
sql = "INSERT INTO books (title, author_id, price, publication_date) VALUES (%s, %s, %s, %s)"
val = ("Book Title 1", 1, 19.99, '2022-01-01')
mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, "record(s) inserted.")

val = ("Book Title 2", 2, 29.99, '2021-05-15')
mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, "record(s) inserted.")

# Read all book data
mycursor.execute("SELECT * FROM books")
myresult = mycursor.fetchall()

print("Books:")
for row in myresult:
    print(row)

# Update a book's price
sql = "UPDATE books SET price = %s WHERE book_id = %s"
val = (14.99, 1)
mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, "record(s) updated.")

# Read the updated book data
mycursor.execute("SELECT * FROM books WHERE book_id = 1")
myresult = mycursor.fetchone()

print("Updated book:")
print(myresult)

# Delete a book
sql = "DELETE FROM books WHERE book_id = 2"
mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount, "record(s) deleted.")

# Close connections
mycursor.close()
mydb.close()

print("Database connection closed.")
