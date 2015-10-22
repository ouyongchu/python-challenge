import urllib2
import re

html = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/equality.html')
print ''.join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]',html))
