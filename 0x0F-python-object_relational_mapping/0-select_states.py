#!/usr/bin/python3.10
""" a script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys

"""
Connect to a MySQL database
Get a cursor object
Execute
Fetch all the rows
Print
Close cursor and connection
"""

if __name__ == "__main__":
    print("Connecting to MySQL database...")
    print("Host:", "localhost")
    print("User:", sys.argv[1])
    print("Password:", sys.argv[2])
    print("Database:", sys.argv[3])

    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    states = cur.fetchall()
    for row in states:
        print(row)
    cur.close()
    db.close()
