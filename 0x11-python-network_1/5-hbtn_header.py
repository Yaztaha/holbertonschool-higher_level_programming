#!/usr/bin/python3
""" Header response using REQUESTS module """
import requests
import sys

if __name__ == "__main__":
    html = requests.get(sys.argv[1])
    print(html.headers.get('X-Request-Id'))
