#!/usr/bin/python3

from sys import argv
save = __import__('5-save_to_json_file').save_to_json_file
# def save_to_json_file(my_obj, filename)
load = __import__('6-load_from_json_file').load_from_json_file
# def load_from_json_file(filename)

filename = "add_item.json"
arguments = []

try:
    arguments = load(filename)
except:  # if there is nothing to load
    arguments = argv[1:]
else:  # if there are previous arguments in file
    arguments += argv[1:]
# save arguments to file
save(arguments, filename)
