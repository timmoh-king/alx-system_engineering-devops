#!/usr/bin/python3

"""
    A python script that uses REST API for a given employee ID
    returns his/her TODO list progress
"""


if __name__ == "__main__":
    import requests
    import sys

    baseUrl = "https://jsonplaceholder.typicode.com/"
    user = sys.argv[1]

    employee = requests.get(baseUrl + "users/{}".format(user)).json()
    todos = requests.get(baseUrl + "todos", params={"userId": user}).json()
    completed = [t.get("title") for t in todos if t.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(
        employee.get("name"), len(completed), len(todos)))

    for i in completed:
        print("\t {}".format(i))
