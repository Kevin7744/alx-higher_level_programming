#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    ret = 0
    for item in my_list:
	if isinstance(item, int)
        	try:
            		print("{}".format(item), end="")
            		ret += 1
        	except (ValueError, TypeError):
            		continue
    print()
    return ret
