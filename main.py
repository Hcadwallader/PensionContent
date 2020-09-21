#!/usr/bin/env python

import json

def load_data():
    with open('data/sample-funds.json') as json_file:
        data = json.load(json_file)
        print(data)

if __name__ == '__main__':
    print("hello world")
    load_data()
