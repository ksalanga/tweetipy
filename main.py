import tweepy
import secrets
import pandas as pd
import numpy as np
import requests
import json

consumer_key = secrets.consumer_key
consumer_secret = secrets.consumer_secret
access_token = secrets.access_token
access_token_secret = secrets.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

x = {
  "web": {
    "client_id": "",
    "client_secret": "",
    "redirect_uris": [""],
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://accounts.google.com/o/oauth2/token",
    "YOUR_API_KEY": ""
  }
}

# print(type(x))
#
# print(x["web"]["auth_uri"])
r = requests.get('https://api.github.com/events')

# 13865345225
# print(r.json()[0]['id'])
# Creating dataFrame to store tweets

timeline = api.user_timeline(count=20)


print(type(timeline))
# print(timeline)


for tweet in timeline:
    print(tweet.text)
# Find Content of Twitter Account

"""
Crawl through the Twitter Account's Friends (Who they are following), and if we have a match from the direct account name, search Spotify API.
"""

# following = api.friends(screen_name='asapmoutis', count=100)
# print(following)

# for status in tweepy.Cursor(api.user_timeline).items(1):
#     print(status.text)


# retrieves the friends of the specific user
for friend in tweepy.Cursor(api.friends, screen_name='').items(1):
  print(friend)

#
# i = 1
# for user in following:
#     print(f'{i}) {user.screen_name}\n')
#     i += 1


