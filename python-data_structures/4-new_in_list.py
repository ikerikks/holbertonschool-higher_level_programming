#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    temp = my_list.copy()

    if idx < 0 or idx >= len(my_list):
        pass
    else:
        temp[idx] = element

    return temp
