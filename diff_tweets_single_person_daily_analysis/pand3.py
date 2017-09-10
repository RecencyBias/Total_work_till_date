import re
str = open('pc3.txt', 'r').read()
#exampleString = "Jessica is 15 years old, and Daniel is 27 years old.Edward is 97 years old, and his grandfather, Oscar, is 102."
replies = re.findall(r'\d{1,6} replies',str)
str1 = ''.join(replies)
replies1 = re.findall(r'\d{1,6}',str1)
retweets = re.findall(r'\d{1,6} retweets',str)
str2 = ''.join(retweets)
retweets2 = re.findall(r'\d{1,6}',str2)

likes = re.findall(r'\d{1,6} likes',str)
str3 = ''.join(likes)
likes2 = re.findall(r'\d{1,6}',str3)
time = re.findall(r'\d{1,2} hours ago',str)
str4 = ''.join(time)
time2 = re.findall(r'\d{1,2}',str4)

#time = re.findall(r'[A-Z][a-z]*\s\d{1,2}',str)
#retweets = re.findall(r'[A-Z][a-z]*',exampleString)
intreplies = [int(numeric_string) for numeric_string in replies1]
intretweets = [int(numeric_string) for numeric_string in retweets2]
intlikes = [int(numeric_string) for numeric_string in likes2]
inttime = [int(numeric_string) for numeric_string in time2]
'''print(intreplies)
print(intretweets)
print(intlikes)
'''
print(inttime)
intreplies1 = intreplies[0:5]
intretweets2=intretweets[0:5]
intlikes2=intlikes[0:5] 
print(intreplies1)
print(intretweets2)
print(intlikes2)
#print(red)
'''/*list2 = []
for i in range(len(replies)):
    x = re.findall(r'\d{1,6}',replies[i])
    t = int(x)
    list2.append(t)

print list2
'''
'''
import matplotlib.pyplot as plt
#plt.plot(inttime,intreplies1) 
plt.bar(inttime,intreplies,label="Example one")
plt.show()
'''
import matplotlib.pyplot as plt
x=inttime
#labels=['','feb','mar','apr']
y=intlikes2
plt.bar(x,y, align='center',color='green',label="No of likes")
#plt.xticks(x, labels)
plt.xlabel('Number of hours ago tweet was posted')
plt.ylabel('Features(Likes, Retweets, Replies')

plt.title('Histogram depicting the relationship between popularity of media features and time')
plt.bar(x,intretweets2,color='yellow',label = "No of retweets")
plt.bar(x,intreplies1,color='blue',label = "No of replies")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
'''
y = np.random.rand(10,4)
y[:,0]= np.arange(10)
df = pd.DataFrame(y, columns=["X", "A", "B", "C"])

ax = df.plot(x="X", y="A", kind="bar")
df.plot(x="X", y="B", kind="bar", ax=ax, color="C2")
df.plot(x="X", y="C", kind="bar", ax=ax, color="C3")

plt.show()
list = ['1' , '2', '3']
list2 = []
for i in range(len(list)):
    t = int(list[i])
    list2.append(t)

print list2
'''
