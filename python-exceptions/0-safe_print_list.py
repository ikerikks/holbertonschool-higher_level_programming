#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    length = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
        except:
            break
        length += 1
    print("")
    return length
