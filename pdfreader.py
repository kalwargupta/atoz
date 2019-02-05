#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 13:50:56 2019

@author: jeetu
"""
#importing the library
import PyPDF2

#opening the pdf file in binary format
#making file object
pdfFileObj=open("file.pdf", "rb")

#Reading the pdf file with file object
#making pdf reader oject
pdfReader=PyPDF2.PdfFileReader(pdfFileObj)

#print the number of pages a file
print (pdfReader.numPages)

#getting the text data from page 3
pageObj=pdfReader.getPage(3)

#printing the extracted text
print (pageObj.extractText())

pdfFileObj.close()