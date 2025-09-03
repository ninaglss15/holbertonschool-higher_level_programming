#!/usr/bin/python3
def uppercase(str):

    for caractere in str:
        if 'a' <= caractere <= 'z':
            majuscule = chr(ord(caractere) - 32)
        else:
            majuscule = caractere
        print("{}".format(majuscule), end="")

    print()
