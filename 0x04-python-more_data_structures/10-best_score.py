#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    best = (None, -1)
    for k in a_dictionary.keys():
        num = a_dictionary.get(k)
        if num > best[1]:
            best = (k, num)
    return best[0]
