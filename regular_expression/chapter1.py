#!/usr/bin/env python

import re
data = 'Thu Mar  4 19:00:21 1971::rkoote@fnsxpltxbm.net::36932421-6-10'

print('using pattern' + '^(Mon|Tue|Wed|Thu|Fri|Sat|Sun)')
patt = re.compile(r'^(Mon|Tue|Wed|Thu|Fri|Sat|Sun)')
m = re.match(patt, data)
if m is not None:
    print(m.group())
    print(m.groups())
print()

print('using pattern' + '^(\w{3})')
patt = re.compile(r'^(\w{3})')
m = re.match(patt, data)
if m is not None:
    print(m.group())
    print(m.groups())
print()

print('using pattern' + '.+(\d+-\d+-\d+)')
patt = re.compile(r'.+(\d+-\d+-\d+)')
m = re.match(patt, data)
m = re.match(patt, data)
if m is not None:
    print(m.group())
    print(m.groups())
print()

print('using pattern' + '.+?(\d+-\d+-\d+)')
patt = re.compile(r'.+?(\d+-\d+-\d+)')
m = re.match(patt, data)
m = re.match(patt, data)
if m is not None:
    print(m.group())
    print(m.groups())
print()
