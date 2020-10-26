import tweepy
import secrets

consumer_key = secrets.consumer_key
consumer_secret = secrets.consumer_secret
access_token = secrets.access_token
access_token_secret = secrets.access_token_secret


class TwitterClient():
    def __init__(self):
        twitter_authenticator = TwitterAuthenticator()
        self.auth = twitter_authenticator.get_auth()
        self.twitter_client = tweepy.API(self.auth)

    def get_api(self):
        client = self.twitter_client
        return client


class TwitterAuthenticator():
    def __init__(self):
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)

    def get_auth(self):
        return self.auth


"""
Retrieve Twitter Account's Tweets
"""

# /friends/list
# for friend in tweepy.Cursor(api.friends, screen_name='').items(300):
#     print(friend)

"""
Retrieve Twitter Account's Followers
"""

