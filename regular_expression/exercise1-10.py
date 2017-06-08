#!/usr/bin/env python

import re

data = '-1.1+2.1j'
patt = re.compile(r'-?\d+(\.\d+)?[+-]\d+(\.\d+)?[jJ]')
m = re.match(patt, data)
if m is not None:
    print(m.group())
else:
    print('not match')
