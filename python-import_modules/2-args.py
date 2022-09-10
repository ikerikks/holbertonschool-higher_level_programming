#!/usr/bin/python3
import sys
if __name__ == '__main__'
    i = len(sys.argv)
    if i < 2:
        print("{} arguments.".format(i))

    else :
        print("{} arguments:".format(i))

        for j in range(1, i):
            print("{:d}: {}".format(j, argv[j]))
