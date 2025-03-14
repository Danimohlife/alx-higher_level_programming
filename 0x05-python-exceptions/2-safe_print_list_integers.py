#!/usr/bin/python3
"""
continuos safe print list value
"""


def safe_print_list_integers(my_list=[], x=0):
    """
    print int only and silence value error
    but not index error
    """

    count = 0

    for lop in range(x):
        try:
            print("{:d}".format(my_list[lop]), end='')
            count += 1
        except (ValueError, TypeError):
            pass

    print()
    return count
