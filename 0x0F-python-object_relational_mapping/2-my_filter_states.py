#!/usr/bin/python3
import sys
import MySQLdb

# Get command-line arguments
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
state_name = sys.argv[4]

# Connect to the MySQL server
db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

# Create a cursor object to interact with the database
cursor = db.cursor()

# Create the SQL query with the user input
sql_query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)

# Execute the SQL query
cursor.execute(sql_query)

# Fetch all the rows from the result set
rows = cursor.fetchall()

# Print the states
for row in rows:
    print(row)

# Close the cursor and database connection
cursor.close()
db.close()

