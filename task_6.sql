-- Insert multiple rows in the table customer (database alx_book_store) in your MySQL server.
USE alx_book_store;

-- Define the values to insert
SET @customer_id_1 = 2;
SET @customer_name_1 = 'Blessing Malik';
SET @email_1 = 'bmalik@sandtech.com';
SET @address_1 = '124 Happiness  Ave.';

SET @customer_id_2 = 3;
SET @customer_name_2 = 'Obed Ehoneah';
SET @email_2 = 'eobed@sandtech.com';
SET @address_2 = '125 Happiness  Ave.';

SET @customer_id_3 = 4;
SET @customer_name_3 = 'Nehemial Kamolu';
SET @email_3 = 'nkamolu@sandtech.com';
SET @address_3 = '126 Happiness  Ave.';

-- Insert the rows
INSERT INTO customer (customer_id, customer_name, email, address)
VALUES (@customer_id_1, @customer_name_1, @email_1, @address_1),
       (@customer_id_2, @customer_name_2, @email_2, @address_2),
       (@customer_id_3, @customer_name_3, @email_3, @address_3);

-- Print the inserted rows
SELECT * FROM customer WHERE customer_id IN (2, 3, 4);
