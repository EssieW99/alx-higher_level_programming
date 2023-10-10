#!/usr/bin/python3
# 100-print_tebahpla.py
for c in range(ord('z'),ord('A') - 1, -1):
    if (ord('a') <= c <= ord('z')) or (ord('A') <= c <= ord('Z')):
        if c % 2 != 0:
            c = chr(c - 32)
        else:
            c = chr(c)
        print("{}".format(c), end="")
