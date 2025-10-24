#!/usr/bin/python3
"""Lists all State objects that contain the letter 'a' from hbtn_0e_6_usa."""

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

    states = session.query(State).filter(State.name.like("%a%")).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
