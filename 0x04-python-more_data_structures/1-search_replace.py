#!/usr/bin/python3
def search_replace(my_list, search, replace):
    listCopy = []
    for i in range(len(my_list)):
        if i == search:
            listCopy.append(replace)
        else:
            listCopy.append(my_list[i])
    return listCopy 
