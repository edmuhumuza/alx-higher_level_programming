#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value not in a_dictionary.values():
        return a_dictionary
    while (value in a_dictionary.values()):
        new_dict = dict(a_dictionary)
        for k,v in new_dict.items():
            if new_dict[k] == value:
                del a_dictionary[k]
        return a_dictionary
