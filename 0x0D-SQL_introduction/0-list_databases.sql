-- Script name: 
-- 0-list_databases.sql
-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
-- Description:
-- This SQL script lists all the databases present on the MySQL server.
-- Usage:
-- 1. Save this script in a .sql file (e.g., 0-list_databases.sql).
-- 2. Run the following command in the terminal:
--      $ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
-- Replace `-hlocalhost` with the appropriate host if your MySQL server
--           is running on a different machine.
-- Provide the MySQL root user password when prompted (`-uroot -p`).
-- Example:
-- Suppose the script is saved in a file named `0-list_databases.sql`.
--            Run the following command:
-- $ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
-- Enter password:
-- Database
-- hbtn_0c_0
-- information_schema
-- mysql
-- performance_schema
-- sys
-- Dependencies:
-- None
-- Author:
-- Alexander Udeogaranya
-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
-- Implementation:
SHOW DATABASES;
