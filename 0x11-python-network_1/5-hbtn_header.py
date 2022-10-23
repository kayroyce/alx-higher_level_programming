#!/usr/bin/python3
'''
    Takes in a URL, sends a request to the URL and displays the value of the variable
    in the response header
'''

import requests
from sys import 

if __name__ == "__main__":
    r = requests.get(argv[1])
    print(r.headers.get("X-Request-Id"))

