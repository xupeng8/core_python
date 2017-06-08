#!/usr/bin/env python

import re

data = '118023092'
patt = re.compile(r'\d+')
m = re.match(patt, data)
if m is not None:
    print(m.group())
else:
    print('not match')
