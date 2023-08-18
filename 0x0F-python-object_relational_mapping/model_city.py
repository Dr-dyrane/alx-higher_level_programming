#!/usr/bin/python3
"""
Author: Alexander Udeogaranya

Description:
This script defines a City class that corresponds to a table
in a MySQL database and works with SQLAlchemy's
Object-Relational Mapping (ORM) framework.
The class has attributes for the city's ID,
the ID of the state it belongs to,
and the name of the city. This class is used to represent
and manipulate city data
within the database.
"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
    City class representing a city entity in a database.

    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The id of the class
        name (str): The name of the class
        state_id (int): The state the city belongs to
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
