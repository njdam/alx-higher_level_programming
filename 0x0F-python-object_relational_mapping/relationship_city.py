#!/usr/bin/python3
"""A Python file similar to model_state.py named model_city.py that
   contains the class definition of a City.
"""

from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """A City class that inherited from class Base"""
    __tablename__ = 'cities'

    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
