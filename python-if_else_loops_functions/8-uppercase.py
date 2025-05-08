#!/usr/bin/python3

#!/usr/bin/python3

def uppercase(str):
    for caractere in str:

        if 'a' <= caractere <= 'z':
            caractere = chr(ord(caractere) - 32)
        
        print("{}".format(caractere), end="")

    print()
