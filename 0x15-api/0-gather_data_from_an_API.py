#!/usr/bin/python3
"""
Gather data from an API
"""
import requests
import sys

if __name__ == "__main__":
    arg = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(arg)
    res = requests.get(url=url)
    todos = res.json()
    url = "https://jsonplaceholder.typicode.com/users/{}".format(
        todos[0].get("userId"))
    res = requests.get(url=url)
    user = res.json()
    user_name = user.get("name")
    completed_todos = list(filter(lambda x: x.get("completed") is True, todos))
    print(
        "Employee {0} is done with tasks({1}/{2}):".format(
            user_name,
            len(completed_todos),
            len(todos)
        )
    )
    for todo in completed_todos:
        print("\t{}".format(todo.get("title")))
