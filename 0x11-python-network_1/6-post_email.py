#!/usr/bin/python3
'''
    Takes in a URL, sends a request to the URL and displays value 
    of request id
'''

import requests
from sys import 

if __name__ == "__main__":
    r = requests.post(argv[1], data={'email': argv[2]})
    print(r.text)
