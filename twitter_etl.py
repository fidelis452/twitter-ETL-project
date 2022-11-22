import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs

access_key = '5k0JJavNTEAYOIMU278ExBFhp'
access_secret =  'nVfXQeqzI5Tjbiu70cB3z8ISaLQYunFouZFT2KXprtcGIl1581'
consumer_key = '1182938294616809477-5owmLZKCTayXMzsWozL16jFFZonw1o'
consumer_secret = 'NyljaFueTlI3C9Yp11pD1Wm6hVjVKEW9QQPSoRxhXjJE0'

#twitter authentication
auth = tweepy.OAuthHandler(access_key, access_secret)
auth.set_access_token(consumer_key, consumer_secret)

# creaing api object
api = tweepy.API(auth)

tweets = api.user_timeline(screen_name ='@elonmusk',
count=200,  
include_rts=False,
tweet_mode = 'extended'
)

# store the tweets in a list
tweet_list = []
for tweet in tweets:
    text = tweet._json["full_text"]

    refined_tweet = {
        'user': tweet.user.screen_name,
        'text': text,
        'favorite_count': tweet.favorite_count,
        'retweet_count': tweet.retweet_count,
        'created_at': tweet.created_at
        }

    tweet_list.append(refined_tweet)

    df = pd.DataFrame(tweet_list)
    df.to_csv("elonmusk_twitter_data.csv")
# print(tweets)