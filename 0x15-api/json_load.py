#!/usr/bin/python3

"""
    A python script that uses REST API for a given employee ID
    returns his/her TODO list progress
"""


if __name__ == "__main__":
    import json

    with open('2.2.json', 'w') as f:
        data = json.loads(f)
        print(data)
