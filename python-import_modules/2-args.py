#!/usr/bin/python3
import sys

i = len(sys.argv)
if i == 0:
    print("{} arguments.".format(i))

else :
    print("{} arguments.".format(i))

    for j in i:
        print("{:d}: {}".format(j, argv[j]))
