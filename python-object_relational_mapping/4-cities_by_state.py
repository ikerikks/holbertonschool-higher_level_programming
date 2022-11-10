#!/usr/bin/python3
""" Cities by state """

import sys

import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        db=sys.argv[3],
    )

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
        FROM cites JOIN states ON states_id = states.id ORDER BY states.id;")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
