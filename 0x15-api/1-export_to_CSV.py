#!/usr/bin/python3

"""
    A python script that uses REST API for a given employee ID
    returns his/her TODO list progress
"""


if __name__ == "__main__":
    import requests
    import sys
    import csv

    baseUrl = "https://jsonplaceholder.typicode.com/"
    user = sys.argv[1]

    employee = requests.get(baseUrl + "users/{}".format(user)).json()
    todos = requests.get(baseUrl + "todos", params={"userId": user}).json()
    username = employee.get("username")

    with open('{}.csv'.format(user), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow([user, username, t.get("completed"), t.get("title")]) for t in todos]
