#!/usr/bin/env python

import re

data = 'hat'
patt = re.compile(r'[bh][aiu]t')
print(re.match(patt,data).group())
