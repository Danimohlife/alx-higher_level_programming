#!/usr/bin/python3
# 2-args.py
# Brennan D Baraban <375@holbertonschool.com>

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    ln = len(sys.argv) - 1
    if ln == 0:
        print("0 arguments.")
    elif ln == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(ln))
    for i in range(ln):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
