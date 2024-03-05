#!/usr/bin/python3
"""
This module queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """Return the top ten of a sub reddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"limit": 10}
    headers = {"User-Agent": "MyRedditBot/1.0 (fily)"}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get("data")
        for post in data.get("children")[:10]:
            print(post.get("data").get("title"))
    else:
        print("None")
