#!/usr/bin/python3
"""
convert json data to python object
"""
import json


def from_json_string(my_str):
    """
    Converts a JSON-formatted string into a Python object.

    Parameters:
    my_str (str): The JSON string to be deserialized.

    Returns:
    any: The corresponding Python object.

    Example Usage:
    >>> from_json_string('{"name": "Alice", "age": 30}')
    {'name': 'Alice', 'age': 30}
    """
    return json.loads(my_str)
