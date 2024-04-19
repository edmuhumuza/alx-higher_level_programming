#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    sum_t = 0
    for element in my_list:
        sum_t += element[1]
    mul = 0
    for tup in my_list:
        mul += (tup[0] * tup[1])
    return mul/sum_t
