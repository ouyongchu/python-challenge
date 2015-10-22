#re.findall
#1.当匹配模式含有单个括号，则返回括号内容的列表
#2.当匹配模式含有多个括号，则返回多个括号内容组成元祖的列表
#3.当不含括号，则返回整个匹配的字符串

import urllib2
import re

html = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/equality.html')
print ''.join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]',html))
