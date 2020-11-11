import tweepy
import secrets
import sqlite3

consumer_key = secrets.consumer_key
consumer_secret = secrets.consumer_secret
access_token = secrets.access_token
access_token_secret = secrets.access_token_secret


class TwitterClient:
    def __init__(self):
        tweepy.debug(True)
        twitter_authenticator = TwitterAuthenticator()
        self.auth = twitter_authenticator.get_auth()
        self.twitter_client = tweepy.API(self.auth, wait_on_rate_limit=True)

    def get_api(self):
        client = self.twitter_client
        return client

    # Retrieve Twitter Account's Followers
    def get_following(self, name=''):
        client = self.twitter_client
        following_results = tweepy.Cursor(client.friends, screen_name=name, count=200).pages()
        # Each page returns a list of what you requested (in this case: users).

        for list_of_users in following_results:
            for user in list_of_users:
                pass

    def get_tweets(self, name=''):
        client = self.twitter_client
        client.user_timeline()
        pass

    def get_favorites(self, name=''):
        client = self.twitter_client
        client.favorites()
        pass

    # get a list of what a user retweeted.
    def get_retweets(self, name=''):
        pass

    '''Brainstorming'''
    # handling the rate limit, we can sleep(60*15)
    # implement a database that can store already existing users/tweets


class TwitterAuthenticator:
    def __init__(self):
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)

    def get_auth(self):
        return self.auth


"""
Retrieve Twitter Account's Tweets
"""

