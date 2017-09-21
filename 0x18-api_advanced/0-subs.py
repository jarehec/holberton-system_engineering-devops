#!/usr/bin/python3
"""
returns the subscriber count of a given subreddit
"""
from requests import get


def number_of_subscribers(subreddit):
    """ Returns number of subscribers """
    url = "https://reddit.com/r/{}/about.json".format(subreddit)
    res = get(url, headers={'User-agent': 'hAxr'}).json()
    subs = res.get('data').get('subscribers')
    return (subs) if subs is not None else 0
