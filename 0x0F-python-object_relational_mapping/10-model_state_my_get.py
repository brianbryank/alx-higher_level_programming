#!/usr/bin/python3
"""lists all State objects that contain the letter a"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    qu = sys.argv[4]
    sql = session().query(State).filter(State.name.like(qu)).all()
    if sql:
        print("{}".format(sql[0].id))
    else:
        print("Not found")
    session().close()
