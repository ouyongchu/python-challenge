#!/usr/bin/env python
# -*- coding: utf-8 -*-
#find the rare characters
#a.txt is a file containing the raw text

with open('a.txt','r') as fd:
    data = ''.join([_.rstrip() for _ in fd])
    freq = {}
    for _ in data:
        freq[_] = freq.get(_,0) + 1
    avg_freq = len(data) // len(freq)
    print(''.join([_ for _ in data if freq[_] < avg_freq]))
