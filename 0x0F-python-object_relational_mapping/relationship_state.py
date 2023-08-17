#!/usr/bin/python3
"""
This script defines a State class and
a Base class to work with MySQLAlchemy ORM.

Author: Your Name

Description:
    This script defines a State class that corresponds
    to a table in a MySQL database. The State class represents a state entity
    and includes attributes for the state's ID and name.
    The script also defines the Base class,
    which is a part of the SQLAlchemy's declarative system.

Attributes:
    - __tablename__ (str): The table name of the State class.
    - id (int): The primary key ID of the state.
    - name (str): The name of the state.
    - cities (:obj:`City`): A relationship to the City class,
    indicating the cities that belong to this state.

Note:
    - This script is intended to be used with SQLAlchemy's
                Object-Relational Mapping (ORM) framework.
    - The State class is meant to be used in conjunction with a MySQL database.
    - The script assumes that the required SQLAlchemy modules are installed.
    - The database connection details
                (e.g., username, password, database name) should be updated
      to match your MySQL configuration.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Declare the base class for declarative class definitions
Base = declarative_base()

class State(Base):
    """State class representing a state entity in a database table.

    Attributes:
        __tablename__ (str): The table name of the class.
        id (int): The primary key ID of the state.
        name (str): The name of the state.
        cities (:obj:`City`): A relationship to the City class
        indicating the cities that belong to this state.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
