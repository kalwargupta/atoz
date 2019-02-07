#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 09:35:24 2019

@author: jeetu
"""
from textblob import TextBlob
text= TextBlob("he is gret preon")
corText=text.correct()
print (corText.detect_language())
tamil= corText.translate(from_lang="en" , to="ta")
hindi= corText.translate(from_lang="en" , to="hi")
#nepali= corText.translate(from_lang="en" , to="np")
chinese= corText.translate(from_lang="en" , to="zh-CN")
arabi= corText.translate(from_lang="en" , to="ar")
print (tamil + "/n")
print (hindi + "/n")
print (chinese + "/n")
print (arabi + "/n")



import PyPDF2

pdfFileObj = open('file.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

print(pdfReader.numPages)

pageObj = pdfReader.getPage(0)

print(pageObj.extractText())

pdfFileObj.close()



from nltk import word_tokenize
string=""
sentence ="helllo my name is jeetu kumar gupta"
tokens=word_tokenize(sentence)
print(tokens)
crtWords=[]
for i in range(len(tokens)):
    print(tokens[i])

for w in range(len(tokens)):
    text=TextBlob(tokens[w])
    crtText=text.correct()
    crtWords.append(crtText)
print (crtWords)




