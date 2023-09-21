#!/usr/bin/python3
"""A script to add State object “Louisiana” to the database hbtn_0e_6_usa"""

from model_state import Base, State
from SQLAlchemy import create_engine
from SQLAlchemy.orm import sessionmaker
from sys import argv


if __name__ == '__main__':
    # Craeting and Connecting session model (tables) to the local database
    DATABASE_URL = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(DATABASE_URL.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Creation of new state object
    new_state = State(name="Louisiana")
    # Adding new state to the section
    session.add(new_state)
    # Committing transaction or changes to the database
    session.commit()

    # Printing the new added state's id
    print(new_state.id)

    # Closing the session model
    session.close()
