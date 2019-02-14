#!/usr/bin/python3
"""queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    user_agent = {'User-agent': 'damon'}
    req = requests.get('http://www.reddit.com/r/{}/top.json?limit=10'
                       .format(subreddit), headers=user_agent)
    try:
        sub = req.json().get('data')
        child = sub.get('children')
        for l in child:
            data = l.get('data')
            for k, v in data.items():
                if k == 'title':
                    print(v)
    except:
        return (0)
