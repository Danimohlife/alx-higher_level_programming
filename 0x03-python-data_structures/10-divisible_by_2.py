#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    
    table = []

    for item in my_list:
        if item % 2 == 0:
            table.append(True)
        else:
            table.append(False)
    return table
