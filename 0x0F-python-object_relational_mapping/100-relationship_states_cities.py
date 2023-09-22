#!/usr/bin/python3
"""A script to create the State “California” with the City "San Francisco"
   from the database hbtn_0e_100_usa
"""

from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == '__main__':
    # Creating and connecting session modal to local database
    DATABASE_URL = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(DATABASE_URL.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Creating new state called California
    new_state = State(name='California')
    session.add(new_state)

    # Creating new city called San Francisco in relation to California
    new_city = City(name='San Francisco', state_id=new_state.id)
    session.add(new_city)

    # Committing all changes to database
    session.commit()
    # Closing session model
    session.close()
