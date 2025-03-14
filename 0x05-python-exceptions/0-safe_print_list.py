#!/usr/bin/python3
"""
function to print list safely with out
of range index calling
"""


def safe_print_list(my_list=[], x=0):
    """
    safe print list
    function
    """
    count = 0

    for lop in range(x):
        try:
            print(my_list[lop], end='')
            count += 1
        except IndexError:
            print()
            return count
    return count



my_list = [1, 2, 3, 4]
x = len(my_list) + 1

nb_print = safe_print_list(my_list, x)
print("{:d}".format(nb_print))
