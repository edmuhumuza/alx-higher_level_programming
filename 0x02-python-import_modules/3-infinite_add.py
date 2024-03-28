#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        print('0')
    else:
        total = 0
        for _ in sys.argv:
            if _ == sys.argv[0]:
                continue
            total = total + int(_)
        print(total)
