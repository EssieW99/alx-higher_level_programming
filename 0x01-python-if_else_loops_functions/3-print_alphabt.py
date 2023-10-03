#!/usr/bin/python3
for get_int in range(ord('a'), ord('z') + 1):
    if get_int != ord('e') and get_int != ord('q'):
        print("{}".format(chr(get_int)), end='')
