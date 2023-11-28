#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

abs_num = abs(number)

ls_num = abs_num % 10

if number < 0:
    ls_num *= -1  # Adjust the last digit if the number is negative

if ls_num > 5:
    print(f"Last digit of {number} is {ls_num} and is greater than 5")
elif ls_num == 0:
    print(f"Last digit of {number} is {ls_num} and is 0")
elif ls_num < 5 and ls_num != 0:
    print(f"Last digit of {number} is {ls_num} and is less than 6 and not 0")
