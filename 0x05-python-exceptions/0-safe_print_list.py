#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for a in my_list:
            if count >= x:
                break
            print(a, end="")
            count += 1
        print()
        return count
    except Exception as e:
        return count
