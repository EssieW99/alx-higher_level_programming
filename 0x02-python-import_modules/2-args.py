#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = len(sys.argv) - 1
    if args == 0:
        print("{} arguments.".format(args))
    else:
        print("{} argument{}:".format(args, 's' if args != 1 else ""))
    for index in range(1, len(sys.argv)):
        print("{}: {}".format(index, sys.argv[index]))
