#!/usr/bin/python3
""" Filters states """

import sys

import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        charset="utf8",
        user=sys.argv[1],
        password=sys.argv[2],
        db=sys.argv[3],
        state=sys.argv[4]
    )

    cur = db.cursor()
    cur.execute("SELECT * from states WHERE name LIKE BINARY '{}'\ORDER BY id".format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
