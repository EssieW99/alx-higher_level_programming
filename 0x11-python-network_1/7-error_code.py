#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL
and displays the body of the response
"""
import requests
import sys


if __name__ == "__main__":
    try:
        r = requests.get(sys.argv[1])
    except requests.exceptions.HTTPError as e:
        print(e.code)
