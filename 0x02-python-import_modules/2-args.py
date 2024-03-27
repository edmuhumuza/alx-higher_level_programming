#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        print('0 arguments.')
    else:
        if len(sys.argv) == 2:
            print('{} argument:'.format(len(sys.argv)-1))
            print('{}: {}'.format(len(sys.argv)-1, sys.argv[1]))
        elif len(sys.argv) > 1:
            print('{} arguments:'.format(len(sys.argv) - 1))
            x = 1
            for _ in sys.argv:
                if  _ == sys.argv[0]:
                    continue
                print('{}: {}'.format(x, sys.argv[x]))
                x += 1
