#!/usr/bin/python3
""" Filters states """

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
    cur.execute("SELECT * FROM states WHERE name[0] = 'N' ORDER BY id;")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
