#!/usr/bin/python3
def multiple_returns(sentence):
    a_tuple = ()
    sent_cpy = list(sentence)
    if sentence == "":
        a_tuple = (len(sent_cpy), None)
    else:
        a_tuple = (len(sent_cpy), sent_cpy[0])
    return a_tuple
