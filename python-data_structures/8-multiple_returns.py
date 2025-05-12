#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence == "":
        return None
    else:
        lenn = len(sentence)
        return (lenn, sentence[0])
