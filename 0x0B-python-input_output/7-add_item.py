#!/usr/bin/python3
"""
A script that adds all command-line arguments to a
Python list and saves them to a file.
If the file doesn’t exist, it should be created
You don’t need to manage file permissions / exceptions
"""

import sys
import json

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def add_item():
    """
    If the file doesn’t exist, it should be created
    You don’t need to manage file permissions /
    exceptions.
    """
    filename = "add_item.json"

    data = load_from_json_file(filename) if os.path.exists(filename) else []

    data.extend(sys.argv[1:])
    save_to_json_file(data, filename)


add_item()
