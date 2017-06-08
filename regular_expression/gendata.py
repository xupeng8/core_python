#!/usr/bin/env python

'''
generate random text for re tests
'''

from random import randrange, choice
from string import ascii_lowercase as lc
from time import time, ctime

tlds = ('com', 'edu', 'net', 'org', 'gov')

for i in range(randrange(5, 11)):
    dtint = randrange(int(time()))
    dtstr = ctime(dtint)
    llen = randrange(4, 8)
    login = ''.join(choice(lc) for j in range(llen))
    dlen = randrange(llen, 13)
    dom = ''.join(choice(lc) for j in range(dlen))
    print('%s::%s@%s.%s::%d-%d-%d' % ( dtstr, login, dom, choice(tlds), dtint,
        llen, dlen) )
