#!/usr/bin/env python
"""
ping.py - Phenny Ping Module
Author: Sean B. Palmer, inamidst.com
About: http://inamidst.com/phenny/
"""

import random


def hello(phenny, input): 
   greeting = random.choice(('Hi', 'Hey', 'Hello',
                             'yo', 'word up', 'what up', 
                             'sup', 'yeah'))
   punctuation = random.choice(('', '!'))
   phenny.say(greeting + ' ' + input.nick + punctuation)
hello.rule = r'(?i)(hi|hello|hey|yo|sup) $nickname\b'


def interjection(phenny, input): 
   phenny.say(input.nick + '!')
interjection.rule = r'$nickname!'
interjection.priority = 'high'
interjection.thread = False


def greeting(phenny, input):
   greeting = random.choice(('Hi', 'Welcome', 'Good day', 'Nice to see you',
                             'Hello', 'Yo'))
   phenny.say('%s %s' % (greeting, input.nick))
greeting.event = 'JOIN'
greeting.rule = r'.*'


if __name__ == '__main__': 
   print __doc__.strip()
