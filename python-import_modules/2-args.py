#!/usr/bin/python3
import sys
if __name__ == '__main__':
    i = len(sys.argv)
    if i < 2:
        print("0 arguments.".format(i))

    else:
        if (i - 1) < 2:
            print("{} argument:".format(i - 1))

        else:
            print("{} arguments:".format(i - 1))

        for j in range(1, i):
            print("{:d}: {}".format(j, sys.argv[j]))
