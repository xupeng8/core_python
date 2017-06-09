#!/usr/bin/env python

import re

data = ('10', '11', '12')
patt = re.compile(r'1[0-2]')
for d in data:
    m = re.match(patt, d)
    if m is not None:
        print(m.group())
    else:
        print('not match')
