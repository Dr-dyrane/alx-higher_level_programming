#!/usr/bin/python3
"""
This script lists all State objects that contain the letter 'a'
from the database `hbtn_0e_6_usa`.

Author: Alexander Udeogaranya

Usage:
    ./9-model_state_filter_a.py <db_username> <db_password> <db_name>

Arguments:
    <db_username> (str): Username for database access.
    <db_password> (str): Password for database access.
    <db_name> (str): Name of the database to connect to.

Example:
    ./9-model_state_filter_a.py root mypassword hbtn_0e_6_usa

Explanation:
    This script establishes a connection to the MySQL database
    using the provided credentials.
    It uses the SQLAlchemy library to filter State objects whose names contain
    the letter 'a' and prints their IDs and names to the console.

Note:
    - Make sure to provide the correct database credentials and name.

Warning:
    - Be cautious while sharing sensitive database credentials.
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    def filter_states_with_a(db_username, db_password, db_name):
        """
        Filters and displays State objects whose names contain the letter 'a'
        from the specified database.

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

        states = session.query(State).filter(State.name.contains('a'))
        if states:
            for state in states:
                print(f"{state.id}: {state.name}")

    if len(argv) != 4:
        print("Usage: ./9-model_state_filter_a.py <db_username> "
              "<db_password> <db_name>")
    else:
        filter_states_with_a(argv[1], argv[2], argv[3])
