#!/usr/bin/python3
"""
This script retrieves and displays a list of states from a specified database.
It establishes a connection to the database using the provided credentials and
fetches all rows from the 'states' table. The retrieved states are then printed
to the console.
"""

import MySQLdb
from sys import argv

def list_states(db_username, db_password, db_name):
    """
    Retrieves and lists all states from the specified database.

    Args:
        db_username (str): Username for database access.
        db_password (str): Password for database access.
        db_name (str): Name of the database to connect to.

    Returns:
        None
    """
    db_connect = MySQLdb.connect(
        host="localhost",
        user=db_username,
        port=3306,
        passwd=db_password,
        db=db_name
    )

    db_cursor = db_connect.cursor()

    db_cursor.execute("SELECT * FROM states ORDER BY id")

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)

if __name__ == '__main__':
    db_username, db_password, db_name = argv[1:4]
    list_states(db_username, db_password, db_name)
