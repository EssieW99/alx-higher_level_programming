#!/usr/bin/python3
"""
takes in a letter and sends a POST request to a URL
with the letter as a parameter
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    try:
        r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
        r.raise_for_status()
        j_data = r.json()

        if not j_data:
            print("No result")
        else:
            print(f"[{j_data.get('id')}] {j_data.get('name')}")
    except ValueError:
        print("Not a valid JSON")
