#!/usr/bin/python3
"""A recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit"""

import requests


def recurse(subreddit, hot_list=[]):
    """returns the number of all hot articles of a given subreddit"""
    r = requests.get(r'https://www.reddit.com/r/{}/hot/.json'
                     .format(subreddit), headers={'User-agent': 'x'},
                     allow_redirects=False)
    if r.status_code == 200:
        data = r.json()['data']
        posts = data['children']
        count = len(posts)
        hot_list.extend(list(map(lambda x: x['data']['title'], posts)))
        if count >= limit and data['after']:
            return recurse(subreddit, hot_list, n + count, data['after'])
        else:
            return hot_list if hot_list else None
        else:
            return hot_list else None
