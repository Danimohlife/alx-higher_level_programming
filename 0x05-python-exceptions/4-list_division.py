#!/usr/bin/python3
"""
safe list division
"""


def list_division(my_list_1, my_list_2, list_length):
    """
    list dibision
    """

    my_list_3 = []

    for lop in range(list_length):
        try:
            ans = my_list_1[lop] / my_list_2[lop]
        except ZeroDivisionError:
            print("division by 0")
            ans = 0
        except TypeError:
            print("wrong type")
            ans = 0
        except IndexError:
            print("out of range")
            ans = 0
        finally:
            my_list_3.append(ans)

    return my_list_3
