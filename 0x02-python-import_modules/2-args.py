#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arguments = len(sys.argv) - 1
    if arguments == 0:
        print("{} arguments.".format(arguments))
    else:
        print("{} argument{}:".format(arguments, 's' if arguments != 1 else ""))
    for index in range(1, len(sys.argv)):
        print("{}: {}".format(index, sys.argv[index]))
