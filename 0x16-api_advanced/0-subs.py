#!/usr/bin/python3
"""0 subs"""
import requests

headers = {"User-Agent": "MyCustomUserAgent/1.0"}


def number_of_subscribers(subreddit):
    """ returns the number of subscribers"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers)
    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0
