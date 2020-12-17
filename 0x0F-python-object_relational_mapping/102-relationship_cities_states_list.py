#!/usr/bin/python3
"""creates the State “California” with the City “San Francisco”
from the database
Args:
    mysql username: name of the user
    mysql password: password for database
    database name: name of the database
"""
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker()
    session = Session(bind=engine)
    Base.metadata.create_all(engine)
    for city, state in session.query(City, State).filter(
            State.id == City.state_id).order_by(City.id).all():
        print("{:d}: {} -> {}".format(city.id, city.name, state.name))
    session.close()
