#!/usr/bin/python3
"""
This script retrieves and prints the ID of the first State object
with a specified name from the database `hbtn_0e_6_usa`.

Author: Alexander Udeogaranya

Usage:
    ./10-model_state_my_get.py <db_username>
    <db_password> <db_name> <state_name>

Arguments:
    <db_username> (str): Username for database access.
    <db_password> (str): Password for database access.
    <db_name> (str): Name of the database to connect to.
    <state_name> (str): Name of the state to search for.

Example:
    ./10-model_state_my_get.py root mypassword hbtn_0e_6_usa California

Explanation:
    This script establishes a connection to the MySQL database using
    the provided credentials. It uses the SQLAlchemy library to retrieve the
    ID of the first State object with the specified name and
    prints it to the console.

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
    def get_state_id_by_name(db_username, db_password, db_name, state_name):
        """
        Retrieves and prints the ID of the first State object with the specified
        name from the database.

        Args:
            db_username (str): Username for database access.
            db_password (str): Password for database access.
            db_name (str): Name of the database to connect to.
            state_name (str): Name of the state to search for.

        Returns:
            None
        """
        db_url = f"mysql+mysqldb://{db_username}:\
        {db_password}@localhost:3306/{db_name}"

        engine = create_engine(db_url)
        Session = sessionmaker(bind=engine)
        session = Session()

        state = session.query(State).filter(State.name == state_name).first()
        if state:
            print(state.id)
        else:
            print("Not found")

    if len(argv) != 5:
        print("Usage: ./10-model_state_my_get.py <db_username> "
              "<db_password> <db_name> <state_name>")
    else:
        get_state_id_by_name(argv[1], argv[2], argv[3], argv[4])
