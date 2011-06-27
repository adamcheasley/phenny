#!/usr/bin/env python
"""
This module requires textmining to be installed:
http://pypi.python.org/pypi/textmining
"""
import textmining
import operator
from datetime import datetime
from datetime import timedelta
from string import letters


chat_data = []
ignored_words = [u'hello', u'botston', u'nick', u'sweet', u'skip', u'arent', u'remeber', 
                 u'cool', u'tunk', u'desk', u'innit',  ]
last_chat = datetime.now()


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
    global last_chat
    last_chat = datetime.now()

get_chat.rule = r'(.*)'
get_chat.priority = 'low'


def chat(phenny, input):
    """
    tells the user who has been chatting and about what
    """
    # get main users
    user_count = {}
    raw_chat = []
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
        raw_chat.append(data['chat'])
    # sort the dict
    sorted_users = sorted(user_count.iteritems(), key=operator.itemgetter(1))
    sorted_users.reverse()
    # if there's less than 2 users chatting
    if len(sorted_users) < 2:
        return phenny.say("No one's been chatting that much")
    # if the chat was more than an hour ago.
    if datetime.now() < last_chat - timedelta(hours=1):
        return phenny.say("No one's been chatting recently")

    phenny.say('Users %s and %s have been chatting mostly' % (
            sorted_users[0][0], sorted_users[1][0]))
    
    # look through for unusual words
    all_words = set()
    interesting_words = []
    rare_words = []
    for chat in raw_chat:
        chat_list = chat.split()
        for s_word in chat_list:
            all_words.add(s_word)

    # at this point we're going to have to do some pretty expensive checking
    # each word for punctuation and non-letters
    all_words = [x for x in all_words if not x.startswith(':')]
    all_real_words = set(all_words)
    for word in all_words:
        expanded_word = [x for x in word]
        for letter in expanded_word:
            if letter not in letters:
                try:
                    all_real_words.remove(word)
                except KeyError:
                    continue
        if word.lower() in ignored_words \
                or len(word) < 4 or len(word) > 25:
            try:
                all_real_words.remove(word)
            except KeyError:
                continue
    
    # create a tuple of all words and their frequency and a list of 
    # all dicitonary words
    freq_word = [(counts[0][0], word) for (word, counts) in \
                     textmining.dictionary.items()]
    freq_word.sort(reverse=True)
    dictionary_words = [x[1] for x in freq_word]
    for posted_word in all_real_words:
        for word in freq_word:
            if posted_word == word[1] and word[0] < 6000:
                interesting_words.append(posted_word)
        if posted_word.lower() not in dictionary_words:
            rare_words.append(posted_word)

    # format the words and post them to the channel
    if not interesting_words:
        return phenny.say(
            'They\'ve not been talking about anything interesting'
            )
    if interesting_words:
        message = 'They have been talking about:'        
        for word in interesting_words[:5]:
            message = message + ' ' + word
        phenny.say(message)
    if interesting_words and rare_words:
        message = 'They have also been chatting about:'
        for word in rare_words[:5]:
            message = message + ' ' + word
        phenny.say(message)

chat.commands = ['chat']
chat.priority = 'low'

