#!/usr/bin/env python

from math import sqrt

P = [0]*1001

for a in xrange(1, 500):
    for b in xrange(1, a):
        c = int(sqrt((a*a) + (b*b)))
        if (c*c) == (a*a) + (b*b):
            p = a + b + c
            if p < 1001:
                P[p] = P[p] + 1

largest = 0
for p in xrange(1001):
    if P[p] > P[largest]:
        largest = p

print largest        
