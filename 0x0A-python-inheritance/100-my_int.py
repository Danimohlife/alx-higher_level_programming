#!/usr/bin/python3
"""
This module defines the MyInt class, a subclass of int
with inverted equality operators.
"""


class MyInt(int):
    """A rebel integer class that inverts `==` and `!=` operators."""

    def __eq__(self, other):
        """Override `==` (equal) to behave like `!=` (not equal)."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override `!=` (not equal) to behave like `==` (equal)."""
        return super().__eq__(other)
