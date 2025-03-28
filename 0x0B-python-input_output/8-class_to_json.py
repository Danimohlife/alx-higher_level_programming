#!/usr/bin/python3
"""
A function that returns the dictionary description of an object
for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary description of an object for JSON serialization.

    Parameters:
    obj (object): An instance of a class.

    Returns:
    dict: A dictionary containing all serializable attributes of the object.

    Example Usage:
    >>> class Person:
    ...     def __init__(self, name, age, is_student):
    ...         self.name = name
    ...         self.age = age
    ...         self.is_student = is_student
    ...
    >>> person = Person("Alice", 30, False)
    >>> class_to_json(person)
    {'name': 'Alice', 'age': 30, 'is_student': False}
    """
    return obj.__dict__
