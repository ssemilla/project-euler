#!/usr/bin/env python

from itertools import permutations

total = 0
for p in permutations('0123456789'):
    p = ''.join(p)
    if int(p[1:4]) % 2 == 0 and\
       int(p[2:5]) % 3 == 0 and\
       int(p[3:6]) % 5 == 0 and\
       int(p[4:7]) % 7 == 0 and\
       int(p[5:8]) % 11 == 0 and\
       int(p[6:9]) % 13 == 0 and\
       int(p[7:10]) % 17 == 0:
        total = total + int(p)
        
print total
       




