#!/usr/bin/python3
"""
This script retrieves and displays states based on a provided name filter
from the database `hbtn_0e_0_usa`. It uses parameter binding to prevent MySQL
injections and ensures safe interaction with the database.

Author: Alexander Udeogaranya

Usage:
./3-my_safe_filter_states.py <db_username> <db_password> <db_name> <state_name>

Arguments:
    <db_username> (str): Username for database access.
    <db_password> (str): Password for database access.
    <db_name> (str): Name of the database to connect to.
    <state_name> (str): The full state name or a partial name to filter.

Example:
    ./3-my_safe_filter_states.py root mypassword hbtn_0e_0_usa Texas

Output:
    The script fetches states from the specified database that match the
    provided state name filter and prints them to the console.

Explanation:
This script establishes a connection to the MySQL database using the provided
credentials. It then constructs a SQL query with a parameterized WHERE clause
to safely filter states based on the provided state name. The parameterized
approach prevents SQL injection attacks. The retrieved states are ordered by
their IDs in ascending order and printed to the console.

"""

import MySQLdb as db
from sys import argv

def filter_states_by_name(db_username, db_password, db_name, state_name):
    """
    Retrieves and lists states from the specified database
    that match the provided state name filter.

    Args:
        db_username (str): Username for database access.
        db_password (str): Password for database access.
        db_name (str): Name of the database to connect to.
        state_name (str): The state name or a partial name to filter.

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

    query = "SELECT * FROM states WHERE name LIKE BINARY %(name)s \
             ORDER BY states.id ASC"

    params = {'name': state_name}

    db_cursor.execute(query, params)

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)

if __name__ == "__main__":
    if len(argv) != 5:
        print("Usage: ./3-my_safe_filter_states.py <db_username> "
              "<db_password> <db_name> <state_name>")

    else:
        filter_states_by_name(argv[1], argv[2], argv[3], argv[4])
