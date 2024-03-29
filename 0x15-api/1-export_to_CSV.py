#!/usr/bin/python3
"""
Export to CSV
"""
import requests
import sys

if __name__ == "__main__":
    arg = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(arg)
    res = requests.get(url=url)
    todos = res.json()
    url = "https://jsonplaceholder.typicode.com/users/{}".format(arg)
    res = requests.get(url=url)
    user = res.json()
    user_name = user.get("username")
    for todo in todos:
        data = '"{0}","{1}","{2}","{3}"'.format(
            arg,
            user_name,
            todo.get("completed"),
            todo.get("title")
        )
        with open(
            "{}.csv".format(arg), 'a', encoding="utf-8"
        ) as f:
            print(data, file=f)
