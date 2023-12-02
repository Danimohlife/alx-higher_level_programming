#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
import sys
import argparse

if __name__ == "__main__":
    ln = len(sys.argv)

    if ln != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    parser = argparse.ArgumentParser(description='Commandline Math Programme')
    parser.add_argument('firstNum', help='First Number')
    parser.add_argument('sign', help='sign to use')
    parser.add_argument('secondNum', help='Second Number')
    args = parser.parse_args()

    a = int(args.firstNum)
    b = int(args.secondNum)

    if args.sign == '*':
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    elif args.sign == '/':
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
    elif args.sign == '+':
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif args.sign == '-':
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    else:
        print(f"Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
