#!/usr/bin/python3
"""
This script deletes all State objects
with a name containing the letter `a`
from the database `hbtn_0e_6_usa`.

Author: Alexander Udeogaranya

Usage:
./13-model_state_delete_a.py <db_username> <db_password> <db_name>

Arguments:
    <db_username> (str): Username for database access.
    <db_password> (str): Password for database access.
    <db_name> (str): Name of the database to connect to.

Example:
    ./13-model_state_delete_a.py root mypassword hbtn_0e_6_usa

Explanation:
    This script establishes a connection to the MySQL database using
    the provided credentials.
    It retrieves State objects with names containing the letter 'a'
    from the session, deletes
    them from the database, commits the changes, and closes the session.

Warning:
    Be cautious while deleting data from the database,
    as it can be irreversible.

"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    def delete_states_with_a(db_username, db_password, db_name):
        """
        Deletes State objects with names containing the letter 'a'
        from the database.

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
        if states is not None:
            for state in states:
                session.delete(state)

            session.commit()
            print("State objects with names containing 'a' deleted successfully.")
        else:
            print("No State objects with names containing 'a' found.")

        session.close()

    if len(argv) != 4:
        print("Usage: ./13-model_state_delete_a.py <db_username> "
              "<db_password> <db_name>")
    else:
        db_username, db_password, db_name = argv[1], argv[2], argv[3]
        delete_states_with_a(db_username, db_password, db_name)
