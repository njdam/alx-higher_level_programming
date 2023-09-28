#!/usr/bin/python3
"""A script to list all City objects from the database hbtn_0e_101_usa
   In format: <city id>: <city name> -> <state name>
"""

from relationship_city import City
from relationship_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == '__main__':
    # Creation and connection session model to local database
    DATABASE_URL = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(DATABASE_URL.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Printing City id, City name and their related State name
    for instance in (
            session.query(City.id, City.name, State.name)
            .filter(State.id == City.state_id).order_by(City.id)
            ):
        print("{}: {} -> {}".format(instance[0], instance[1], instance[2]))

    # Closing session model
    session.close()
