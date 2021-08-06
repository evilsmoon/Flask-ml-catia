import nltk
import numpy as np
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import re

######
def lowercase(sentence):
  for i,temp in enumerate(sentence):
      sentence[i] = temp.lower()
  return sentence
###### 
def deleteChars(sentence):
  for i,temp in enumerate(sentence):
     sentence[i] = re.sub('[^A-Za-záéíóúñ]+',' ',temp)
  return sentence
###### 
def tokenizertext(sentence):
  for i,temp in enumerate(sentence):
    sentence[i]= temp.split()
  return sentence
###### 
def stopWords(sentence,cont):
  c = 0
  sw = stopwords.words('spanish')
  if cont>0:
    for word in sentence:
      for i in word:
        if i in sw:
          word.remove(i)
          c +=1
    stopWords(sentence,c)
  else:
    print()
  return sentence
######
def stemmer(tit):
  st = SnowballStemmer('spanish')
  for i in tit:
    for x,h in enumerate(i):
      i[x]=st.stem(h)
  return tit




