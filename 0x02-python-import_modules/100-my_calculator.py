#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    ln = len(sys.argv)

    if ln == 4:
        a = int(sys.argv[1])
        b = int(sys.argv[3])

    if ln != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    for sign in "*+/-":
        if sys.argv[2] == sign and sign == '*':
            print("{:d} {} {:d} = {:d}".format(a, sign, b, a * b))
            break
        elif sys.argv[2] == sign and sign == '/':
            print("{:d} {} {:d} = {:d}".format(a, sign, b, a / b))
            break
        elif sys.argv[2] == sign and sign == '+':
            print("{:d} {} {:d} = {:d}".format(a, sign, b, a + b))
            break
        elif sys.argv[2] == sign and sign == '-':
            print("{:d} {} {:d} = {:d}".format(a, sign, b, a * b))
            break
    else:
        print("{}".format("Unknown operator. Available operators: +, -, * and /"))
        sys.exit(1)
