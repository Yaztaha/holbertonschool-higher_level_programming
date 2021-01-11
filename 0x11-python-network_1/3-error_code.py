#!/usr/bin/python3
""" Request URL with error exception management """
from url.request import Request, urlopen
from urllib.error import HTTPError
import sys

req = Request(sys.argv[1])
try:
    response = urlopen(req)
    html = response.read()
    print(html.decode('utf-8'))
except HTTPError as e:
    print('Error Code: ', e.code)
