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
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id;")
    rows = cur.fetchall()
    for row in rows:
        if 'N' in row[1]:
            print(row)

    cur.close()
    db.close()
