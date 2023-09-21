#!/usr/bin/python3
"""A script to delete all State objects with a name containing
   the letter `a` from the database hbtn_0e_6_usa.
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == '__main__':
    # Creating and connecting session to local database
    DATABASE_URL = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(DATABASE_URL.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Trying to delete State names with alphabert 'a'
    try:
        delState = session.query(State).filter(State.name.like('%a%')).all()
        for state in delState:
            session.delete(state)

        # Commiting all changes to databases
        session.commit()

    except Exception:
        pass

    finally:
        # Closing the session model
        session.close()
