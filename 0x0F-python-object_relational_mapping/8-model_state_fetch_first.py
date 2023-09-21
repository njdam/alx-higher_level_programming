#!/usr/bin/python3
"""A script to print the first State object from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import argv


if __name__ == '__main__':
    DATABASE_URL = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(DATABASE_URL.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session() = sessionmaker(bind=engine)
    session = Session()

    instance = session.query(State).first()
    if instance is not None:
        print(instance.id, instance.name, sep=": ")
    else:
        print("Nothing")
