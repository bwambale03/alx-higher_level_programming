#!/usr/bin/python3
"""
Lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa.
Usage: ./101-relationship_states_cities_list.py <mysql username> /
                                                <mysql password> /
                                                <database name>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City

def main():
    if len(sys.argv) != 4:
        print("Usage: ./101-relationship_states_cities_list.py <mysql username> "
              "<mysql password> <database name>")
        return

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}",
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")
        cities = state.cities
        for city in cities:
            print(f"    {city.id}: {city.name}")

    session.close()

if __name__ == "__main__":
    main()
