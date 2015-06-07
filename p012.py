#!/usr/bin/env python

import math

def divisors(n):
    root = int(math.sqrt(n))
    count = 0
    for i in xrange(1,root+1):
        if n % i == 0:
            count = count + (i == root and 1 or 2)
    return count

nth = 1
triangle = 1
while divisors(triangle) <= 500:
    nth = nth + 1
    triangle = triangle + nth

print triangle    
