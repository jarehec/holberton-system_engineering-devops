#!/usr/bin/python3
"""
exports csv file with information about employee based on id
"""
import csv
from requests import get
from sys import argv


if __name__ == '__main__':
        tasks = []
        tasks_list = []
        root = 'https://jsonplaceholder.typicode.com'
        user = get(root + '/users/{}'.format(argv[1])).json()
        for i in get(root + '/todos').json():
            if i.get('userId') == int(argv[1]):
                tasks.append(argv[1])
                tasks.append(user.get('username'))
                tasks.append(i.get('completed'))
                tasks.append(i.get('title'))
                tasks_list.append(tasks)
                tasks = []
        with open('{}.csv'.format(argv[1]), 'w') as f:
            f_csv = csv.writer(f, quoting=csv.QUOTE_ALL)
            f_csv.writerows(tasks_list)
