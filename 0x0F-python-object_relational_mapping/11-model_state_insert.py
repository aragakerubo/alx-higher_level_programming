#!/usr/bin/python3
"""
Adds the State object “Louisiana” to the database hbtn_0e_6_usa
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
    louisiana = State(name="Louisiana")
    session.add(louisiana)
    session.commit()
    print("{}".format(louisiana.id))
    session.close()
