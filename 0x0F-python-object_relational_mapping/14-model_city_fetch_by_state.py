#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
"""

from sys import argv
from model_city import Base, City
from model_state import State
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
    cities = session.query(City, State).filter(City.state_id == State.id).all()
    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
