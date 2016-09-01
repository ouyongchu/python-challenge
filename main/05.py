#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
from urllib.request import urlopen

url = 'http://www.pythonchallenge.com/pc/def/banner.p' 
res = urlopen(url).read().strip()
data = pickle.loads(res)
for elt in data:
    print("".join([e[1] * e[0] for e in elt]))
