#!/usr/bin/python3
""" POST with urllib.parse """

if __name__ == "__main__":
    data = urllib.parse.encode({'email': sys.argv[2]})
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)

    with urllib.request.urlopen(req) as response:
        html = response.read()
        print(html.decode('utf-8'))
