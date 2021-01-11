#!/usr/bin/python3
""" Displaying GitHub id using API """
import requests
import sys

if __name__ == "__main__":
    r = requests.get('https://api.github.com/user',
                     auth=(sys.argv[1], sys.argv[2]))
    req_id = r.json().get('id')
    print(req_id)
