#!/usr/bin/env python

import re

with open('redata.txt', 'r') as f:
    patt = re.compile(r'^(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) ([0-9 ][0-9]) \d{2}:\d{2}:\d{2} (\d{4})')
    for line in f:
        m = re.sub(patt, r'\1,\2,\3', line)
        if m is not None:
            print(m, end='')
