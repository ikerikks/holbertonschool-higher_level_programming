#!/usr/bin/python3
import sys
if __name__ == '__main__':
    i = len(sys.argv)
    sum = 0

    for j in range(1, i):
        sum += int(sys.argv[j])

    print(sum)
