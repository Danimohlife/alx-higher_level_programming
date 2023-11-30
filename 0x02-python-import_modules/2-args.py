#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    l_st = sys.argv
    ln = len(l_st) - 1
    print("{:d} {}".format(ln, 'argument.' if ln == 1 or ln == 0 else 'arguments:'))

    ln += 1
    for i in range(1, ln):
        print("{}: {}".format(i, l_st[i]))
