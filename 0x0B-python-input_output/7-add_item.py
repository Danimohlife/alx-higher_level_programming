#!/usr/bin/python3
"""
A script that adds all command-line arguments to a
Python list and saves them to a file.
If the file doesn’t exist, it should be created
You don’t need to manage file permissions / exceptions."""


import sys
import json


"""
loading external files for json and object conversion
"""


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"

"""
checking if required file exit first before loading with imported function
"""
data = load_from_json_file(filename) if os.path.exists(filename) else []

data.extend(sys.argv[1:])
save_to_json_file(data, filename)
