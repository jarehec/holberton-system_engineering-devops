#!/usr/bin/python3
"""
returns information about employee TODO list progress based on id
"""
from requests import get
from sys import argv


if __name__ == '__main__':
        done = 0
        tasks = []
        root = 'https://jsonplaceholder.typicode.com'
        name = get(root + '/users/{}'.format(argv[1])).json().get('name')
        for i in get(root + '/todos').json():
            if i.get('userId') == int(argv[1]):
                tasks.append(i)
                if i.get('completed') is True:
                    done += 1
        print("Employee {} is done with tasks({}/{}):".
              format(name, done, len(tasks)))
        for i in tasks:
            if i.get('completed') is True:
                print("\t {}".format(i.get('title')))
