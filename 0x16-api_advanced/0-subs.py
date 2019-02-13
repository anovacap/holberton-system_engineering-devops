#!/usr/bin/python3
"""function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given
subreddit.If an invalid subreddit is given, the function should return 0 """
import requests


def number_of_subscribers(subreddit):
    user_agent = {'User-agent': 'damon'}
    req = requests.get('http://www.reddit.com/r/{}/about.json'
                       .format(subreddit), headers=user_agent)
    try:
        sub = req.json().get('data')
        for k, v in sub.items():
            if k == 'subscribers':
                return (v)
    except:
        return (0)
