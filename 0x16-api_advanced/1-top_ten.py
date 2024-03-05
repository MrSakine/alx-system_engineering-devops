#!/usr/bin/python3
"""
This module queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """Return the top ten of a sub reddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "MyRedditBot/1.0 (fily)"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get("data")
        for _, post in enumerate(data.get("children"), start=1):
            res = post.get("data")
            print("{}".format(res.get("title")))
    else:
        print("None")
