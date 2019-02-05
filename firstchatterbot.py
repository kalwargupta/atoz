#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 11:49:10 2019

@author: jeetu
"""

from chatterbot.trainers import ListTrainer # method to train the chatbot
from chatterbot import ChatBot # import the chatbot

bot = ChatBot('Test')

conv = open('chat.txt', 'r').readlines()

bot.set_trainer(ListTrainer) # set the trainer

bot.train(conv) # train the bot

while True:
	request = input('You: ')
	response = bot.get_response(request)

print('Bot: ', response)
