#!/usr/bin/python3
"""
This module queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0
"""
import requests


def number_of_subscribers(subreddit):
    """Returns total subscribers of a sub reddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "MyRedditBot/1.0"}
    response = requests.get(url=url, headers=headers, allow_redirects=False)
    if response.status_code == 404 or response.status_code == 302:
        return 0
    return response.json().get("data").get("subscribers")
