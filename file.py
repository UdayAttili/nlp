# -*- coding: utf-8 -*-
import nltk
import string
import re
from nltk import ngrams
from nltk.corpus import reuters
from collections import Counter
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
from random import *
from random import shuffle
st = StanfordNERTagger('stanford-ner/classifiers/english.muc.7class.distsim.crf.ser.gz', 'stanford-ner/stanford-ner.jar', encoding='utf-8')

with open('doc.txt', 'r') as input:
	text = input.read()
   # no_punctuation = text.translate(str.maketrans('','',string.punctuation))

f = open("questionPaper.txt","w+")
qn=0
seperated = re.split(r'(?<=\w\.)\s', text)
for i in seperated:
	a = i
	tokens = nltk.word_tokenize(a)
	tagged = nltk.pos_tag(tokens)
	str1 = ''.join(a)
	#print (str1)
	classified_text = st.tag(tokens)
	#print(classified_text)
#	print(tagged)
	#for word,tag in tagged:
	#	if tag == 'NNP':
	#		s = str1.replace(word, 'what')
	#		s = s.replace('.', '?')
	#		print (s)
	#		print ("Ans: ",word)
	v=0
	k=0
	for word,tag in classified_text:
		
		if word == 'by':
			v=1
		if word == 'at':
			k = 1
		if tag == 'PERSON':
			
			if v==1:
				s = str1.replace(word, 'whom')
			else:
				s = str1.replace(word, 'who')
			s = s.replace('.', '?')
			f.write (str(qn+1)+') ')
			qn = qn + 1
			f.write(s)
			f.write ('\n')
			count = 1
			options = []
			while (count!=4):
				
				load_profile = open('person.txt', "r")
				x = randint(1, 4945)
				read_it = load_profile.read().splitlines()[x]
				options.append(read_it)
				count=count+1
			options.append(word)
			shuffle(options)
			count = 0
			while (count!=4):
				f.write (str(count+1)+' ')
				f.write(options[count])
				f.write ('\n')
				count=count+1
		if tag == 'ORGANIZATION':
			s = str1.replace(word, 'which')
			s = s.replace('.', '?')
			f.write (str(qn+1)+') ')
			qn = qn + 1
			f.write(s)
			f.write ('\n')
			count = 1
			options = []
			while (count!=4):
				
				load_profile = open('organisation.txt', "r")
				x = randint(1, 111)
				read_it = load_profile.read().splitlines()[x]
				options.append(read_it)
				count=count+1
			options.append(word)
			shuffle(options)
			count = 0
			while (count!=4):
				f.write (str(count+1)+' ')
				f.write(options[count])
				f.write ('\n')
				count=count+1
		if tag == 'LOCATION':
			options = []
			count = 1
			if k==1:
				s = str1.replace(word, '')
				print (k)
			else:
				s = str1.replace(word, ' which country')
			s = s.replace('.', '?')
			f.write (str(qn+1)+') ')
			qn = qn + 1
			f.write(s)
			f.write ('\n')
			while (count!=4):
				load_profile = open('location.txt', "r")
				x = randint(1, 195)
				read_it = load_profile.read().splitlines()[x]
				options.append(read_it)
				count=count+1
			options.append(word)
			shuffle(options)
			count = 0
			while (count!=4):
				f.write (str(count+1)+' ')
				f.write(options[count])
				f.write ('\n')
				count=count+1
		if tag == 'DATE':
			options = []
			count = 1
			s = str1.replace(word, 'the year')
			s = s.replace('.', '?')
			f.write (str(qn+1)+') ')
			qn = qn + 1
			f.write(s)
			f.write ('\n')
			while (count!=4):
				load_profile = open('location.txt', "r")
				x = randint(1, 10)
				read_it = int(word)+x
				options.append(read_it)
				count=count+1
			options.append(word)
			shuffle(options)
			
			count = 0
			while (count!=4):
				f.write (str(count+1)+' ')
				f.write(str(options[count]))
				f.write ('\n')
				count=count+1