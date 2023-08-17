-- 6-model_state.sql
-- Author: Alexander Udeogaranya

-- Description:
-- This script creates a database 'hbtn_0e_6_usa', switches to it,
-- and retrieves the CREATE TABLE statement for the 'states' table.

-- Usage:
-- Run this script in your MySQL client to create the database and view the CREATE TABLE statement.

-- Note:
-- Make sure to have a MySQL server running and accessible.

-- Create the 'hbtn_0e_6_usa' database if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0e_6_usa;

-- Use the 'hbtn_0e_6_usa' database
USE hbtn_0e_6_usa;

-- Display the CREATE TABLE statement for the 'states' table
SHOW CREATE TABLE states;
