#!/usr/bin/python3
"""
This script lists all City objects and their corresponding State objects
from the database `hbtn_0e_101_usa`.

Usage:
    ./102-relationship_cities_state_lists.py <db_username>
    <db_password> <db_name>

Arguments:
    <db_username> (str): Username for database access.
    <db_password> (str): Password for database access.
    <db_name> (str): Name of the database to connect to.

Example:
    ./102-relationship_cities_state_lists.py root mypassword hbtn_0e_101_usa

Explanation:
    This script establishes a connection to the MySQL database using
    the provided credentials.
    It queries the database to retrieve all City objects & their corresponding
    State objects using a one-to-many relationship.
    The results are printed to the console, displaying the ID,
    name of the City, and the name of the associated State.

Note:
    - The State & City models are assumed to be defined in separate files named
    `relationship_state.py` and `relationship_city.py`.
"""

import sys
from relationship_state import State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def list_cities_with_states(db_username, db_password, db_name):
    """
    Lists all City objects & their corresponding State objects
    from the database.

    Args:
        db_username (str): Username for database access.
        db_password (str): Password for database access.
        db_name (str): Name of the database to connect to.

    Returns:
        None
    """
    db_uri = f"mysql+mysqldb://{db_username}:\
    {db_password}@localhost:3306/{db_name}"
    engine = create_engine(db_uri, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).join(City).order_by(City.id).all()

    for state in states:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./102-relationship_cities_state_lists.py <db_username> "
              "<db_password> <db_name>")
    else:
        db_username, db_password, db_name = sys.argv[1:4]
        list_cities_with_states(db_username, db_password, db_name)
