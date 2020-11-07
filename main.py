from TwitterClient import TwitterClient

if __name__ == "__main__":
    twitter_client = TwitterClient()
    twitter_client.get_following(name='')

    # i = 1
    # for friend in friends:
    #     print(f"{i}) {friend}")
    #     i += 1

    # following = twitter_client.get_following(count=2)
    #
    # print(type(following))
    # for follower in following:
    #     print(type(follower))
    #     print(follower)
    #     print(follower.name)

    print(twitter_client.get_api().rate_limit_status())
