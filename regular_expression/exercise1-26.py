#!/usr/bin/env python

import re

MY_EMAIL = 'hello.world@google.com'

with open('redata.txt', 'r') as f:
    patt = re.compile(r'\w{4,8}@\w{4,13}.\w{3}')
    count = 0
    for line in f:
        m = re.subn(patt, MY_EMAIL, line)
        if m is not None:
            print(m)
            count += m[1]
    if count:
        print('%d email replaced' % count)
