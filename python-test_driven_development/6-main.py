#!/usr/bin/python3
max_integer = __import__('6-max_integer').max_integer

def main():
    print(max_integer([1, 2, 3, 4]))        # 4
    print(max_integer([1, 3, 4, 2]))        # 4
    print(max_integer([4, 3, 2, 1]))        # 4
    print(max_integer([]))                   # None
    print(max_integer([42]))                 # 42
    print(max_integer([1.5, 2.7, 2.3]))     # 2.7
    print(max_integer([-1, -3, -2, -4]))    # -1
    print(max_integer([1, 2.5, 3, 0]))      # 3

if __name__ == "__main__":
    main()
