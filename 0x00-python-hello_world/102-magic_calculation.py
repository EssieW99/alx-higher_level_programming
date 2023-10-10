#!/usr/bin/python3
# 102-magic_calculation.py
import dis


def magic_calculation(a, b):
    return (a**b) + 98


dis.dis(magic_calculation)
