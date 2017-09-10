# import libraries
import urllib2  
from bs4 import BeautifulSoup  
import re

quote_page = 'https://en.wikipedia.org/wiki/Deep_Blue_%28chess_computer%29'  

page = urllib2.urlopen(quote_page).read()  

soup = BeautifulSoup(page)  
body = soup.body
all_texts = body.find_all("p")
for i in range(len(all_texts)):
		#print(all_texts[i])
		#all_links = all_texts[i].find_all("th")
		
		for text in all_texts:
		  	cleanr = re.compile('<.*?>')
  		  	all_texts[i] = re.sub(cleanr, '', str(all_texts[i]))
  		  	cleanr = re.compile('<script>.*?</script>')
  		  	all_texts[i] = re.sub(cleanr, '', str(all_texts[i]))
		print(all_texts[i])

