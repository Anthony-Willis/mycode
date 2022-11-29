#!/usr/bin/env python3
import requests
from pprint import pprint #pretty print)

def main():
    URL= "http://127.0.0.1:2224"
    resp= requests.get(URL).json()
    pprint(resp)


if __name__ == "__main__":
    main()
