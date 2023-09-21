#!/usr/bin/python3
"""A script that print State object with name passed as argument
   from database hbtn_0e_6_usa.
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
import re


if __name__ == '__main__':
    DATABASE_URL = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(DATABASE_URL.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(State).order_by(State.id):
        escaped_name = re.escape(instance.name)
        matched = re.match(escaped_name, argv[4])

    if matched is not None:
        print(matched.id)
    else:
        print("Not found")
