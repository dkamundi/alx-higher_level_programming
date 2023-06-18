#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

def list_cities_by_state(mysql_user, mysql_password, db_name, state_name):
    # Connect to MySQL database
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=mysql_user,
        passwd=mysql_password,
        db=db_name
    )

    # Create cursor to execute queries
    cursor = db.cursor()

    # Select all cities of the given state
    query = """
        SELECT cities.name FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    # Fetch all rows as a list of tuples and join city names with a comma separator
    cities = [row[0] for row in cursor.fetchall()]
    cities_str = ', '.join(cities)

    # Close cursor and database connections
    cursor.close()
    db.close()

    return cities_str

if __name__ == '__main__':
    # Script arguments
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Call the function to list cities by state
    result = list_cities_by_state(mysql_user, mysql_password, db_name, state_name)

    # Print the result
    print(result)

