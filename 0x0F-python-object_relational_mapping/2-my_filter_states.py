#!/usr/bin/python3
"""
This script interacts with a MySQL database to retrieve and display
states whose names match a provided search argument. It connects to
the 'hbtn_0e_0_usa' database using the given credentials and fetches
all rows from the 'states' table where the 'name' column matches the
provided search argument. The retrieved states are then printed to the console.

Author: Alexander Udeogaranya

Usage:
    ./2-my_filter_states.py <db_username> <db_password> <db_name> <name_to_search>

Arguments:
    <db_username>: Username for database access.
    <db_password>: Password for database access.
    <db_name>: Name of the database to connect to.
    <name_to_search>: The name to search for in the states.

Example:
    ./2-my_filter_states.py root mypassword hbtn_0e_0_usa Texas

Output:
    The script prints the list of states retrieved from the specified database
    where the name matches the provided search argument.
"""

import MySQLdb as db
from sys import argv

if __name__ == '__main__':
    def filter_states_by_name(db_username, db_password, db_name, name_to_search):
        """
        Retrieves and lists states with names matching the provided argument
        from the specified database.

        Args:
            db_username (str): Username for database access.
            db_password (str): Password for database access.
            db_name (str): Name of the database to connect to.
            name_to_search (str): The name to search for in the states.

        Returns:
            None
        """
        db_connect = db.connect(
            host="localhost",
            port=3306,
            user=db_username,
            passwd=db_password,
            db=db_name
        )
        db_cursor = db_connect.cursor()

        db_cursor.execute(
            "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY \
            states.id ASC".format(name_to_search)
        )

        rows_selected = db_cursor.fetchall()

        for row in rows_selected:
            print(row)

    if len(argv) != 5:
        print("Usage: ./2-my_filter_states.py <db_username> "
              "<db_password> <db_name> <name_to_search>")
    else:
        filter_states_by_name(argv[1], argv[2], argv[3], argv[4])
