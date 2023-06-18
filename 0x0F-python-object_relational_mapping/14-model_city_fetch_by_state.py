#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == '__main__':
    # Script arguments
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine and session
    engine = create_engine(f'mysql+mysqldb://{mysql_user}:{mysql_password}@localhost:3306/{db_name}')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all City objects and join with State objects
    cities = session.query(City, State.name).join(State).order_by(City.id).all()
    
    # Print the cities with their associated states
    for city, state_name in cities:
        print(f'{state_name}: ({city.id}) {city.name}')

    # Close the session
    session.close()
