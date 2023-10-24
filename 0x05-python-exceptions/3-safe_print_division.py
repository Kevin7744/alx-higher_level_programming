#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result =  a / b
    except (ZeroDivisionError, TypeError):
        result = None
    finally:
        if result is not None:
            print("Inside result: {}".format(result))
        else:
            print("Inside result: None")
    if result is not None:
        print("{:d} / {:d} = {}".format(a, b, result))
    else:
        print("{:d} / {:d} = {}".format(a, b, result))

