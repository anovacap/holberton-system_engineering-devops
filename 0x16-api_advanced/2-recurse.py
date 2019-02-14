#!/usr/bin/python3
"""a recursive function that queries the Reddit API,
parses the title of all hot articles, and prints a
sorted count of given keywords """
import requests


def recurse(subreddit, hot_list=[], after=""):
    user_agent = {'User-agent': 'damon'}
    url = 'http://www.reddit.com/r/{}/hot.json?limit=100&after={}'
    req = requests.get(url.format(subreddit, after), headers=user_agent)
    try:
        sub = req.json().get('data')
        child = sub.get('children')
        for d in child:
            hot_list.append(d.get('title'))
        after = sub.get('after')
        if 'after' in sub and after is not None:
            return(recurse(subreddit, hot_list, after))
        else:
            return (hot_list)
    except:
        return(None)
