#!/usr/bin/python3
def uniq_add(my_list=[]):
    n_list = set(my_list)
    total = 0
    for i in n_list:
        total += i

    return (total)
