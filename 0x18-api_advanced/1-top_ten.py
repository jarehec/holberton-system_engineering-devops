#!/usr/bin/python3
"""
prints the top ten titles of a given subreddit
"""
from requests import get


def top_ten(subreddit):
    try:
        res = get("https://www.reddit.com/r/{}/hot.json".format(subreddit),
                  headers={'User-agent': 'hAxr'}, params={'limit': 10},
                  allow_redirects=False).json()
        for item in res['data']['children']:
            print(item['data']['title'])
    except:
        print('None')
