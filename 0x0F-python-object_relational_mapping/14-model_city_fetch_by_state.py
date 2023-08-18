#!/usr/bin/python3
"""
This script prints all City objects from the database `hbtn_0e_14_usa`.

Author: Alexander Udeogaranya

Usage:
./14-model_city_fetch_all.py <db_username> <db_password> <db_name>

Arguments:
    <db_username> (str): Username for database access.
    <db_password> (str): Password for database access.
    <db_name> (str): Name of the database to connect to.

Example:
./14-model_city_fetch_all.py root mypassword hbtn_0e_14_usa

Explanation:
    This script establishes a connection to the MySQL database
    using the provided credentials.
    It retrieves City objects along with their corresponding
    State objects from the database.
    The retrieved data is then printed in 
    the format: "State: (City ID) City Name".

Note:
    - The State and City models are assumed to be defined in separate files
    named `model_state.py` and `model_city.py`.

"""

from sys import argv
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    def fetch_and_print_cities(db_username, db_password, db_name):
        """
        Retrieves and prints all City objects along with their 
        corresponding State objects.

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

        results = session.query(City, State).join(State)

        for city, state in results.all():
            print("{}: ({}) {}".format(state.name, city.id, city.name))

        session.close()

    if len(argv) != 4:
        print("Usage: ./14-model_city_fetch_all.py <db_username> "
              "<db_password> <db_name>")
    else:
        db_username, db_password, db_name = argv[1], argv[2], argv[3]
        fetch_and_print_cities(db_username, db_password, db_name)
