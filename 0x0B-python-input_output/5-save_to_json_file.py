#!/usr/bin/python3
"""
A function that writes an Object to a text file, using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a text file using a JSON representation.

    Parameters:
    my_obj (any): The Python object to be serialized and written to the file.
    filename (str): The name of the file where the object will be stored.

    Returns:
    int: The number of characters written to the file.

    Example Usage:
    >>> save_to_json_file({"name": "Alice", "age": 30}, "output.json")
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(json.dumps(my_obj))
