#!/usr/bin/python3
"""A script that lists all State objects that contain the letter `a`
   from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == '__main__':
    DATABASE_URL = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(DATABASE_URL.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Instance name Of State containing letter `a` ordered by state id
    a_instances = session.query(State).filter(
            State.name.like('%a%')).order_by(states.id)
    for instance in a_instances:
        print(instance.id, instance.name, sep=': ')

    session.close()
