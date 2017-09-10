import tweepy 
import csv
#Twitter API credentials
consumer_key = "IWSVC6OEOK41wPBtwJPNXQAT4"
consumer_secret = "8DOZOOmT2gQN3CVnQ0MCXghyif3m3R80AFQPSU2y5Fa5D2DX9K"
access_key = "4360002133-HIi8Mun9T1Ig61XcCKPGZBJIUsWQ5KR8q6OiGsc"
access_secret = "CtwLUfKqg8jl7LYuuOXD7vgJVfqJz9MKIeZ2XWrHKzOq0"


def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	#authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
    alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	
	#save most recent tweets
    alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print( "getting tweets before %s" % (oldest))
		
		#all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		
		#save most recent tweets
        alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
		
        print ("...%s tweets downloaded so far" % (len(alltweets)))
    #print( tweet )  # u can use tweet.text if u want to print only tweet not other features
    # i print latest 500 tweets a person whose i used as a screen_name or username u can print total tweets
	#or no of tweets according to your choice change range in given list
    barray = alltweets[0:500]  
    for tweet in barray:
     	print(tweet)
		
		
if __name__ == '__main__':
    get_all_tweets("MichelleObama") #pass in the username of the account you want to download I used "narendramodi". 
