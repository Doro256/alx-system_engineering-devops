#!/usr/bin/python3
"""A recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit"""

import requests


def recurse(subreddit, hot_list=[]):
    """returns the number of all hot articles of a given subreddit"""
    response = requests.get('https://www.reddit.com/r/{}/hot/.json'
                            .format(subreddit), headers={'User-agent': 'x'},
                            allow_redirects=False)
    ml = response.json().get('data').get('children')
    if response.status_code != 200:
        return None
    # return [subreddit] + hot_list
    if hot == []:
        return None
    else:
        k = hot[0]
        small_list = hot[1:]
        return k + recurse(small_list)
