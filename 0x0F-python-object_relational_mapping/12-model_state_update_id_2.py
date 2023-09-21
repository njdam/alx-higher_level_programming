#!/usr/bin/python3
"""A script to change the name of a State object from database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == '__main__':
    # Creating and connection session model to local database
    DATABASE_URL = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(DATABASE_URL.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Filter out the first Occurence of State name at id = 2
    update_state = session.query(State).filter_by(id=2).first()

    if update_state:
        # Updating State name at state id = 2
        update_state.name = "New Mexico"
        # To commit all changes to database
        session.commit()

    # Close session model
    session.close()
