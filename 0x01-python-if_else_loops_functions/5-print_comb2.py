#!/usr/bin/python3
for print_numbers in range(100):
    numbers = "{:02}".format(print_numbers)
    delimeter = ", "
    if print_numbers != 99:
        print("{}{}".format(numbers, delimeter), end="")
    else:
        print("{}".format(numbers))
