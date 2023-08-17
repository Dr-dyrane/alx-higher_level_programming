#!/usr/bin/python3
"""
This script interacts with a MySQL database to retrieve and display
states whose names start with the letter 'N'. It establishes a connection
to the 'hbtn_0e_0_usa' database using the provided credentials and fetches
all rows from the 'states' table where the 'name' column starts with 'N'.
The retrieved states are then printed to the console.

Author: Alexander Udeogaranya

Usage:
    ./1-filter_states.py <db_username> <db_password> <db_name>

Arguments:
    <db_username>: Username for database access.
    <db_password>: Password for database access.
    <db_name>: Name of the database to connect to.

Example:
    ./1-filter_states.py root mypassword hbtn_0e_0_usa

Output:
    The script prints the list of states retrieved from the specified database
    with names starting with the letter 'N'.
"""

import MySQLdb as db
from sys import argv

def list_states_with_N(db_username, db_password, db_name):
    """
    Retrieves and lists states with names starting with 'N'
    from the specified database.

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
    db_cursor = db_connect.cursor()

    db_cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' \
         ORDER BY states.id ASC"
    )

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)

if __name__ == '__main__':
    if len(argv) != 4:
        print("Usage: ./1-filter_states.py <db_username> "
              "<db_password> <db_name>")
    else:
        list_states_with_N(argv[1], argv[2], argv[3])
