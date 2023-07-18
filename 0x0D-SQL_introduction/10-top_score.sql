-- Script name: 10-top_score.sql
-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
-- Description:
-- This SQL script lists all records of the table second_table from the database hbtn_0c_0 in the MySQL server.
-- The results include the score and name fields, and they are ordered by the score in descending order.
-- Usage:
-- 1. Save this script in a .sql file (e.g., 10-top_score.sql).
-- 2. Run the following command in the terminal:
--      $ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
-- Replace `-hlocalhost` with the appropriate host if your MySQL server
--           is running on a different machine.
-- Provide the MySQL root user password when prompted (`-uroot -p`).
-- Example:
-- Suppose the script is saved in a file named `10-top_score.sql`.
--            Run the following command:
-- $ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
-- Enter password:
-- score   name
-- 14  Bob
-- 10  John
-- 8   George
-- 3   Alex
-- Dependencies:
-- None
-- Author:
-- Alexander Udeogaranya
-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
-- Implementation:
SELECT score,
    name
FROM second_table
ORDER BY score DESC;
