#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from urllib.request import urlopen

url_prefix = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
url = url_prefix + '63579'
num_pat = re.compile('([0-9]+)')

while True:
	res = urlopen(url).read().decode('utf-8').strip()
	try:
		num = num_pat.search(res).group(1)
	except Exception:
		print(res)
		break
	url = url_prefix + num
