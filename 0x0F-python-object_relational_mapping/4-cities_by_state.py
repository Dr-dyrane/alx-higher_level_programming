#!/usr/bin/python3
"""
This script retrieves and displays a list of cities along with
their corresponding state from the database `hbtn_0e_4_usa`.

Author: Alexander Udeogaranya

Usage:
    ./4-cities_by_state.py <db_username> <db_password> <db_name>

Arguments:
    <db_username>: Username for database access.
    <db_password>: Password for database access.
    <db_name>: Name of the database to connect to.

Example:
    ./4-cities_by_state.py root mypassword hbtn_0e_4_usa

Output:
    The script fetches a list of cities along with their corresponding states
    from the database and prints them to the console.

Explanation:
    This script establishes a connection to the MySQL database using
    the provided credentials. It constructs an SQL query that joins
    the 'cities' and 'states' tables based on the 'state_id' relationship.
    The resulting data includes city IDs, city names,
    and corresponding state names. The retrieved information is then
    ordered by city IDs in ascending order and printed to the console.
"""

import MySQLdb as db
from sys import argv

if __name__ == '__main__':
    def list_cities_and_states(db_username, db_password, db_name):
        """
        Retrieves and lists all cities along with their
        corresponding states from the specified database.

        Args:
            db_username (str): Username for database access.
            db_password (str): Password for database access.
            db_name (str): Name of the database to connect to.

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

        with db_connect.cursor() as db_cursor:
            query = "SELECT cities.id, cities.name, states.name \
                    FROM cities JOIN states ON cities.state_id = states.id \
                    ORDER BY cities.id ASC"
            db_cursor.execute(query)
            rows_selected = db_cursor.fetchall()

        if rows_selected is not None:
            for row in rows_selected:
                print(row)

    if len(argv) != 4:
        print("Usage: ./4-cities_by_state.py <db_username> "
              "<db_password> <db_name>")
    else:
        list_cities_and_states(argv[1], argv[2], argv[3])
