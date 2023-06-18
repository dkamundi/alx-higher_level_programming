#!/usr/bin/python3
"""
This module defines a script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument, using
parameterized queries to prevent SQL injection.
"""

import MySQLdb
import sys


def safe_select_states(username, password, db_name, state_name):
    """
    This function takes in four arguments and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument, using parameterized
    queries to prevent SQL injection.
    """
    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8"
    )

    # Get a cursor
    cursor = db.cursor()

    # Define the query with a parameter placeholder
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"

    # Execute the query with the parameter value
    cursor.execute(query, (state_name,))

    # Fetch all the rows as a list of tuples
    rows = cursor.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Close cursor and database
    cursor.close()
    db.close()


if __name__ == "__main__":
    # Call the safe_select_states() function with the provided arguments
    safe_select_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
