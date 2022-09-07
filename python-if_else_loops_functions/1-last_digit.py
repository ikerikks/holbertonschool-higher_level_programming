#!/usr/bin/python3

import random

number = random.randint(-10000, 10000)
str = "Last digit of"
last_digit = number % 10

if number < 0:
    last_digit = (number * (-1)) % 10 * (-1)

if last_digit > 5:
    print(f"{str} {number} is {last_digit} and is greater than 5")

if last_digit == 0:
    print(f"{str} {number} is {last_digit} and is 0")

if last_digit < 6 and last_digit != 0:
    print(f"{str} {number} is {last_digit} and is less than 6 and not 0")
