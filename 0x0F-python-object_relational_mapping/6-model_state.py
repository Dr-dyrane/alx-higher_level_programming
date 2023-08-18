#!/usr/bin/python3
"""
This script defines a State class and a Base class to work with
MySQLAlchemy ORM. It creates a database engine and initializes
the database tables using the Base class.

Author: Alexander Udeogaranya

Usage:
    ./6-model_state.py <db_username> <db_password> <db_name>

Arguments:
    <db_username> (str): Username for database access.
    <db_password> (str): Password for database access.
    <db_name> (str): Name of the database to connect to.

Example:
    ./6-model_state.py root mypassword hbtn_0e_4_usa

Explanation:
    This script establishes a connection to the MySQL database
    using the provided credentials. It uses the SQLAlchemy library to create
    a database engine and initializes the database tables
    defined in the Base class.
    This is essential for defining the structure of the ORM objects.

Note:
    - Make sure to provide the correct database credentials and name.

Warning:
    - Be cautious while sharing sensitive database credentials.

"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    def create_database_tables(db_username, db_password, db_name):
        # Create a database engine using SQLAlchemy
        engine = create_engine(f'mysql+mysqldb://{db_username}:\
                            {db_password}@localhost/{db_name}',
                            pool_pre_ping=True)

        # Create the database tables defined in the Base class
        Base.metadata.create_all(engine)

        # Notify the user that the tables have been created
        print(f"Database tables have been created for '{db_name}' database.")


        if len(sys.argv) != 4:
            print("Usage: ./6-model_state.py <db_username> "
                "<db_password> <db_name>")
            sys.exit(1)

    # Extract database credentials from command-line arguments
    db_username = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]

    # Create database tables
    create_database_tables(db_username, db_password, db_name)
