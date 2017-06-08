#!/usr/bin/env python

import re

data = 'Eric Xu'
patt = re.compile(r'\w+ \w+')
print(re.match(patt,data).group())
