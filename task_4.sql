-- Print the full description of the table books from the database alx_book_store in your MySQL server.
USE alx_book_store;

-- Get the table structure as a string
SELECT CONCAT("DESCRIBE `", table_name, "`;") AS stmt
FROM information_schema.tables
WHERE table_name = 'books' AND table_schema = DATABASE();
