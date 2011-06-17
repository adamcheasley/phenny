#!/usr/bin/env python

blackball_data = []


def blackball(phenny, input):
    """
    allow other users to 'blackball' users.
    If a user receives 3 blackballs, they are banned
    MODE #channel +b *!*@X._____.IP
    """
    if input.sender.startswith('#'): 
        return phenny.say('pm .blackball <username> to nominate someone anonymously for a blackball-style ban from the channel.')
    blackballee = input.group(2)
    blackballer = input.sender
    if not blackballee:
        return phenny.say('Who would you like to blackball?')
    blackballed_users = [x['nick'] for x in blackball_data]
    if blackballee not in blackballed_users:
        blackball_data.append({'nick' : blackballee,
                               'blackballed_by': [blackballer]
                               })
    else:
        for user in blackball_data:
            if user['nick'] == blackballee:
                user['blackballed_by'].append(blackballer)
                ball_count = len(user['blackballed_by'])
    phenny.reply('Thank you. The user %s has been blackballed' % blackballee)
    print 'A user was blackballed'
    print 'ball count for user %s is %i' % (blackballee,
                                            ball_count)
blackball.commands = ['blackball']
blackball.priority = 'high'

