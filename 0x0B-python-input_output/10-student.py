#!/usr/bin/python3
"""
A class that defines a Student.
"""


class Student:
    """
    A class representing a student with first name, last name, and age.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Parameters:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, att=None):
        """
        Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, only attribute names contained
        in this list are retrieved. Otherwise, all attributes are retrieved.

        Parameters:
            attrs (list, optional): A list of attribute names to retrieve.

        Returns:
            dict: A dictionary representation of the student.
        """
        if isinstance(att, list) and all(isinstance(atr, str) for atr in att):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
