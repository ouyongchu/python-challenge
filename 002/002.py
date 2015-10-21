#!/usr/bin/env python
# -*- coding: utf-8 -*-
#find the rare characters
#a.txt is a file containing the raw text

f = "".join(open('a.txt','r').readlines()).replace('\n','')
d = {}
rare = set()
answer = []
for i in f:
    for j in i:
        d[j]=d.get(j,0)+1
for i in d:
    if d[i] < 10:
        rare.add(i)
for i in f:
    if i in rare:
        answer.append(i)
print ''.join(answer)
