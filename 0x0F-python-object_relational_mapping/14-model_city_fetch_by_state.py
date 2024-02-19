#!/usr/bin/python3
"""
script that prints all City objects from the database
"""
from model_state import Base, State
from model_city import City
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

    query = session.query(City, State).join(State)
    for c, s in query.all():
        print("{}: ({}) {}".format(s.name, c.id, c.name))

    session.commit()
