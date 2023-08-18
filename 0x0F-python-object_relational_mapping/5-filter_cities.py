#!/usr/bin/python3
"""
This script takes the name of a state as an argument
and lists all cities of that state
from the database `hbtn_0e_4_usa`.

Author: Alexander Udeogaranya

Usage:
    ./5-filter_cities.py <db_username> <db_password> <db_name> <state_name>

Arguments:
    <db_username> (str): Username for database access.
    <db_password> (str): Password for database access.
    <db_name> (str): Name of the database to connect to.
    <state_name> (str): The name of the state to filter cities by.

Example:
    ./5-filter_cities.py root mypassword hbtn_0e_4_usa Texas

Output:
    The script fetches and lists the cities of the specified state
    from the database.

Explanation:
    This script establishes a connection to the MySQL database using
    the provided credentials. It constructs an SQL query that joins
    the 'cities' and 'states' tables based on the 'state_id' relationship.
    The query selects cities that belong to the specified state using the
    'state_name' argument.
    The retrieved cities are then ordered by their IDs in ascending order
    and listed, separated by commas, in the console.

"""

import MySQLdb as db
from sys import argv

if __name__ == "__main__":
    def list_cities_by_state(db_username, db_password, db_name, state_name):
        """
        Retrieves and lists cities of the specified state from the database.

        Args:
            db_username (str): Username for database access.
            db_password (str): Password for database access.
            db_name (str): Name of the database to connect to.
            state_name (str): The name of the state to filter cities by.

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
            db_cursor.execute("""
                SELECT
                    cities.id, cities.name
                FROM
                    cities
                JOIN
                    states
                ON
                    cities.state_id = states.id
                WHERE
                    states.name LIKE BINARY %(state_name)s
                ORDER BY
                    cities.id ASC
            """, {
                'state_name': state_name
            })
            rows_selected = db_cursor.fetchall()

        if rows_selected is not None:
            print(", ".join([row[1] for row in rows_selected]))

    list_cities_by_state(argv[1], argv[2], argv[3], argv[4])
