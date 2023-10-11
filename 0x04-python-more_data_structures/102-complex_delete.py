#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    to_del = []
    for k in a_dictionary.keys():
        if a_dictionary[k] == value:
            to_del.append(k)
    for k in to_del:
        a_dictionary.pop(k)
    return a_dictionary
