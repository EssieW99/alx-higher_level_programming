#!/usr/bin/python3
for digit in range(10):
    for combination in range(1 + digit, 10):
        number = "{}{}".format(digit, combination)
        delimeter = ", "
        if digit != 8:
            print("{}{}".format(number, delimeter), end="")
        else:
            print("{}".format(number))
