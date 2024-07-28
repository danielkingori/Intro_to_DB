-- Insert a single row in the table customer (database alx_book_store) in your MySQL server.
USE alx_book_store;

-- Define the values to insert
SET @customer_id = 1;
SET @customer_name = 'Cole Baidoo';
SET @email = 'cbaidoo@sandtech.com';
SET @address = '123 Happiness Ave.';

-- Insert the row
INSERT INTO Customers (customer_id, customer_name, email, address)
VALUES (@customer_id, @customer_name, @email, @address);

-- Print the inserted row
SELECT * FROM Customers WHERE customer_id = @customer_id;
