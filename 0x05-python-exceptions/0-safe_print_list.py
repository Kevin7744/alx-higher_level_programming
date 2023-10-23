#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    my_list = []
    try:
        print(my_list[x:])
    except ValueError as error:
        print("Please enter a valid number")

