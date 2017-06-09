#!/usr/bin/env python

import re

data = ('<type \'int\'>', '<type \'float\'>', '<type \'builtin_function_or_method\'>')
patt = re.compile(r'<type \'(\w+)\'>')
for d in data:
    m = re.match(patt, d)
    if m is not None:
        print(m.groups()[0])
    else:
        print('not match')
