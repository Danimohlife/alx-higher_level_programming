#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    my_lists = my_list

    my_lists.reverse()

    for x in range(len(my_lists)):
        print("{:d}".format(my_lists[x]))
