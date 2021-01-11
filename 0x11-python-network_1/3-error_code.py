#!/usr/bin/python3
""" Request URL with error exception management """
import urllib.request
import sys

req = urllib.request.Request(sys.argv[1])
try:
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print(html.decode('utf-8'))
except urllib.error.HTTPError as e:
    print('Error Code: ', e.code)
