#!/usr/bin/python3
"""A python file that contains the class definition of a State and
   an instance Base = declarative_base().
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData, Column, Integer, String

Base = declarative_base(metadata=MetaData())


class State(Base):
    """State class which inherits from class Base with id and name
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
