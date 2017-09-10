import re
str = open('pc1.txt', 'r').read()
#exampleString = "Jessica is 15 years old, and Daniel is 27 years old.Edward is 97 years old, and his grandfather, Oscar, is 102."
replies = re.findall(r'\d{1,6} replies',str)
str1 = ''.join(replies)
replies1 = re.findall(r'\d{1,6}',str1)
retweets = re.findall(r'\d{1,6} retweets',str)
str2 = ''.join(retweets)
retweets2 = re.findall(r'\d{1,6}',str2)
days = re.findall(r'Aug\s\d{1,2}|Jul\s\d{1,2}',str)
strday = ''.join(days)
days1 = re.findall(r'\d{1,2}',strday)
intdays = [int(numeric_string) for numeric_string in days1]
likes = re.findall(r'\d{1,6} likes',str)
str3 = ''.join(likes)
likes2 = re.findall(r'\d{1,6}',str3)
time = re.findall(r'\d{1,2}h',str)
str4 = ''.join(time)
time2 = re.findall(r'\d{1,2}',str4)
#print days
#print days1
#print intdays
intnewdays = [abs(11-i)*24 for i in intdays]
for i in intdays:
	if((11-i)  > 0):
		j = (11-i)*24
		intnewdays.append(j)
	else:
		j = abs(11-31)*24+(31-i)*24
		intnewdays.append(j)

		
#print intnewdays
intnewdays = intnewdays[0:5]
#print intnewdays
#time = re.findall(r'[A-Z][a-z]*\s\d{1,2}',str)
#retweets = re.findall(r'[A-Z][a-z]*',exampleString)
intreplies = [int(numeric_string) for numeric_string in replies1]
intretweets = [int(numeric_string) for numeric_string in retweets2]
intlikes = [int(numeric_string) for numeric_string in likes2]
inttime = [int(numeric_string) for numeric_string in time2]
inttime=inttime+intnewdays
print inttime
'''print(intreplies)
print(intretweets)
print(intlikes)

print(inttime)
'''

intreplies1 = intreplies[0:10]
intretweets2=intretweets[0:10]
intlikes2=intlikes[0:10] 
inttime1=inttime[0:10]

print(len(intreplies1))
print(len(intretweets2))
print(len(intlikes2))
print(len(inttime1))
print(intreplies1)
print(intretweets2)
print(intlikes2)
print(inttime1)

import matplotlib.pyplot as plt
x=inttime1
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
import numpy
#a = numpy.array([[1,2],[3,4],[5,6]])
numpy.savetxt("pc.csv",zip(inttime,intreplies,intlikes,intretweets), delimiter=',', header="Time,Replies,Likes,Retweets", comments="")
import re
str = open('pc.txt', 'r').read()
#exampleString = "Jessica is 15 years old, and Daniel is 27 years old.Edward is 97 years old, and his grandfather, Oscar, is 102."
replies = re.findall(r'\d{1,6} replies',str)
str1 = ''.join(replies)
replies1 = re.findall(r'\d{1,6}',str1)
retweets = re.findall(r'\d{1,6} retweets',str)
str2 = ''.join(retweets)
retweets2 = re.findall(r'\d{1,6}',str2)
days = re.findall(r'Aug\s\d{1,2}|Jul\s\d{1,2}',str)
strday = ''.join(days)
days1 = re.findall(r'\d{1,2}',strday)
intdays = [int(numeric_string) for numeric_string in days1]
likes = re.findall(r'\d{1,6} likes',str)
str3 = ''.join(likes)
likes2 = re.findall(r'\d{1,6}',str3)
time = re.findall(r'\d{1,2} hours ago',str)
str4 = ''.join(time)
time2 = re.findall(r'\d{1,2}',str4)
#print days
#print days1
#print intdays
intnewdays = [abs(11-i)*24 for i in intdays]
for i in intdays:
	if((11-i)  > 0):
		j = (11-i)*24
		intnewdays.append(j)
	else:
		j = abs(11-31)*24+(31-i)*24
		intnewdays.append(j)

		
#print intnewdays
intnewdays = intnewdays[0:5]
#print intnewdays
#time = re.findall(r'[A-Z][a-z]*\s\d{1,2}',str)
#retweets = re.findall(r'[A-Z][a-z]*',exampleString)
intreplies = [int(numeric_string) for numeric_string in replies1]
intretweets = [int(numeric_string) for numeric_string in retweets2]
intlikes = [int(numeric_string) for numeric_string in likes2]
inttime = [int(numeric_string) for numeric_string in time2]
inttime=inttime+intnewdays
print inttime
'''print(intreplies)
print(intretweets)
print(intlikes)

print(inttime)
'''

intreplies1 = intreplies[0:10]
intretweets2=intretweets[0:10]
intlikes2=intlikes[0:10] 
inttime1=inttime[0:10]

print(len(intreplies1))
print(len(intretweets2))
print(len(intlikes2))
print(len(inttime1))
print(intreplies1)
print(intretweets2)
print(intlikes2)
print(inttime1)

import matplotlib.pyplot as plt
x=inttime1
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
import numpy
#a = numpy.array([[1,2],[3,4],[5,6]])
numpy.savetxt("pc.csv",zip(inttime,intreplies,intlikes,intretweets), delimiter=',', header="Time,Replies,Likes,Retweets", comments="")

