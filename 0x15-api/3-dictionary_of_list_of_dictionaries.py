#!/usr/bin/python3
"""
Dictionary of list of dictionaries
"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos"
    res = requests.get(url=url)
    todos = res.json()
    url = "https://jsonplaceholder.typicode.com/users/"
    res = requests.get(url=url)
    users = res.json()
    data = {}
    for user in users:
        data[user.get("id")] = []
        user_todos = list(filter(lambda x: x.get(
            "userId") == user.get("id"), todos))
        for user_todo in user_todos:
            data[user.get("id")].append({
                "task": user_todo.get("title"),
                "completed": user_todo.get("completed"),
                "username": user.get("username")
            })
    with open("todo_all_employees.json", 'w', encoding="utf-8") as f:
        print(json.dumps(data), file=f, end='')
