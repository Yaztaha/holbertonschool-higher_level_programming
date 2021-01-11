#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status """
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as res:
        html = res.read()
        print("Body response:\n\
\t- type: {}\n\
\t- content: {}".format(type(html), html))
