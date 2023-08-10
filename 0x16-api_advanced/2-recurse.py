#!/usr/bin/python3

"""
    Hint: The Reddit API uses pagination for separating pages
    Prototype: def recurse(subreddit, hot_list=[])
    Note: You may change the prototype but not the working
    If not a valid subreddit, return None
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """If not a valid subreddit, return None."""
    base_url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    user_agent = {'User-Agent': 'MyRedditScript/1.0'}
    params = {'after': after} if after else {}

    res = requests.get(base_url, headers=user_agent,
                       params=params, allow_redirects=False)

    if res.status_code == 200:
        try:
            data = res.json()
            posts = data['data']['children']

            if not posts:
                return hot_list

            hot_list.extend([post['data']['title'] for post in posts])
            after = data['data']['after']

            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        except (KeyError, ValueError):
            return None
    else:
        return None


def top_ten(subreddit):
    '''
    Prints the titles of the first 10 hot posts for a given subreddit.
    '''
    hot_list = recurse(subreddit)

    if hot_list is not None:
        for i, title in enumerate(hot_list[:10], start=1):
            print(f"{i}. {title}")
    else:
        print(None)
