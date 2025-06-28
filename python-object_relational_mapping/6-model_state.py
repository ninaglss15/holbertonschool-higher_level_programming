#!/usr/bin/python3
"""Script that creates the states table in the database using SQLAlchemy"""

import sys

from model_state import Base, State

from sqlalchemy import create_engine

if __name__ == "__main__":

    db_url = "mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]
    )

    engine = create_engine(db_url, pool_pre_ping=True)

    Base.metadata.create_all(engine)
