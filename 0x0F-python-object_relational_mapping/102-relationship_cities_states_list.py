#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_101_usa.
Usage: ./102-relationship_cities_states_list.py <mysql username> /
                                                <mysql password> /
                                                <database name>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}",
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        state_name = city.state.name
        print(f"{city.id}: {city.name} -> {state_name}")

    session.close()
