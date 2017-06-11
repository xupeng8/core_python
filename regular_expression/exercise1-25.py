#!/usr/bin/env python

import re

with open('redata.txt', 'r') as f:
    patt = re.compile(r'.*::(\w{4,8})@(\w{4,13}).(\w{3})::.*')
    for line in f:
        m = re.match(patt, line)
        if m is not None:
            print(m.groups())
