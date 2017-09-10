import matplotlib.pyplot as plt
import numpy as np
time = [46,7,29,18,8,27,35,29,24,6,16,3,47,21,16,24,50,31,35,40,31,18,39,13,29,25,46,41]
replies = [1,4,0,123,60,0,123,60,0,120,25,71,0,0,0,12,0,17,32,0,63,59,0,1,77,5,10,6,79,63]
retweets = [7,9,62,1,309,6,7,347,20,219,0,3,1,32,3,28,135,9,202,96,9,15,127,16,109,13,219,253]
likes = [10,46,4,0,1100,70,5,1500,58,841,0,7,2,224,10,134,458,13,854,303,16,28,162,44,143,73,697,1200]
ranks = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
plt.bar(ranks,time, align='center',color='green',label="No of likes")
print len(time)
print len(retweets)
print len(likes)
print len(ranks)
plt.xlabel('The number at which it appeared on timeline')
plt.ylabel('Green = Hours, Red = Replies, cyan = likes ,yellow = retweets')
plt.show()
#plt.xticks(x, labels)
plt.bar(ranks,replies,align = 'center',color='red')
plt.xlabel('The number at which it appeared on timeline')
plt.ylabel('Green = Hours, Red = Replies, cyan = likes ,yellow = retweets')
plt.show()
plt.bar(ranks,retweets,align = 'center',color = 'yellow')
plt.xlabel('The number at which it appeared on timeline')
plt.ylabel('Green = Hours, Red = Replies, cyan = likes ,yellow = retweets')
plt.show()
plt.bar(ranks,likes,align ='center',color = 'cyan')
plt.xlabel('The number at which it appeared on timeline')
plt.ylabel('Green = Hours, Red = Replies, cyan = likes ,yellow = retweets')
plt.show()
