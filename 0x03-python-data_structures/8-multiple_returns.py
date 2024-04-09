#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return(0, None)
    length = 0
    for _ in sentence:
        length = length + 1
    return length, sentence[0]
