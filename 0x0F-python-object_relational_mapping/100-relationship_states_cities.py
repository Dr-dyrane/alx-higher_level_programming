#!/usr/bin/python3
"""
This script adds a City object to a State object in
the database `hbtn_0e_14_usa`.

Usage:
    ./100-relationship_state_cities.py <db_username> <db_password> <db_name>

Arguments:
    <db_username> (str): Username for database access.
    <db_password> (str): Password for database access.
    <db_name> (str): Name of the database to connect to.

Example:
    ./100-relationship_state_cities.py root mypassword hbtn_0e_14_usa

Explanation:
    This script establishes a connection to the MySQL database using
    the provided credentials.
    It creates a new City object and associates it with a new State object.
    The State object is then added to the database along with the City object
    as part of a relationship. This demonstrates the use of one-to-many
    relationships in SQLAlchemy.

Note:
    - The State and City models are assumed to be defined in separate files named
    `relationship_state.py` and `relationship_city.py`.
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    def add_city_to_state(db_username, db_password, db_name):
        """
        Adds a City object to a State object in the database.

        Args:
            db_username (str): Username for database access.
            db_password (str): Password for database access.
            db_name (str): Name of the database to connect to.

        Returns:
            None
        """
        db_uri = f"mysql+mysqldb://{db_username}:\
        {db_password}@localhost:3306/{db_name}"
        engine = create_engine(db_uri)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)

        session = Session()
        
        cal_state = State(name='California')
        sfr_city = City(name='San Francisco')
        cal_state.cities.append(sfr_city)

        session.add(cal_state)
        session.commit()
        session.close()

    if len(argv) != 4:
        print("Usage: ./100-relationship_state_cities.py <db_username> "
              "<db_password> <db_name>")
    else:
        db_username, db_password, db_name = argv[1], argv[2], argv[3]
        add_city_to_state(db_username, db_password, db_name)
