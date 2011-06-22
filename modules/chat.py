#!/usr/bin/env python

import operator


chat_data = []


def get_chat(phenny, input):
    """
    records the chat
    """
    raw_chat = input
    channel = input.sender
    user = input.nick
    # do not record the command itself
    if raw_chat == u'.chat':
        return

    if len(chat_data) > 50:
        chat_data.pop(0)
    data = {'user' : user,
            'channel' : channel,
            'chat' : raw_chat
            }
    chat_data.append(data)

get_chat.rule = r'(.*)'
get_chat.priority = 'low'


def chat(phenny, input):
    """
    tells the user who has been chatting and about what
    """
    # get main users
    user_count = {}
    channel = input.sender
    for data in chat_data:
        # only look at the channel the command was sent from
        if data['channel'] != channel:
            continue
        user = data['user']
        if user not in user_count.keys():
            user_count[user] = 1
        else:
            user_count[user] += 1
    # sort the dict
    sorted_users = sorted(user_count.iteritems(), key=operator.itemgetter(1))
    sorted_users.reverse()
    if len(sorted_users) < 2:
        return phenny.say("No one's been chatting that much")    
    phenny.say('Users %s and %s have been chatting mostly' % (
            sorted_users[0][0], sorted_users[1][0]))
#     phenny.say('They have been talking about %s' % chat_data)

chat.commands = ['chat']
chat.priority = 'low'

