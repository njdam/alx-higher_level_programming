#!/usr/bin/python3
"""A script that print State object with name passed as argument
   from database hbtn_0e_6_usa.
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv, exit


if __name__ == '__main__':
    """A script must receive 4 parameters to find state id"""
    if len(argv) != 5:
        print(f'Usage: {argv[0]} <user> <passwd> <database> <state_name>')
        exit(1)

    DATABASE_URL = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(DATABASE_URL.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_name = argv[4]
    found = session.query(State).filter(State.name == state_name).first()

    if found is not None:
        print(found.id)
    else:
        print("Not found")
