#!/usr/bin/env python

import re

data = ('world.hello@google.com', '12345678@qq.com', 'hello_world@python.re',
        'www.baidu.com')
patt = re.compile(r'^[\w\._]*\w+@\w+.\w+$')
for d in data:
    m = re.match(patt, d)
    if m is not None:
        print(m.group())
    else:
        print('not match')
