import tweepy as tp
from tweepy.auth import OAuthHandler
import time

# variables....
consumerKey = "n0hiTaJkhUAFyycYQDy6wzUzO"
consumerSecretKey = "6F3yg5eEmc0fGL2tTtgmFNgUiYC5iaqjH7jOpGzDWaHjiZtJqq"
# accessing
AccessKey = "1244614920945229824-k9yBJNJzf3uoUoowrQst6Usd5ZmpNi"
AccessSecretKey = "m6ymwcxuiYdtzm0S5UCCAzUn0efgFJlnUU2rovNkPInt8"
# Globalizes
hasTag = "#100DaysOfCode"
dateFrom = "2020-4-12"
no_of_tweets = "1"

# authentications API
auth = OAuthHandler(consumerKey, consumerSecretKey)
auth.set_access_token(AccessKey, AccessSecretKey)
auth.secure = True

api = tp.API(auth, wait_on_rate_limit=True)
user = api.me()


# Collect tweets
# cursor method used to avoid old iteration method for user authentication pages

# basic retweet method

def reTweet():
    for tweet in tp.Cursor(api.search, q=hasTag).items(no_of_tweets):
        try:
            tweet.retweet()
            time.sleep(10)
        except tp.TweepError as e:
            print(e.reason)
        except StopIteration:
            break


reTweet()
