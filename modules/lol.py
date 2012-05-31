#!/usr/bin/env python

import urllib
import web

def lol(phenny, input):
    main_input = input.group(2)
    if not main_input:
        return phenny.say('Give me something to translate!')
    url = 'http://speaklolcat.com/?from=%s' % urllib.quote(main_input)
    bytes = web.get(url)
    start = bytes.index('<div id="text">');
    start = bytes.index('</p>', start);
    start = bytes.index('<p>', start);
    start = start + 3
    end = bytes.index('</p>', start);
    phenny.say(bytes[start:end])

lol.commands = ['lol']
lol.example = '.lol'

if __name__ == '__main__':
    print __doc__.strip()
