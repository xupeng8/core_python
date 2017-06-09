#!/usr/bin/env python

import re

data = ('110102233445566', '2202011223344556', '1101-022334-45566', 
        '2202-0112-2334-4556')
patt = re.compile(r'\d{4}-\d{4}-\d{4}-\d{4}|\d{4}-\d{6}-\d{5}|\d{15,16}')
for d in data:
    m = re.match(patt, d)
    if m is not None:
        print(m.group())
    else:
        print('not match')
