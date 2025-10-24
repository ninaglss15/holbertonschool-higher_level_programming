#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City


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

    cities = session.query(City).join(State).order_by(City.id).all()
    for city in cities:
        print(f"{city.state.name}: ({city.id}) {city.name}")

    session.close()
