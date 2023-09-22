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
    for instance in session.query(State).order_by(State.id):
        print("{}: {}".format(instance.id, instance.name))
        for ct_instance in instance.cities:
            print("\t{}: {}".format(ct_instance.id, ct_instance.name))

    # Closing session model
    session.close()
