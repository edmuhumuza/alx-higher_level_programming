#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = []
    str_copy = list(str)
    copy = ""
    if n >= 0 and n <= len(str_copy):
        for _ in str_copy:
            if _ == str_copy[n]:
                continue
            else:
                new_str.append(_)
    else:
        for _ in str_copy:
            new_str.append(_)
    return copy.join(new_str)
