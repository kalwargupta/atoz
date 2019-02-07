#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 14:41:47 2019

@author: jeetu
"""


import speech_recognition as sr

while True:
    r=sr.Recognizer()
    
    with sr.Microphone() as source:
        
        print ("say something")
        audio = r.listen(source)
        
        try:
            print("Text:" + r.recognize_google(audio))
        except sr.UnknownValueError:
            print("can not undersatand")


