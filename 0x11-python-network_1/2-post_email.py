#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request
with the email as a parameter and displays the body
"""
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    link = sys.argv[1]
    value = {'email': sys.argv[2]}
    # produces a string to be sent in the POST request
    data = urllib.parse.urlencode(value)
    # data ought to be in bytes
    data = data.encode('utf-8')
    # create a Request object with the URL obtained
    req = urllib.request.Request(link, data)
    # opens the file-like object rep. the response
    with urllib.request.urlopen(req) as response:
        page = response.read()
    # print the body of the response
    print(page.decode('utf-8'))
