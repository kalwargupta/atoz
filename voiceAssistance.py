#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 17:47:45 2019

@author: jeetu
"""

import speech_recognition as sr
import os


while True:
    r=sr.Recognizer()
    
    with sr.Microphone() as source:
        audio=r.listen(source)
        
        try:
            filename="draft.txt"
            f=open(filename,"a+")
            
            recognized_text = r.recognize_google(audio)
            print (recognized_text)
            remainder= recognized_text.split()
            while remainder:
                line,remainder=remainder[:5], remainder[5:]
                f.write(" ".join(line) + "\n")
                
            if recognized_text=="bye":
                break
            if recognized_text=="Directory":
                print (os.makedirs("jeetu"))
                break
        
        
        except sr.UnknownValueError:
            print ("Google could not understand")
        
        except sr.RequestError as e:
            print("Google error; (0)".format(e))