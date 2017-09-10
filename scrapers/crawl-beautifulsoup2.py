# -*- coding: utf-8 -*-
# python 2

# from urllib import urlopen
import os
import shutil
import urllib
import urllib2
import urlparse
import time
import pprint
import sys
import lxml.html
from bs4 import BeautifulSoup # get html links

def processOneUrl(url):
	"""fetch URL content and update resultUrl."""
	try:                        # in case of 404 error
		html_page = urllib2.urlopen(url)
		soup = BeautifulSoup.BeautifulSoup(html_page)
		for link in soup.findAll('A'):
			fullurl = urlparse.urljoin(url, link.get('HREF'))
			if fullurl.startswith(inputURL):
				if (fullurl not in resultUrl):
					resultUrl[fullurl] = False
		resultUrl[url] = True       # set as crawled
	except:
		resultUrl[url] = True   # set as crawled

def moreToCrawl():
	"""returns True or False"""
	for url, crawled in iter(resultUrl.iteritems()):
		print url
		print crawled
		if not crawled:
			print "moreToCrawl found {}".format(url)
			return url
	return False




# craw a website, list all url under a specific given path

if len(sys.argv) < 3:
	print "usage: python crawl-healthcare.py <folderName> <url>"
	exit()

inputURL = sys.argv[2]
resultUrl = {inputURL:False}
print resultUrl
# key is a url we want. value is True or False. True means already crawled

docType = sys.argv[1]
if os.path.isdir(os.getcwd()+"/"+docType):
	shutil.rmtree(docType)
os.mkdir(docType)
curDir=os.getcwd()
os.chdir(curDir+"/"+docType)


while True:
	toCrawl = moreToCrawl()
	if not toCrawl:
		print "not to crawl"
		break
	aStr= str(toCrawl)
	arr = aStr.split("/")
	document = str(arr[len(arr)-1])
	f = open(document,'w')
	proxyhandler = urllib2.ProxyHandler({'http': 'http://10.10.78.61:3128'})
	opener = urllib2.build_opener(proxyhandler)
	try:
		opener.open(toCrawl)
	except urllib2.URLError, e:
		print e.code
		print e.read()
	urllib2.install_opener(opener)
	req = urllib2.Request(toCrawl)
	response = urllib2.urlopen(req)
	html = response.read()
	response.read()
	response.close()
	tree = lxml.html.fromstring(html)
	for e in tree.iter():
		if e.tag=="p" or e.tag=="h1":
			f.write(e.text_content().encode('utf8'))
			f.write('\n')
	f.close()
	processOneUrl(toCrawl)
	time.sleep(2)



#pprint.pprint(resultUrl)
