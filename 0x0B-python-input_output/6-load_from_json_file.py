#!/usr/bin/python3
"""
A function that creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """
    Reads a JSON file and converts its content into a Python object.

    Parameters:
    filename (str): The name of the file containing the JSON data.

    Returns:
    any: The corresponding Python object.

    Example Usage:
    >>> data = load_from_json_file("data.json")
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.loads(file.read())
