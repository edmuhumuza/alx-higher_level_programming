#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    my_dict = a_dictionary.keys()
    new_dict = {}
    for _ in my_dict:
        new_dict[_] = a_dictionary[_] * 2
    return new_dict
