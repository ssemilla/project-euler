#!/usr/bin/env python

from math import factorial

def C(n, r):
    return factorial(n) / (factorial(r) * factorial(n-r))

total = 0    
for n in range(1, 101):
    for r in range(1, n):
        if C(n, r) > 1000000:
            total = total + 1

print total
