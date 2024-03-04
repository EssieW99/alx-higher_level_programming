#!/usr/bin/python3
"""
takes in a URL, sends a GET request to the URL
and displays the body of the response
"""
import urllib.request
import sys


if __name__ == "__main__":
    link = sys.argv[1]
    with urllib.request.urlopen(link) as response:
        html = response.read()
    id = response.headers.get('X-Request-Id')
    print(id)
