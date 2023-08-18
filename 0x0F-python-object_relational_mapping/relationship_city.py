#!/usr/bin/python3
"""
Author: Alexander Udeogaranya

Description:
This script defines a City class to work with MySQLAlchemy ORM.
The City class represents a city entity in a database table.
It includes attributes for the city's ID, name, and the state it belongs to.
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
