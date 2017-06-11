#!/usr/bin/env python

import re

week_count = {'Mon':0, 'Tue':0, 'Wed':0, 'Thu':0, 'Fri':0, 'Sat':0, 'Sun':0}

with open('redata.txt', 'r') as f:
    for line in f:
        for week in week_count:
            week_count[week] += line.split().count(week)

for week in week_count:
    print('count of %s is %d'  % (week, week_count[week]))
