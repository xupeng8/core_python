#!/usr/bin/env python

import re

data = '118023092L'
patt = re.compile(r'\d+[lL]')
m = re.match(patt, data)
if m is not None:
    print(m.group())
else:
    print('not match')
