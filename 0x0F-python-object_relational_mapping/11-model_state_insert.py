#!/usr/bin/python3
"""
This script adds a new State object named 'Louisiana' to
the database 'hbtn_0e_6_usa'.

Author: Alexander Udeogaranya

Usage:
./11-model_state_insert.py <db_username> <db_password> <db_name>

Arguments:
    <db_username> (str): Username for database access.
    <db_password> (str): Password for database access.
    <db_name> (str): Name of the database to connect to.

Example:
    ./11-model_state_insert.py root mypassword hbtn_0e_6_usa

Explanation:
    This script establishes a connection to the MySQL database
    using the provided credentials. It then creates a new State object
    with the name 'Louisiana', adds it to the session, commits the changes
    to the database, and prints the ID of the newly added State object.
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def add_state(db_username, db_password, db_name):
    """
    Adds a new State object named 'Louisiana' to the specified database.

    Args:
        db_username (str): Username for database access.
        db_password (str): Password for database access.
        db_name (str): Name of the database to connect to.

    Returns:
        None
    """
    db_url = f"mysql+mysqldb://{db_username}:\
    {db_password}@localhost:3306/{db_name}"
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    print(new_state.id)
    session.close()

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./11-model_state_insert.py <db_username> "
              "<db_password> <db_name>")
    else:
        db_username, db_password, db_name = argv[1], argv[2], argv[3]
        add_state(db_username, db_password, db_name)
