#!/usr/bin/env python

import re

data = ('https://www.baidu.com:80', 'http://baidu.com',
        'http://tieba.baidu.com/p/5152311507?pid=107895607306&cid=0#107895607306',
        'www.baidu.com', 'baidu.org', 'localhost:8080/index.html',
        '192.168.1.1:8080/index.html',
        'http://news.qq.com/a/20170609/002204.htm',
        '12345678@qq.com')
patt = re.compile(r'''(?ix)
                  ^
                  (?:https?://)?                           # http:// or https://
                  ((?:(?:\w(?:[A-Z0-9-]{0,61}\w)?\.)+[A-Z]{2,6}) | #domain name
                      localhost |                        # localhost
                      \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})  # ip
                  (?::\d+)?                                #optional port
                  (?:/?|/\S+)
                  $
                  ''')
for d in data:
    m = re.match(patt, d)
    if m is not None:
        print(m.group())
    else:
        print('not match')
