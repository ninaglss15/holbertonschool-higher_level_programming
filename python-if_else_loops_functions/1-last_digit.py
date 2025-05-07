#!/usr/bin/python3

import random
number = random.randint(-10000, 10000)
pepechiken = (number) % 10
if pepechiken > 5:
    print(f"Last digit of {pepechiken} and is greater than 5")
elif pepechiken == 0:
    print(f"Last digit of {pepechiken} and is 0")
else:
    print(f"Last digit of {pepechiken} and is less than 6 and not 0")
