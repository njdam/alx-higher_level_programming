#!/usr/bin/python3
"""A script to list all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa.
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

    # Printing State and their related cities
    for st_instance in (
            session.query(State.id, State.name).order_by(State.id)
            ):
        print("{}: {}".format(st_instance[0], st_instance[1]))
        for ct_instance in (
                session.query(City.id, City.name)
                .filter(st_instance[0] == City.state_id).order_by(City.id)
                ):
            print("\t{}: {}".format(ct_instance[0], ct_instance[1]))

    # Closing session model
    session.close()
