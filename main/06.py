#!/usr/bin/env python
# -*- coding: utf-8 -*-

# zipfile获取每个member的comment信息拼接

import re
import zipfile

num_pat = re.compile('Next nothing is (\d+)')
file = zipfile.ZipFile('channel.zip')
f = '%s.txt'
n = '90052'
c_list = []
while True:
	try:
		n = num_pat.search(file.read(f % n)).group(1)
	except Exception:
		print(file.read(f % n))
		break
	c_list.append(file.getinfo(f % n).comment)
print(''.join(c_list))
