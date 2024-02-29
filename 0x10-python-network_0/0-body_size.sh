#!/bin/bash
# a script that sends a request to a URL and displays the size of the body
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
