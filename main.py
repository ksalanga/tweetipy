import tweepy
import secrets
import pandas as pd
import numpy as np

consumer_key = secrets.consumer_key
consumer_secret = secrets.consumer_secret
access_token = secrets.access_token
access_token_secret = secrets.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


# Creating dataFrame to store tweets

timeline = api.user_timeline(count=1)

print(dir(timeline[0]))

# Find Content of Twitter Account




