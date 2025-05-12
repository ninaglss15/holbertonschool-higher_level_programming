#!/usr/bin/python3

def multiple_returns(sentence):
    lu = 0
    le = len(sentence)
    if sentence == "":
        lu = None
    else:
        lu = sentence[0]
        return (le, lu)
