#!/usr/bin/python3
""" Posting email using REQUESTS module """
import requests
import sys

if __name__ == "__main__":
    r = requests.post(sys.argv[1], {"email": sys.argv[2]})
    print(r.text)
