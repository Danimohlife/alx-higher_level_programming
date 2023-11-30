#!/usr/bin/python3
import sys

if __name__ == "__main__":
    ln = len(sys.argv) - 1

    num = 0

    for x in range(ln):
        num += int(sys.argv[x + 1])
    print("{:d}".format(num))
