#!/usr/bin/python3
"""
This script prints the first State object from the database `hbtn_0e_6_usa`.

Author: Alexander Udeogaranya

Usage:
    ./8-model_state_first_fetch.py <db_username> <db_password> <db_name>

Arguments:
    <db_username> (str): Username for database access.
    <db_password> (str): Password for database access.
    <db_name> (str): Name of the database to connect to.

Example:
    ./8-model_state_first_fetch.py root mypassword hbtn_0e_6_usa

Explanation:
    This script establishes a connection to the MySQL database
    using the provided credentials. It uses the SQLAlchemy library to fetch
    the first State object from the database and prints its ID and
    name to the console.

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
    def fetch_and_display_first_state(db_username, db_password, db_name):
        """
        Fetches and displays the first State object from : specified database.

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

        state = session.query(State).order_by(State.id).first()
        if state is not None:
            print(f"{state.id}: {state.name}")
        else:
            print("Nothing")

    if len(argv) != 4:
        print("Usage: ./8-model_state_first_fetch.py <db_username> "
              "<db_password> <db_name>")
    else:
        fetch_and_display_first_state(argv[1], argv[2], argv[3])
