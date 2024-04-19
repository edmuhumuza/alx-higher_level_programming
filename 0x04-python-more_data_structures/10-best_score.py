#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    d_values = list(a_dictionary.values())
    n = len(d_values)
    for value in range(n):
        for x in range(n-value-1):
            if d_values[x] > d_values[x+1]:
                d_values[x], d_values[x+1] = d_values[x+1], d_values[x]
    g_value = d_values[-1]

    d_keys = a_dictionary.keys()
    for d_key in d_keys:
        if a_dictionary[d_key] == g_value:
            return d_key
