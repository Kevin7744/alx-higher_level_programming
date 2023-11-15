#!/usr/bin/python3
import sys
import os
import json
""" Add all arguments to a list """


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if os.path.exists("add_item.py"):
    my_list = load_from_json_file("add_item.json")
else:
    my_list = []
for i in range(1, len(sys.argv)):
    my_list.append(args[1:])
save_to_json_file(my_list, "add_item.json")
