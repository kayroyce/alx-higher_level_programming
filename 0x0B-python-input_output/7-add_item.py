#!/usr/bin/python3
"""Program to save strings from command line arguments to file called
`add_item.json`. File contains a json serialized list of all strings
entered as arguments to the program.
Example:
    $ ./9-add_item.py Best School
    $ cat add_item.json ; echo
    ["Best", "School"]
    $ ./9-add_item.py Python 89 C
    $ cat add_item.json ; echo
    ["Best", "School", "Python", "89", "C"]
"""

if __name__ == "__main__":
    import sys
    import json
    save_to_json_file = \
        __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    filename = "add_item.json"
    with open(filename, 'a+') as f:  # Create add_item.json, if necessary
        if f.tell() == 0:
            json.dump([], f)
    file_data = load_from_json_file("add_item.json")
    if len(sys.argv) > 1:
        file_data.extend(sys.argv[1:])
    save_to_json_file(file_data, filename)
