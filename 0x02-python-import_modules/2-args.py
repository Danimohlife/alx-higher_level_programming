#!/usr/bin/python3

import sys

if __name__ == "__main__":

    l_st = sys.argv
    ln = len(l_st) - 1

    print("{:d} {}".format(ln, 'argument.' if ln <= 1 else 'arguments:'))

    ln += 1
    for i in range(1, ln):
        print("{}: {}".format(i, l_st[i]))
