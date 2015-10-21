#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Caesar cipher, wikipedia

import string

low_letters = sting.lowercase
table = string.maketrans(low_letters,low_letters[:2]+low_letters[:2])

text = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. 
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''

print text.translate(table)
print 'map'.translate(table)
