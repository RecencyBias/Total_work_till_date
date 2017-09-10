import tweepy
from tweepy import OAuthHandler
 
consumer_key = 'lbRtZs1L0MBJx4LyelfKi8Wzc'
consumer_secret = ' TTWDKtYDMYjBdD8g0yuIdew8vMPkDUUSg1tFAWK80xVPNBWH6m'
access_token = ' 4214565200-wbYjEuKDU65L5PHoXPZMicUuhEvhbulRuVUNAgJ'
access_secret = 'Y1RVzp05UfnOZvX9hDOXl5Gf7zRTR9FgWcSaXLYZflpXC'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status.text)
