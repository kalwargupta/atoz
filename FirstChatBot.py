#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 17:08:46 2019

@author: jeetu
"""



from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot=ChatBot("test")
conv=open("chat.txt","r").readlines()

trainer=ListTrainer(bot)
trainer.train(conv)

while True:
    request = input("you: ")
    response=bot.get_response(request)
    print("Bot: ", response)