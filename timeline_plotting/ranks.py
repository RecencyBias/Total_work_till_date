import matplotlib.pyplot as plt
import numpy as np
time = [1,5,2,2,5,5,2,6,7,7,0.5,7]
replies = [109,37,483,79,121,23000,672,409,416,405,42,32]
retweets = [244,57,3200,155,254,15000,1800,810,71,8300,124,106]
likes = [575,203,18000,328,1100,56000,1600,5600,460,28000,194,1100]
ranks = [1,2,3,4,5,6,7,8,9,10,11,12]
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
