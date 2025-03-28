#!/usr/bin/python3
"""
Module with a script that adds arguments
to a Python list saved in a file
"""

import sys
import os


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


"""
If the file doesn’t exist, it should be created
You don’t need to manage file permissions /
exceptions.
"""
filename = "add_item.json"

data = load_from_json_file(filename) if os.path.exists(filename) else []
data.extend(sys.argv[1:])
save_to_json_file(data, filename)
