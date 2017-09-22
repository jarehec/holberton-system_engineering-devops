#!/usr/bin/pyhon3
"""
prints the top ten titles of a given subreddit
"""
from requests import get


def top_ten(subreddit):
    try:
        res = get("https://www.reddit.com/r/{}/hot.json".format(subreddit),
                  headers={'User-agent': 'hAxr'}, allow_redirects=False).json()
        i = 0
        for item in res.get('data').get('children'):
            print(item.get('data').get('title'))
            i += 1
            if i > 9:
                break
    except:
        print('None')
