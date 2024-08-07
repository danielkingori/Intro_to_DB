-- Print the full description of the table books from the database alx_book_store in your MySQL server.
USE alx_book_store;

-- Get the table structure as a string
SELECT CONCAT(
    "Column_name: ", COLUMN_NAME, "\n",
    "Type: ", DATA_TYPE, "\n",
    "Is_nullable: ", IS_NULLABLE, "\n",
    "Column_key: ", COLUMN_KEY, "\n",
    "Column_default: ", COLUMN_DEFAULT, "\n",
    "Extra: ", COLUMN_TYPE, "\n\n"
) AS stmt
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'Books' AND TABLE_SCHEMA = 'alx_book_store';
