#!/usr/bin/python3
for _ in range(0, 100):
    if _ == range(0, 100)[-1]:
        print("{:02d}".format(_))
    else:
        print("{:02d}, ".format(_), end="")
