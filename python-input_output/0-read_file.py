#!/usr/bin/python3

def read_file(filename="my_file_0.txt"):
    with open(filename, "r", encoding="utf-8") as fichier:
        print(fichier.read(), end="")
