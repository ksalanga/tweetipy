from TwitterClient import TwitterClient

if __name__ == "__main__":
    twitter_client = TwitterClient()
    api = twitter_client.get_api()

    print(api.rate_limit_status())
