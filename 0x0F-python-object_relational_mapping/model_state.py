#!/usr/bin/python3
"""
Author: Alexander Udeogaranya

Description:
This script defines a State class and a Base class to work with
the MySQLAlchemy ORM.
The State class represents a state entity in a database table.
It includes attributes for the state's ID and name.

Usage:
This script is intended to be used as part of a larger application
where you need to interact with state data stored in a MySQL database.
You can import the State class to create, update,
and query state data using SQLAlchemy's ORM features.

Attributes:
    - __tablename__ (str): The table name of the State class.
    - id (int): The primary key ID of the state.
    - name (str): The name of the state.

Example:
    # Import required modules
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State

    # Create a database connection
    db_uri = "mysql+mysqldb://username:password@localhost:3306/db_name"
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new state object
    new_state = State(name="California")

    # Add the state object to the session
    session.add(new_state)

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()

Note:
- The State class is meant to be used in conjunction with a MySQL database.
- The script assumes that the required SQLAlchemy modules are installed.
- The database connection details (db_uri)
        should be updated to match your configuration.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    State class representing a state entity in a database.

    Attributes:
        __tablename__ (str): The table name of the State class.
        id (int): The primary key ID of the state.
        name (str): The name of the state.
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
