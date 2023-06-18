#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the letter 'a'
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

    # Query and delete all State objects with a name containing 'a'
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()
    for state in states_to_delete:
        session.delete(state)

    # Commit the session to persist the changes in the database
    session.commit()

    # Close the session
    session.close()
