#!/usr/bin/python3
import sys
if __name__ == "__main__":
    result = 0
    for args in sys.argv[1:]:
        result = result + int(args)
    print("{}".format(result))
