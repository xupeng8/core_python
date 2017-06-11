#!/usr/bin/env python

import re

data = ('800-555-1212', '555-1212', '(800)555-1212')
patt = re.compile(r'(\d{3}-|\(\d{3}\))?\d{3}-\d{4}')
for d in data:
    m = re.match(patt, d)
    if m is not None:
        print(m.group())
    else:
        print('not match')
