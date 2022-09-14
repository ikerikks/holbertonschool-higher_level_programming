#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    a = [0, 0]
    b = [0, 0]
    for idx, i in enumerate(tuple_a):
        if (idx < 2):
            a[idx] = tuple_a[idx]
    for idx, i in enumerate(tuple_b):
        if (idx < 2):
            b[idx] = tuple_b[idx]
    var_a = a[0] + b[0]
    var_b = a[1] + b[1]
    return (var_a, var_b)
