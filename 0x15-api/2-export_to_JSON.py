#!/usr/bin/python3

"""
    A python script that uses REST API for a given employee ID
    returns his/her TODO list progress
"""


if __name__ == "__main__":
    import requests
    import sys
    import json

    baseUrl = "https://jsonplaceholder.typicode.com/"
    user = sys.argv[1]

    employee = requests.get(baseUrl + "users/{}".format(user)).json()
    todos = requests.get(baseUrl + "todos", params={"userId": user}).json()
    username = employee.get("username")

    with open('{}.json'.format(user), 'w') as file:
        json.dump({user: [{
                "tasks": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todos]}, file)
