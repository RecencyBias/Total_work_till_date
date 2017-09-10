import scrapy
import urllib2
import urllib
from scrapy.spiders import BaseSpider
from scrapy.selector import Selector
from scrapy.http.request import Request
from scrapy.http.response import Response
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
import re
import csv
#start_urls = search_url
#start_urls=['http://www.flipkart.com/rosra-c1-analog-watch-couple-men-women-boys-girls/p/itmef43d6hdnmv2q']
#hxs = Selector(response)
#hxs.select(".//a[@class='fk-display-block']/text()").extract()
class amazoncom(scrapy.Spider):
    search_q = raw_input("Enter what you want to search with quotations:")
    search_q= search_q.replace(" ", "+")
    search_url="http://www.amazon.com/s/?field-keywords="+search_q
    print search_url
    name = "amazoncom"		
    allowed_domains = ['amazon.com']
    start_urls = [search_url]
    #def __init__(self):
	#super(Flipkart, self)
    #def spider_closed(self, spider):
	#pass
    fo=open("reviews_amazoncom.csv","w+")
    fo.write("Rating,Date,Review\n")
    fo.close()
    def parse(self, response):
        #hxs = Selector(response)
        hxs=Selector(response)
        links = hxs.xpath(".//a[@class='a-link-normal s-access-detail-page  a-text-normal']/@href").extract()
        link=links[0]
        print "\n The link to go is:\n\n"
        print link
        print "\n\n\n ^^^The link to go"
        request = scrapy.Request(link,callback=self.parse_review)
        #-------------------------request.meta['item'] = item
        yield request
    def parse_review(self, response):
        hxs = Selector(response)
        #item = response.meta['item']
        newlinks= hxs.xpath(".//div[@class='a-fixed-left-grid-col a-col-left']/a[@class='a-link-emphasis a-nowrap']/@href").extract()
        newlink=newlinks[0]
        print newlink
        request = scrapy.Request(newlink,callback=self.parse_review2)
        yield request

    def parse_review2(self, response):
        hxs = Selector(response)
        review_elements=hxs.xpath(".//span[@class='a-size-base review-text']").extract()
        review_rating=hxs.xpath(".//div[@class='a-section review']/div[@class='a-row']/a[@class='a-link-normal']/i/span/text()").extract()
        #--date of posting can be found from next line
        review_date=hxs.xpath(".//div[@class='a-section review']/div[@class='a-row']/span[@class='a-size-base a-color-secondary review-date']/text()").extract()
        #--review_date=hxs.xpath(".//div[@class='line']/div[@class='date']/text()").extract()
        tmp1=0
        
        for review_element in review_elements:
            review_element=review_element.replace("<br>", "")
            review_element=review_element.replace('<span class="a-size-base review-text">', "")
            review_element=review_element.replace("</span>", "")
            review_element=review_element.replace("\n", "")
            #review_element=review_element.replace("\u2019", "")
            #review_element=unicode(review_element, errors='ignore')
            review_element=review_element.encode('utf-8')
            #type()
            #print tmp1
            #print review_element
            #print review_rating[tmp1]
            #print "----------------------------------------------------"
            #with open('C:\Users\HP\Desktop\Skybits\\a\\flipkart\\flipkart\Extracted_Reviews\\reviews_amazoncom.csv', 'w') as f:
            #    c = csv.writer(f)
            #writerow=review_rating[tmp1]+","+review_element+"\n"
            fo=open("reviews_amazoncom.csv","a")
            fo.write(review_rating[tmp1].replace("out of 5 stars", "")+",")
            fo.write((review_date[tmp1].replace("on", "")).replace("\n", "")+",")
            fo.write(review_element)
            fo.write("\n")
            tmp1=tmp1+1

        next_page_link = hxs.xpath(".//ul[@class='a-pagination']/li[@class='a-last']/a/@href").extract()
        #next_page_link=next_prev_page[1]
        k=len(next_page_link)-1
        #print "THE LINK TO NEXT PAGE IS:"
        next_page_go_link= "http://amazon.com"+next_page_link[k]
        if next_page_go_link: # check if there is a next page at all
            yield Request(next_page_go_link, callback=self.parse_review2)
#Flipkart()