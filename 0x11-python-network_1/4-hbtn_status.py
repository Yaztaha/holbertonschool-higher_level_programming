#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status """
import requests

response = requests.get('https://intranet.hbtn.io/status')
print("Body response:\n\
\t- type: {}\n\
\t- content: {}".format(type(response.text), response.text))
