#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8)
"""
import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    link = sys.argv[1]
    try:
        with urllib.request.urlopen(link) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.request.HTTPError as e:
        print(f"Error code: {e.code}")
