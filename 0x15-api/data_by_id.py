#!/usr/bin/python3

"""
    A python script that uses REST API for a given employee ID
    returns his/her TODO list progress
"""


if __name__ == "__main__":
    import requests
    import sys
    import csv

    user_id = sys.argv[1]
    baseurl = "https://jsonplaceholder.typicode.com/"
    # userUrl = baseurl + 'users/' +  user_id
    taskUrl = baseurl + 'todos/'
    
    users = requests.get(taskUrl, params={"userId": user_id})
    data = users.json()

    [print("{}".format(i)) for i in data]
    print("----------------------------------------------------------------------------------")
    [print("{}".format(i)) for i in data if i.get('completed') is True]
    print("----------------------------------------------------------------------------------")
    title = [i.get('title') for i in data if i.get("completed") is False]
    [print("\t{}".format(i)) for i in title]
    print("**********************************************************************************")
    print("{}".format(len(title)))

    with open('id.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        [writer.writerow([i.get('userId'),
                            i.get('id'),
                            i.get('title'),
                            i.get('completed')]) for i in data]
