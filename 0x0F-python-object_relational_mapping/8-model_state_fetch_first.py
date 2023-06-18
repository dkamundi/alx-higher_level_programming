#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa
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

    # Query the first State object
    state = session.query(State).order_by(State.id).first()

    # Print the result or "Nothing" if no state found
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
