from TwitterClient import TwitterClient
import tweepy
import secrets

consumer_key = secrets.consumer_key
consumer_secret = secrets.consumer_secret
access_token = secrets.access_token
access_token_secret = secrets.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

friends = []
likes = []
tweets = []

if __name__ == "__main__":
    api = tweepy.API(auth, wait_on_rate_limit=True)
    # tweepy.debug(True)
    # twitter_client = TwitterClient()
    # twitter_client.get_following(name='')

    print("Recent Posts")

    # Returns a list of statuses
    timeline = api.user_timeline(count=10)
    print(dir(timeline))
    for tweet in timeline:
        print(dir(tweet))
        print(tweet.text)

    # Returns a list of statuses
    print("Recent Likes")
    # print(api.favorites())

    print(api.rate_limit_status())
    # print(twitter_client.get_api().rate_limit_status())
