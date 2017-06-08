#!/usr/bin/env python

import re

data = 'www.google.com'
patt = re.compile(r'^www\.\w+\.com$')
m = re.match(patt, data)
if m is not None:
    print(m.group())
else:
    print('not match')

data = 'http://www.foothill.edu'
patt = re.compile(r'^\w{4}://[\w+\.]+[edu|org|com|cn|net]$')
m = re.match(patt, data)
if m is not None:
    print(m.group())
else:
    print('not match')
