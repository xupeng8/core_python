#!/usr/bin/env python

import re

data = '123.45'
patt = re.compile(r'\d+(\.\d+)?')
m = re.match(patt, data)
if m is not None:
    print(m.group())
else:
    print('not match')
