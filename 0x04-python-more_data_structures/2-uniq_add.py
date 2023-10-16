#!/usr/bin/python3
def uniq_add(my_list=[]):
    newCopy = set(my_list)
    result = 0
    for i in newCopy:
        result += i
    return result
