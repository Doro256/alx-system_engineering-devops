#!/usr/bin/python3
"""
function that queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts listed"""
    response = requests.get('https://www.reddit.com/r/{}/hot/.json'
                            .format(subreddit), headers={'User-agent': 'x'},
                            allow_redirects=False)
    if response.status_code == 200:
        for post in response.json()['data']['children'][0:10]:
            print(post['data']['title'])
    else:
        print(None)
