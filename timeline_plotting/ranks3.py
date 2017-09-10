import matplotlib.pyplot as plt
import numpy as np
time = [60,52,16,60,12,5,60,24,24]
replies = [0,357,0,0,0,7,20,1,69]
retweets = [16,625,4,110,0,34,2000,14,62]
likes = [15,1100,2,8,2,72,3100,16,59]
ranks = [1,2,3,4,5,6,7,8,9]
plt.bar(ranks,time, align='center',color='green',label="No of likes")
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
