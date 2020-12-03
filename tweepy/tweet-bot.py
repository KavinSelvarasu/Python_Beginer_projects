import tweepy as tp
from tweepy.auth import OAuthHandler
import time
import sys

# variables....
consumerKey = "n0hiTaJkhUAFyycYQDy6wzUzO"
consumerSecretKey = "6F3yg5eEmc0fGL2tTtgmFNgUiYC5iaqjH7jOpGzDWaHjiZtJqq"
# accessing
AccessKey = "1244614920945229824-k9yBJNJzf3uoUoowrQst6Usd5ZmpNi"
AccessSecretKey = "m6ymwcxuiYdtzm0S5UCCAzUn0efgFJlnUU2rovNkPInt8"
# Globalizes
hasTag = "#100DaysOfCode"
dateFrom = "2020-10-12"

auth = OAuthHandler(consumerKey, consumerSecretKey)
auth.set_access_token(AccessKey, AccessSecretKey)
auth.secure = True

api = tp.API(auth, wait_on_rate_limit=True)


# Collect tweets
# cursor method used to avoid old iteration method for user authentication pages

def collectData():
    tweets = tp.Cursor(api.search,
                       q=hasTag,
                       lang="en",
                       since=dateFrom).items(5)

    # Iterate and print tweets
    for tweet in tweets:
        print(tweet)


collectData()
