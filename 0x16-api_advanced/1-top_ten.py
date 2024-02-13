#!/usr/bin/python3
"""Top ten"""
import requests


headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0\
        Safari/537.36'}

def top_ten(subreddit):
    """ returns the top ten hot posts"""


    if subreddit is None or type(subreddit) is not str:
        print(None)
        return
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)