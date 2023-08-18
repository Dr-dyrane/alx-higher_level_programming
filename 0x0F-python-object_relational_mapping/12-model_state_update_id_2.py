#!/usr/bin/python3
"""
This script updates the name of a specific State object
in the database `hbtn_0e_6_usa`.

Author: Alexander Udeogaranya

Usage:
./12-model_state_update_id_2.py <db_username> <db_password> <db_name>

Arguments:
    <db_username> (str): Username for database access.
    <db_password> (str): Password for database access.
    <db_name> (str): Name of the database to connect to.

Example:
    ./12-model_state_update_id_2.py root mypassword hbtn_0e_6_usa

Explanation:
    This script establishes a connection to the MySQL database using
    the provided credentials. It retrieves the State object with ID 2
    from the session, updates its name to 'New Mexico',
    commits the changes to the database, and closes the session.

Warning:
    Be cautious while updating data in the database, as it can affect
    the integrity of the data.

"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def update_state_name(db_username, db_password, db_name):
    """
    Updates the name of a specific State object in the database.

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

    state = session.query(State).filter(State.id == 2).first()
    if state is not None:
        state.name = "New Mexico"
        session.commit()
        print("State name updated successfully.")
    else:
        print("State with ID 2 not found.")

    session.close()

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./12-model_state_update_id_2.py <db_username> "
              "<db_password> <db_name>")
    else:
        db_username, db_password, db_name = argv[1], argv[2], argv[3]
        update_state_name(db_username, db_password, db_name)
