#!/usr/bin/python3
""" function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    returns the number of subscribers for a given subreddit
    """
    response = requests.get(
        'https://www.reddit.com/r/{}/about.json'
        .format(subreddit),
        headers={'User-agent': 'x'},
        allow_redirects=False)

    if response.status_code != 200:
        return 0

    return response.json()['data']['subscribers']
