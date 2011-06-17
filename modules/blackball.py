#!/usr/bin/env python

blackball_data = []


def blackball(phenny, input, origin):
    """
    allow other users to 'blackball' users.
    If a user receives 3 blackballs, they are banned
    MODE #channel +b *!*@X._____.IP
    """
    if input.sender.startswith('#'): 
        return phenny.say('pm .blackball <username> to nominate someone anonymously for a blackball-style ban from the channel.')
    blackballee = input.group(2)
    blackballer = origin.host
    if not blackballee:
        return phenny.say('Who would you like to blackball?')
    blackballed_users = [x['nick'] for x in blackball_data]
    if blackballee not in blackballed_users:
        blackball_data.append({'nick' : blackballee,
                               'blackballed_by': [blackballer]
                               })
        ball_count = 1
    else:
        for user in blackball_data:
            if user['nick'] == blackballee:
                if blackballer in user['blackballed_by']:
                    return phenny.say('You may only blackball a user once.')
                user['blackballed_by'].append(blackballer)
                ball_count = len(user['blackballed_by'])
    phenny.say('Thank you. The user %s has been blackballed' % blackballee)
    print 'A user was blackballed'
    print 'ball count for user %s is %i' % (blackballee,
                                            ball_count)
blackball.commands = ['blackball']
blackball.priority = 'high'

