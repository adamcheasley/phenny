#!/usr/bin/env python
"""
seen.py - Phenny Seen Module
Copyright 2008, Sean B. Palmer, inamidst.com
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""

import time
import pickle
from tools import deprecated


@deprecated
def f_seen(self, origin, match, args): 
   """.seen <nick> - Reports when <nick> was last seen."""
   if origin.sender == '#talis': return
   nick = match.group(2)
   if not nick: 
      return self.msg(origin.sender, 'Seen who?')
   nick = nick.lower()   
   if not hasattr(self, 'seen'): 
      return self.msg(origin.sender, '?')
   if self.seen.has_key(nick): 
      channel, t = self.seen[nick]
      t = time.strftime('%H:%M (UTC) %d/%m/%Y', time.localtime(t))

      msg = "I last saw %s at %s on %s" % (nick, t, channel)
      self.msg(origin.sender, str(origin.nick) + ': ' + msg)
   else: self.msg(origin.sender, "Sorry, I haven't seen %s around." % nick)
f_seen.rule = (['seen'], r'(\S+)')


@deprecated
def f_note(self, origin, match, args): 
   def note(self, origin, match, args):
      if not hasattr(self.bot, 'seen'):
         try:
            seen_file = open('seen.pkl', 'rb')
         except IOError:
            seen_data = {}
         else:
            try:
               seen_data = pickle.load(seen_file)
            except EOFError:
               seen_data = {}
            seen_file.close()
         self.bot.seen = seen_data
      if origin.sender.startswith('#'):
         seen_file = open('seen.pkl', 'wb')
         self.seen[origin.nick.lower()] = (origin.sender, time.time())
         pickle.dump(self.seen, seen_file)
         
      seen_file.close()

   try: note(self, origin, match, args)
   except Exception, e: print e
f_note.rule = r'(.*)'
f_note.priority = 'low'


if __name__ == '__main__': 
   print __doc__.strip()
