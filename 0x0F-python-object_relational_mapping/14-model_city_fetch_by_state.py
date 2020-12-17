#!/usr/bin/python3
"""Adds a new city object to the database"""

from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from model_city import City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format
                           (argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    for city, state in session.query(
            City, State).filter(
            City.state_id == State.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
