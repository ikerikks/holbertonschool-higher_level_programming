#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    temp = my_list.copy()

    if idx in range(len(my_list)):
        temp[idx] = element
        return temp
