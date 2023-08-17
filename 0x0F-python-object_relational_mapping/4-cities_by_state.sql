-- File: 4-cities_by_state.sql
-- Author: Alexander Udeogaranya
--
-- This SQL script creates the `states` and `cities` tables in
-- the `hbtn_0e_4_usa` database.
-- It also populates these tables with sample data for demonstration purposes.
--
-- Usage:
--   1. Execute this script in a MySQL database environment.
--
-- Example:
--   After executing the script, you can query the `cities` and `states`
--   tables to retrieve information about cities & their corresponding states.

-- Create the `hbtn_0e_4_usa` database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0e_4_usa;

-- Switch to the `hbtn_0e_4_usa` database
USE hbtn_0e_4_usa;

-- Create the `states` table with an auto-incrementing ID and a name column
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);

-- Insert sample state data into the `states` table
INSERT INTO states (name)
VALUES
    ("California"),
    ("Arizona"),
    ("Texas"),
    ("New York"),
    ("Nevada");

-- Create the `cities` table with: auto-incrementing ID,
-- `state_id` foreign key, and a name column
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);

-- Insert sample city data into the `cities` table
INSERT INTO cities (state_id, name)
VALUES
    (1, "San Francisco"),
    (1, "San Jose"),
    (1, "Los Angeles"),
    (1, "Fremont"),
    (1, "Livermore"),
    (2, "Page"),
    (2, "Phoenix"),
    (3, "Dallas"),
    (3, "Houston"),
    (3, "Austin"),
    (4, "New York"),
    (5, "Las Vegas"),
    (5, "Reno"),
    (5, "Henderson"),
    (5, "Carson City");
