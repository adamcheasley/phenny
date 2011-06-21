#!/usr/bin/env python

chat_data = []


def chat(phenny, input):
    """
    tells the user who has been chatting and about what
    """
    phenny.say('working')

chat.commands = ['chat']
chat.priority = 'high'


