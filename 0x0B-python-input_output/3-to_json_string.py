#!/usr/bin/python3
"""
to convert python object into json data type (str)
"""
import json


def to_json_string(my_obj):
    """
    Converts a Python object into a JSON-formatted string.

    Parameters:
    my_obj (any): The Python object to be serialized into JSON.

    Returns:
    str: The JSON representation of the object.

    Example Usage:
    >>> to_json_string({"name": "Alice", "age": 30})
    '{"name": "Alice", "age": 30}'
    """
    return json.dumps(my_obj)
