#!/usr/bin/python3
for print_numbers in range(99):
    decimal = "{}".format(print_numbers)
    hexadecimal = "{:x}".format(print_numbers)
    print("{} = 0x{}".format(decimal, hexadecimal))
