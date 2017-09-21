#!/usr/bin/python3
"""
returns the subscriber count of a given subreddit
"""
from requests import get


def number_of_subscribers(subreddit):
    try:
        i = get("https://www.reddit.com/r/{}/about.json".format(subreddit),
                headers={'User-agent': 'hAxr'}, allow_redirects=False).json()
    except:
        return 0
    return i.get('data').get('subscribers')
