#!/usr/bin/python3

def magic_calculation(a, b):
    result = 0
    for a in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            result += (a ** b) / i
        except Exception as e:
            raise e
            result = a + b
            break
    return result
