-- Description: Converts the hbtn_0c_0 database, first_table table, and name field in first_table
--to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in the MySQL server.
USE `hbtn_0c_0` ALTER TABLE `first_table` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
