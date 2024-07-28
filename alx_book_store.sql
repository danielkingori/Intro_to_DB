CREATE DATABASE IF NOT EXISTS alx_book_store

CREATE TABLE Books (
book_id (Primary Key)
title VARCHAR(130)
author_id (Foreign Key referencing Authors table)
price DOUBLE
publication_date DATE
);

CREATE TABLE Authors (
author_id (PRIMARY KEY)
author_name VARCHAR(215)
);

CREATE TABLE Customers (
customer_id (Primary Key)
customer_name VARCHAR(215)
email VARCHAR(215)
address TEXT
);

CREATE TABLE Orders (
order_id INT (Primary Key)
customer_id INT
FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
order_date DATE
);

CREATE TABLE Order_Details(
orderdetailid (Primary Key)
order_id (Foreign Key referencing Orders table)
book_id INT 
FOREIGN KEY (order_id) REFERENCES Orders(order_id)
FOREIGN KEY (book_id) REFERENCES Books(book_id)
);
