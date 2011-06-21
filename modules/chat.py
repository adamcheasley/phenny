#!/usr/bin/env python

chat_data = []


def get_chat(phenny, input):
    """
    records the chat
    """
    raw_chat = input
    # do not record the command itself
    if raw_chat == u'.chat':
        return
    if len(chat_data) > 50:
        chat_data.pop(0)
    chat_data.append(raw_chat)

get_chat.rule = r'(.*)'
get_chat.priority = 'low'


def chat(phenny, input):
    """
    tells the user who has been chatting and about what
    """
    phenny.say('Well')
    phenny.say('People have been talking about %s' % chat_data)

chat.commands = ['chat']
chat.priority = 'low'

