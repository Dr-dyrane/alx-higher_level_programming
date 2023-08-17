#!/usr/bin/python3
"""
Author: Alexander Udeogaranya

Description:
This script defines a City class to work with MySQLAlchemy ORM.
The City class represents a city entity in a database table.
It includes attributes for the city's ID, name, and the state it belongs to.

Usage:
This script is intended to be used as part of a larger application
where you need to interact with city data stored in a MySQL database.
You can import the City class to create, update,
and query city data using SQLAlchemy's ORM features.

Attributes:
    - __tablename__ (str): The table name of the City class.
    - id (int): The primary key ID of the city.
    - name (str): The name of the city.
    - state_id (int): The foreign key ID of the state the city belongs to.

Example:
    # Import required modules
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_city import City

    # Create a database connection
    db_uri = "mysql+mysqldb://username:password@localhost:3306/db_name"
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new city object
    new_city = City(name="New York", state_id=1)

    # Add the city object to the session
    session.add(new_city)

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()

Note:
- The City class is meant to be used in conjunction with a MySQL database.
- The script assumes that the required SQLAlchemy modules are installed.
- The database connection details (db_uri)
        should be updated to match your configuration.
"""

from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey

class City(Base):
    """
    City class representing a city entity in a database.

    Attributes:
        __tablename__ (str): The table name of the City class.
        id (int): The primary key ID of the city.
        name (str): The name of the city.
        state_id (int): The foreign key ID of the state the city belongs to.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
