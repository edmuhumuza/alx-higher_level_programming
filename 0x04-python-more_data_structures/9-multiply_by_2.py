#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.keys()
    for _ in new_dict:
        a_dictionary[_] = a_dictionary[_] * 2
    return a_dictionary
