#!/usr/bin/python3
'''
Print all City object from the database hbtn_0e_14_usa
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sys import argv


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    s_city = session.query(State, City).filter(State.id == City.state_id).all()

    for state, city in s_city:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
