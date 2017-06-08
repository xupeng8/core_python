#!/usr/bin/env python

import re

data = 'HelloWorld123'
patt = re.compile(r'\b[a-zA-Z_]\w+\b')
print(re.match(patt,data).group())
