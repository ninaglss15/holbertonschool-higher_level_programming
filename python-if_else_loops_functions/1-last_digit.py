#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_d = number % 10
if last_d > 5:
    print(F"Last digit of {number} is {last_d} and is greater than 5")
elif last_d == 0:
    print(F"Last digit of {number} and is {last_d}")
elif last_d < 6:
    print(F"Last digit of {number} is {last_d} and is less than 6 and not 0")
