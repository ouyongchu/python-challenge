#!/usr/bin/env python
# -*- coding: utf-8 -*-

#To see the solutions to the previous level, replace pc with pcc, i.e. go to: http://www.pythonchallenge.com/pcc/def/ocr.html
#经测试，http://www.pythonchallenge.com/是通过cookie而非Referer来验证当前用户是否具有访问答案URL的权限的
#比如根据当前问题的URL：http://www.pythonchallenge.com/pc/def/ocr.html
#得到访问上一关答案的URL:http://www.pythonchallenge.com/pcc/def/ocr.html
#最后请求答案URL：http://wiki.pythonchallenge.com/index.php?title=Level1:Main_Page时
#只要附上请求当前问题URL时的cookie头部，就有访问权限，前提是两次访问均在同一进程执行

import cookielib
import urllib2

cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie)) 

pre_url = 'http://www.pythonchallenge.com/pcc/def/ocr.html'
answer_url = 'http://wiki.pythonchallenge.com/index.php?title=Level1:Main_Page'

opener.open(pre_url)

for item in cookie:
    name = item.name
    value = item.value
    print name,value

request = urllib2.Request(url)
request.add_header('cookie','='.join([name,value]))

print urllib2.urlopen(request).read() 
