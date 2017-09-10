import urllib2 
from bs4 import BeautifulSoup as soup
quote_page = "https://twitter.com/" 
# query the website and return the html to the variable 'page'
page = urllib2.urlopen(quote_page)  
page_soup = soup(page, "html.parser")
#tweets=page_soup.findAll("p",{"class":"TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"}) # no of tweets 20 stored in tweets...
""" tweets[0].text
    tweets[1].text
	we get tweets using it"""

"""for tweet in tweets:
    print("--> "+ (tweet.text))
    comment="""
prat=page_soup.findAll("div", {"class":"content"})
# prac=prat[0]
"""filename = "tweetslist.csv"
f = open(filename, "w")    #open file in write mode
headers = "tweet, tweet_details, reply2, reweet, like\n"
f.write(headers)"""
for prac in prat:
    tweets = prac.p.text
    print("------->"+ tweets)    # print tweet 
    tweet_details = prac.div.text.strip()
    print(tweet_details)  # print tweet details 
    reply = prac.findAll("span", {"class": "ProfileTweet-actionCount"})
    reply2=reply[0].text  
    print(reply2)    # print no of reply on tweet 
    retweet =reply[1].text
    print(retweet)    # print no of reweets
    likes =reply[2].text
    print(likes)      #print no of likes
	
   # f.write(tweets + "," + tweet_details + "," + reply2 + "," + retweet + "," + likes + "\n")
#f.close()	
