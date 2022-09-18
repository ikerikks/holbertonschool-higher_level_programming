#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    order = sorted(a_dictionary)
    for i in order:
        print("{}: {}".format(i, a_dictionary[i]))
