import re
str = open('obama.txt', 'r').read()
#exampleString = "Jessica is 15 years old, and Daniel is 27 years old.Edward is 97 years old, and his grandfather, Oscar, is 102."
replies = re.findall(r'\d{1,6} replies',str)
str1 = ''.join(replies)
replies1 = re.findall(r'\d{1,6}',str1)		
retweets = re.findall(r'\d{1,6} retweets',str)
str2 = ''.join(retweets)
retweets2 = re.findall(r'\d{1,6}',str2)
augdays = re.findall(r'Aug\s\d{1,2}',str)
juldays = re.findall(r'Jul\s\d{1,2}',str)
jundays = re.findall(r'Jun\s\d{1,2}',str)
maydays = re.findall(r'May\s\d{1,2}',str)
aprdays = re.findall(r'Apr\s\d{1,2}',str)
#print aprdays
augdays = ''.join(augdays)
juldays = ''.join(juldays)
jundays = ''.join(jundays)
maydays = ''.join(maydays)
aprdays = ''.join(aprdays)

augdays1 = re.findall(r'\d{1,2}',augdays)
juldays1 = re.findall(r'\d{1,2}',juldays)
jundays1 = re.findall(r'\d{1,2}',jundays)
maydays1 = re.findall(r'\d{1,2}',maydays)
aprdays1 = re.findall(r'\d{1,2}',aprdays)
augdates = [int(numeric_string) for numeric_string in augdays1]
juldates = [int(numeric_string) for numeric_string in juldays1]
jundates = [int(numeric_string) for numeric_string in jundays1]
maydates = [int(numeric_string) for numeric_string in maydays1]
aprdates = [int(numeric_string) for numeric_string in aprdays1]
print augdates
print juldates
print jundates
print maydates
print aprdates
finaldate = []
for i in augdates:
	finaldate.append(13-i)
for i in juldates:
	if(13-i > 0):
		finaldate.append(30+13-i)
	elif(13-i < 0):
		finaldate.append(30 - abs(13-i))
for i in jundates:
	if(13-i > 0):
		finaldate.append(30*2+13-i)
	elif(13-i < 0):
		finaldate.append(30*2 -abs(13-i))
for i in maydates:
	if(13-i > 0):
		finaldate.append(30*3+13-i)
	elif(13-i < 0):
		finaldate.append(30*3-abs(13-i))
for i in aprdates:
	if(13-i > 0):
		finaldate.append(30*4+13-i)
	elif(13-i < 0):
		finaldate.append(30*4-abs(13-i))
	
print finaldate
'''strday = ''.join(days)0
days1 = re.findall(r'\d{1,2}',strday)
intdays = [int(numeric_string) for numeric_string in days1]
print intdays'''
likes = re.findall(r'\d{1,6} likes',str)
str3 = ''.join(likes)
likes2 = re.findall(r'\d{1,6}',str3)
'''time = re.findall(r'\d{1,2} hours ago',str)
str4 = ''.join(time)
time2 = re.findall(r'\d{1,2}',str4)

#print days
#print days1
#print intdays
intnewdays = []
for i in 
for i in intdays:
	if((13-i)  > 0):
		j = 13-i
		intnewdays.append(j)
	else:
		j = abs(13-31)+13-i
		intnewdays.append(j)

		
print intnewdays
#intnewdays = intnewdays[0:5]
#print intnewdays
#time = re.findall(r'[A-Z][a-z]*\s\d{1,2}',str)
'''
#retweets = re.findall(r'[A-Z][a-z]*',exampleString)
intreplies = [int(numeric_string) for numeric_string in replies1]
intretweets = [int(numeric_string) for numeric_string in retweets2]
intlikes = [int(numeric_string) for numeric_string in likes2]
#inttime = [int(numeric_string) for numeric_string in time2]
#inttime=inttime+intnewdays
#print inttime

print(intreplies)
print(intretweets)
print(intlikes)

print(finaldate)


intreplies1 = intreplies[0:16]
intretweets2=intretweets[0:16]
intlikes2=intlikes[0:16] 
#inttime1=intnewdays[0:10]
'''
print(len(intreplies1))
print(len(intretweets2))
print(len(intlikes2))
print(len(inttime1))
print(intreplies1)
print(intretweets2)
print(intlikes2)
print(inttime1)
'''
import matplotlib.pyplot as plt
x=finaldate
#labels=['','feb','mar','apr']
y=intlikes2
plt.bar(x,y, align='center',color='green',label="No of likes")
#plt.xticks(x, labels)
plt.xlabel('Number of days ago tweet was posted')
plt.ylabel('Features(Likes = green, Retweets=yellow, Replies=blue)')

plt.title('Histogram depicting the relationship between popularity of media features and time')
plt.bar(x,intretweets2,color='yellow',label = "No of retweets")
plt.bar(x,intreplies1,color='blue',label = "No of replies")
plt.show()
import numpy
#a = numpy.array([[1,2],[3,4],[5,6]])
numpy.savetxt("pc.csv",zip(inttime,intreplies,intlikes,intretweets), delimiter=',', header="Time,Replies,Likes,Retweets", comments="")


