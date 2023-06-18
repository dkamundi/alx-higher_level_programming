#!/usr/bin/python3
"""
Script that lists all State objects containing the letter 'a'
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    # Script arguments
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Database connection
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(mysql_user, mysql_password, db_name),
        pool_pre_ping=True
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query State objects containing the letter 'a'
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id)

    # Print the results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close he session
    session.close()
