#!/usr/bin/python3
"""
Deletes all State objects with a name
containing the letter 'a' from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    dbname = argv[3]
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(user, passwd, dbname),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.like("%a%")).all()
    for state in states:
        session.delete(state)
    session.commit()
    session.close()
