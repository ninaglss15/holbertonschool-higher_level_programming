#!/usr/bin/python3
"""Adds the State object “Louisiana” to the database hbtn_0e_6_usa."""

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

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print(new_state.id)

    session.close()
