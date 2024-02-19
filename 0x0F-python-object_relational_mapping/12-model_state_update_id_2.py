#!/usr/bin/python3
"""
a script that changes the name of a State object from the database
"""
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    """ create engine"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    """ create a session"""
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = session.query(State).filter(State.id == '2').first()
    new_state.name = 'New Mexico'
    session.commit()
