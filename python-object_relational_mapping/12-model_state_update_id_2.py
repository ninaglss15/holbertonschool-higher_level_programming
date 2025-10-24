#!/usr/bin/python3
"""Changes the name of a State object in the database hbtn_0e_6_usa."""

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

    state = session.query(State).get(2)
    if state:
        state.name = "New Mexico"
        session.commit()

    session.close()
