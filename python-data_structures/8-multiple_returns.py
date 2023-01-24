#!/usr/bin/python3


def multiple_returns(sentence):
    len_sen = len(sentence)
    
    for i in range(len_sen):
        return len_sen, sentence[0]
    
