# import libraries
import urllib2
from bs4 import BeautifulSoup  
# specify the url
print("Above modi");
quote_page = 'https://twitter.com/narendramodi'
print("Below modi")  
# query the website and return the html to the variable 'page'
page = urllib2.urlopen(quote_page)  
print("Below url")
# parse the html using beautiful soap and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')  
#soup.prettify()
print("under")
# Take out the <div> of name and get its value
name_box = soup.findAll('div', attrs={'class': 'content'}) 
#name = name_box.text.strip() # strip() is used to remove starting and trailing  
for i in name_box:
	tweets = i.p.text
   	print("------->"+ tweets)    # print tweet 
   	tweet_details = i.div.text.strip()
   	print(tweet_details)  # print tweet details 
    	reply = i.findAll("span", {"class": "ProfileTweet-actionCount"})
    	reply2=reply[0].text  
    	print(reply2)    # print no of reply on tweet 
    	retweet =reply[1].text
    	print(retweet)    # print no of reweets
    	likes =reply[2].text

