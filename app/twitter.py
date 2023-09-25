import tweepy
from app.pickupline import pickupline_str
import os

bearer_token = os.environ.get("X_BEARER_TOKEN")
api_key = os.environ.get("X_API_KEY")
api_secret = os.environ.get("X_API_SECRET")
access_token = os.environ.get("X_ACCESS_TOKEN")
access_token_secret = os.environ.get("X_ACCESS_TOKEN_SECRET")


client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuthHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)


def sendTweet():

    client.create_tweet(text=f"{pickupline_str}\n#Trending #pickuplines")

    print("Tweet posted successfully")

