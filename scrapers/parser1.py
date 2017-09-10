import urllib2
import re
from bs4 import BeautifulSoup
from nltk.corpus import wordnet
from nltk import word_tokenize
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from collections import Counter 
def parse(url):
	headers = { 'User-Agent' : 'Mozilla/5.0' }
	req = urllib2.Request(url, None, headers)		
	data = urllib2.urlopen(req).read()

	data = BeautifulSoup(data)
	body = data.body
	all_texts = body.find_all("p")
	#print(all_texts[1])
	#all_texts = all_texts[0]
	#print(all_texts)
	#print(len(all_texts))
	text1 = ""
	for i in range(len(all_texts)):
		#print(all_texts[i])
		all_links = all_texts[i].find_all("a")
		
		for links in all_links:
		  	cleanr = re.compile('<.*?>')
  		  	all_texts[i] = re.sub(cleanr, '', str(all_texts[i]))
  		  	cleanr = re.compile('<script>.*?</script>')
  		  	all_texts[i] = re.sub(cleanr, '', str(all_texts[i]))
		#print(all_texts[i])
		text1 = text1 + str(all_texts[i])
	cleanr = re.compile('<.*?>')
	text1 = re.sub(cleanr, '', str(text1))
	#print
	#print(text)

	#print(data)
	#print(data.title.string)
	#print(data.h1.string)
	h = '\d{1,4}'
	hs = re.findall(h,str(data.string))
	#print(hs)
	#print(data.h2.string)
	#print(data.p.string)
	#print(data.body)
	data = data.body.get_text
	data = re.sub('<.*?>', '', str(data))
	data = re.sub('(\\t*\\n*)*', '	', str(data))
	data = re.sub('(\\n*\\t*)*', '', str(data))
	data = str(data).replace("\t","")
	data = data.replace("\n","")
	f = open("parser1.txt","w")
	f.write(data)
	f.close()
	#print(data)

	words = word_tokenize(data)

	#print(words)

	fin_list1 = []
	for word in words:
		if wordnet.synsets(word):
			fin_list1.append(word)
		
	#print(fin_list1)

	lemmatizer = WordNetLemmatizer()
	fin_lits1 = [lemmatizer.lemmatize(token) for token in fin_list1]

	stop_words = set(stopwords.words('english'))

	fin_list = []

	for word in fin_list1:
		if word not in stop_words:
			fin_list.append(word)
	text = " ".join(fin_list)
	return text1
'''

tf = []


tf = Counter(fin_list)

total = 0

print(tf)

for key,value in tf.iteritems():
	total = total + value
	
print(total)


for key,value in tf.iteritems():
	tf[key] = value/float(total)
	
print(tf)

total = 0

text = " ".join(fin_list)

texts=Counter(text.split())

vocab_inv = {x[0] for x in texts.most_common()}
vocab = {x: i for i,x in enumerate(vocab_inv)}
#print(vocab)
for key,value in vocab.iteritems():
	total = total + value
	
print(total)

datas = nltk.pos_tag(fin_list)
datas =  nltk.ne_chunk(datas, binary=True)

#print(datas)
'''