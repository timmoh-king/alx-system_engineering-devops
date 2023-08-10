#!/usr/bin/python3
"""
    Write a function that queries the Reddit API
    prints the titles of the first 10 hot posts
    listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts"""
    about_url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    user_agent = {'User-Agent': 'MyRedditScript/1.0'}

    res = requests.get(about_url, headers=user_agent)

    if res.status_code == 200:
        try:
            data = res.json()
            posts = data['data']['children']
            for post in posts[:10]:
                print(post['data']['title'])
        except (KeyError, ValueError):
            print(None)
    else:
        print(None)
