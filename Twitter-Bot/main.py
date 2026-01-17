import tweepy
from time import sleep
from credentials import *
from config import QUERY, FOLLOW, LIKE, SLEEP_TIME

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

print("Twitter Bot Started")
print("Hashtag:", QUERY)
print("Like Tweets:", LIKE)
print("Follow Users:", FOLLOW)

for tweet in tweepy.Cursor(api.search, q=QUERY).items():
    try:
        print(f"\nTweet by: @{tweet.user.screen_name}")

        tweet.retweet()
        print("Retweeted")

        if LIKE:
            tweet.favorite()
            print("Liked")

        if FOLLOW and not tweet.user.following:
            tweet.user.follow()
            print("Followed user")

        sleep(SLEEP_TIME)

    except tweepy.TweepError as e:
        print("Error:", e.reason)

    except StopIteration:
        break
