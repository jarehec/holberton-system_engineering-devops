#!/usr/bin/python3
"""
 exports json file with information about employee progress based on id
"""
from collections import OrderedDict
import json
from requests import get
from sys import argv


if __name__ == '__main__':
        task = OrderedDict()
        tasks_list = []
        user_dict = {}
        root = 'https://jsonplaceholder.typicode.com'
        user = get(root + '/users/{}'.format(argv[1])).json()
        for i in get(root + '/todos').json():
            if i.get('userId') == int(argv[1]):
                task["task"] = i.get('title')
                task['completed'] = i.get('completed')
                task['username'] = user.get('username')
                tasks_list.append(task)
                task = OrderedDict()
        user_dict[argv[1]] = tasks_list
        with open('{}.json'.format(argv[1]), 'w') as f:
            json.dump(user_dict, f)
