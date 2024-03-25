#!/usr/bin/python3
x = 1
for _ in range(122, 96, -1):
    if x % 2 == 0:
        print("{:c}".format(_-32), end="")
        x = x + 1
    else:
        print("{:c}".format(_), end="")
        x = x + 1
