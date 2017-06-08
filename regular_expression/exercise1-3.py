#!/usr/bin/env python

import re

data = 'Eric,X'
patt = re.compile(r'(\w+)[ ,](\w+)')
print(re.match(patt,data).groups())
