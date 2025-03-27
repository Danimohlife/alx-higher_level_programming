#!/usr/bin/python3
"""
append text on a file
"""


def append_write(filename="", text=""):
    """
    Appends the given text to the specified file.
    If the file does not exist, it is created automatically.

    Parameters:
    filename (str): The name of the file to append text to.
    text (str): The text to be appended to the file.

    Returns:
    int: The number of characters written to the file.

    Example Usage:
    >>> append_write("example.txt", "Hello, world!")
    13  # (Number of characters written)
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
