#!/usr/bin/python3
"""
    Prototype: def number_of_subscribers(subreddit)
    If not a valid subreddit, return 0
    NOTE: Invalid subreddits may return a redirect to search results
    Ensure that you are not following redirects.
"""
import requests

def number_of_subscribers(subreddit):
    """A function that queries the reddit api"""
    about_url = f'https://www.reddit.com/r/{subreddit}/about.json'
    user_agent = {'User-Agent': 'MyRedditScript/1.'}

    res = requests.get(about_url, headers=user_agent)

    if res.status_code == 200:
        try:
            data = res.json()
            return data['data']['subscribers']
        except (KeyError, ValueError):
            return 0
    else:
        return 0
