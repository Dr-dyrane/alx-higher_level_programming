#!/usr/bin/python3
"""
This script retrieves and displays a list of states from a specified database.
It establishes a connection to the database using the provided credentials and
fetches all rows from the 'states' table. The retrieved states are then printed
to the console.

Author: Alexander Udeogaranya
Usage:
    ./0-select_states.py <db_username> <db_password> <db_name>

Arguments:
    <db_username>: Username for database access.
    <db_password>: Password for database access.
    <db_name>: Name of the database to connect to.

Example:
    ./0-select_states.py root mypassword hbtn_0e_0_usa

Output:
    The script prints the list of states retrieved from the specified database.
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
    if len(argv) != 4:
        print("Usage: ./0-select_states.py <db_username> "
              "<db_password> <db_name>")
    else:
        list_states(argv[1], argv[2], argv[3])

