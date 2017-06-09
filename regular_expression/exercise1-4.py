#!/usr/bin/env python

import re

data = '_hello_world_123'
patt = re.compile(r'\b[a-zA-Z_][\w_]+\b')
print(re.match(patt,data).group())
