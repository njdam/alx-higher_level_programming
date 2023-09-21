#!/usr/bin/python3
"""A script that lists all State objects from the database hbtn_0e_6_usa."""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ = '__main__':
    DATABASE_URL = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(DATABASE_URL.format(argv[1], argv[2], argv[3]))
    # Make connection to Local Databases
    Base.metadata.create_all(engine)
    # Connection bridge bettween inputs and storage engine
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).order_by(State.id):
        print(instance.id, instance.name, sep=": ")
