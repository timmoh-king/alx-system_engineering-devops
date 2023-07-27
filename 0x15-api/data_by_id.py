#!/usr/bin/python3

"""
    A python script that uses REST API for a given employee ID
    returns his/her TODO list progress
"""


if __name__ == "__main__":
    import requests
    import sys

    user_id = sys.argv[1]
    baseurl = "https://jsonplaceholder.typicode.com/"
    # userUrl = baseurl + 'users/' +  user_id
    taskUrl = baseurl + 'todos/'
    
    users = requests.get(taskUrl, params={"userId": user_id})
    data = users.json()
    # [print("{}".format(i)) for i in data if i.get('completed') is True]

    # for i in data:
    #     print("Task Name:", i['title'])

    [print("{}".format(i)) for i in data]
    print("----------------------------------------------------------------------------------")
    [print("{}".format(i)) for i in data if i.get('completed') is True]
    print("----------------------------------------------------------------------------------")
    title = [i.get('title') for i in data if i.get("completed") is False]
    [print("\t{}".format(i)) for i in title]
