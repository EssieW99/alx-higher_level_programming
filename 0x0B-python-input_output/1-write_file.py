#!/usr/bin/python3

def write_file(filename="", text=""):
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            no_chars = file.write(text)
        return no_chars
    except Exception as e:
        print("An error occurred: {}".format(e))
