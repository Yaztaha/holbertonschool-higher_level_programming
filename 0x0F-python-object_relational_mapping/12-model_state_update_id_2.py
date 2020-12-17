#!/usr/bin/python3
"""Changes the name of a 'State' object"""

from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format
                           (argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter_by(id="2").first()
    state.name = "New Mexico"
    session.commit()
