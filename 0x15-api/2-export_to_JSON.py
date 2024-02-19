#!/usr/bin/python3
"""
Export to JSON
"""
import json
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
    data = {}
    data[str(arg)] = []
    for todo in todos:
        data[str(arg)].append({
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": user_name
        })
    with open(
        "{}.json".format(arg), 'w', encoding="utf-8"
    ) as f:
        print(json.dumps(data), file=f, end='')
