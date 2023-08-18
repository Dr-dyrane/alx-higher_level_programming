#!/usr/bin/python3
"""
Author: Alexander Udeogaranya

Description:
This script defines a State class and a Base class to work with
the MySQLAlchemy ORM.
The State class represents a state entity in a database table.
It includes attributes for the state's ID and name.
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
