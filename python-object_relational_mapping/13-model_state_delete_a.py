#!/usr/bin/python3
"""Deletes all State objects with a name containing the letter 'a' from hbtn_0e_6_usa."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    dbname = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(user, pwd, dbname),
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)
    session = Session(engine)

    states_to_delete = session.query(State).filter(State.name.like("%a%")).all()
    for state in states_to_delete:
        session.delete(state)
    session.commit()

    session.close()
