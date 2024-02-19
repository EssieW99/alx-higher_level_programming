#!/usr/bin/python3
"""
a script that prints the first State object from
the database hbtn_0e_6_usa
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

    """print first State object"""
    instance = session.query(State).order_by(State.id).first()
    if instance is None:
        print("Nothing")
    else:
        print("{}: {}".format(instance.id, instance.name))
