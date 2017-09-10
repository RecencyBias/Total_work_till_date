import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#This may not work if you do not have chromedriver.
#Get it from here: 
#https://sites.google.com/a/chromium.org/chromedriver/home  
#Copy the executable file into the PATH folder.

browser = webdriver.Chrome()
#opens an automated browser window

url = 'https://twitter.com/narendramodi'

browser.get(url)
#opens the url in the browser

body = browser.find_element_by_tag_name('body')
for i in range(5):
	body.send_keys(Keys.PAGE_DOWN)
	time.sleep(0.2)
#moves the page down by 5 page down scrolls

tweets = browser.find_element_by_class_name('tweet-text')
#finds elements by class name of the tweets

for tweet in tweets:
	print(tweet)

browser.close()
#closes the browser window
