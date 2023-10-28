#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for a in range(x):
            if isinstance(my_list[a], int):
                print("{:d}".format(my_list[a]), end="")
            else:
                continue
            count += 1
        print()
        return count
    except (ValueError, TypeError):
        pass
