#!/usr/bin/python3
def multiple_returns(sentence):
    for i in sentence:
        if i == " " :
            sentence[0] = None
        else:
            print("Length: {} - First character: {}".format(len(sentence), sentence[0]))
