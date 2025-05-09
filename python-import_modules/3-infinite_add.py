#!/usr/bin/python3
import sys

total = 0
if __name__ == "__main__":
    for i in range(1, len(sys.argv)):
        total += int(sys.argv[i])
    print(total)
