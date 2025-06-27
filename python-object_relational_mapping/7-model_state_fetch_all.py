#!/usr/bin/python3
"""
This module lists all State objects from the database.
"""

import sys
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == "__main__":

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
        )
    )

    session = Session(engine)
    for instance in session.query(State).order_by(State.id).all():
        print("{}: {}".format(instance.id, instance.name))
