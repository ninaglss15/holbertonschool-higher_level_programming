#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":

    noms = dir(hidden_4)

    noms_tries = sorted(noms)

    for nom in noms_tries:
        if not nom.startswith("__"):
            print(nom)
