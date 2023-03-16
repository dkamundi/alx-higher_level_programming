#!/usr/bin/python3

def uniq_add(my_list=[]):
    my_list = list(dict.fromkeys(my_list))
    result = 0
    for i in range(len(my_list)):
        result += my_list[i]
    return result
