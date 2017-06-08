#!/usr/bin/env python

import re

data = '1180 De La Cruz Drive'
patt = re.compile(r'^(\w+ )+\w+$')
m = re.match(patt, data)
if m is not None:
    print(m.group())
else:
    print('not match')
