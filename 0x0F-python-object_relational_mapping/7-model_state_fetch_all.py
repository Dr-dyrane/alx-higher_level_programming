#!/usr/bin/python3
"""
This script fetches and displays all State objects from the
database `hbtn_0e_6_usa`.

Author: Alexander Udeogaranya

Usage:
    ./7-model_state_fetch_all.py <db_username> <db_password> <db_name>

Arguments:
    <db_username> (str): Username for database access.
    <db_password> (str): Password for database access.
    <db_name> (str): Name of the database to connect to.

Example:
    ./7-model_state_fetch_all.py root mypassword hbtn_0e_6_usa

Explanation:
    This script establishes a connection to the MySQL database
    using the provided credentials.
    It uses the SQLAlchemy library to fetch all State objects
    from the database and prints their IDs and names to the console.

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
    def fetch_and_display_states(db_username, db_password, db_name):
        """
        Fetches and displays all State objects from the specified database.

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

        for instance in session.query(State).order_by(State.id):
            print(f"{instance.id}: {instance.name}")

    if len(argv) != 4:
        print("Usage: ./7-model_state_fetch_all.py <db_username> "
              "<db_password> <db_name>")
    else:
        fetch_and_display_states(argv[1], argv[2], argv[3])
