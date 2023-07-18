-- This SQL script creates a table called first_table in the current database in the MySQL server. The table has two columns: id (INT) and name (VARCHAR(256)). If the table first_table already exists, the script will not fail.
CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
