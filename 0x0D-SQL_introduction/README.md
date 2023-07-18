SQL - Introduction

This repository contains solutions for the SQL Introduction project of the ALX Higher Level Programming curriculum. The project covers various SQL concepts and commands to interact with databases using MySQL.

## Table of Contents

- [Project Description](#project-description)
- [Learning Objectives](#learning-objectives)
- [Installation](#installation)
- [Usage](#usage)
- [Project Files](#project-files)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## Project Description

The SQL Introduction project introduces fundamental concepts of databases, relational databases, and SQL. It covers topics such as creating databases, tables, and manipulating data using SQL queries. The project also explores the usage of SQL functions, subqueries, and basic data analysis operations.

## Learning Objectives

Upon completion of this project, students are expected to be able to:

- Understand the concept of a database and a relational database.
- Explain what SQL stands for and its role in interacting with databases.
- Create a database and tables using Data Definition Language (DDL) commands.
- Retrieve data from a table using SELECT statements.
- Perform data manipulation operations using INSERT, UPDATE, and DELETE statements.
- Utilize subqueries and SQL functions for more advanced queries.
- Understand the importance of proper database design and table relationships.

## Installation

To run the SQL scripts, you need to have MySQL 8.0 installed on Ubuntu 20.04 LTS. You can follow these steps to install MySQL:

```bash
$ sudo apt update
$ sudo apt install mysql-server
```

## Usage

To execute the SQL scripts, follow these steps:

1. Connect to the MySQL server using the appropriate credentials.
2. Navigate to the directory containing the SQL script files.
3. Run the desired SQL script using the `mysql` command followed by the script file.

Example:

```bash
$ mysql -h localhost -u root -p < 0-list_databases.sql
```

Make sure to replace the file name (`0-list_databases.sql`) with the appropriate script file.

## Project Files

This project includes the following files:

- `0-list_databases.sql`: Script to list all databases in the MySQL server.
- `1-create_database_if_missing.sql`: Script to create the `hbtn_0c_0` database if it doesn't exist.
- `2-remove_database.sql`: Script to delete the `hbtn_0c_0` database if it exists.
- `3-list_tables.sql`: Script to list all tables in a specified database.
- `4-first_table.sql`: Script to create the `first_table` table in the `hbtn_0c_0` database.
- `5-full_table.sql`: Script to display the full description of the `first_table` in the `hbtn_0c_0` database.
- `6-list_values.sql`: Script to list all rows in the `first_table` of the `hbtn_0c_0` database.
- `7-insert_value.sql`: Script to insert a new row into the `first_table` of the `hbtn_0c_0` database.
- `8-count_89.sql`: Script to display the number of records with `id = 89` in the `first_table` of the `hbtn_0c_0` database.
- `9-full_creation.sql`: Script to create the `second_table` table and insert multiple rows into it in the `hbtn_0c_0` database.
- `10-top_score.sql`: Script to list all records in the `second_table` of the `hbtn_0c_0` database, ordered by score (descending).
- `11-best_score.sql`: Script to list records with a score greater than or equal to 10 in the `second_table` of the `hbtn_0c_0` database.
- `12-no_cheating.sql`: Script to update the score of a record with the name "Bob" to 10 in the `second_table` of the `hbtn_0c_0` database.
- `13-change_class.sql`: Script to remove records with a score less than or equal to 5 from the `second_table` of the `hbtn_0c_0` database.
- `14-average.sql`: Script to compute the average score of all records in the `second_table` of the `hbtn_0c_0` database.
- `15-groups.sql`: Script to display the number of records with the same score in the `second_table` of the `hbtn_0c_0` database, sorted by the number of records.
- `16-no_link.sql`: Script to list all records in the `second_table` of the `hbtn_0c_0` database, excluding rows without a name value, ordered by descending score.
- `100-move_to_utf8.sql`: Script to convert the `hbtn_0c_0` database, `first_table` table, and `name` field to UTF8 encoding.
- `101-avg_temperatures.sql`: Script to display the average temperature by city (in Fahrenheit) from a temperature table in the `hbtn_0c_0` database.
- `102-top_city.sql`: Script to display the top 3 cities with the highest temperatures during July and August from a temperature table in the `hbtn_0c_0` database.
- `103-max_state.sql`: Script to display the maximum temperature of each state, ordered by state name, from a temperature table in the `hbtn_0c_0` database.

## Contributing

Contributions to this project are not accepted as it is a part of the ALX Higher Level Programming curriculum.

## License

This project is licensed under the [MIT License](LICENSE).

## Author

This project was implemented by Alexander Udeoagranya. You can find the GitHub repository at [https://github.com/Dr-dyrane/alx-higher_level_programming/0x0D-SQL_introduction](https://github.com/Dr-dyrane/alx-higher_level_programming/0x0D-SQL_introduction).

