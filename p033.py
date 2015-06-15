#!/usr/bin/env python

from itertools import permutations as perm
from fractions import gcd
import operator

digits = range(1, 10)

curious = []

for a in perm(range(1, 10), 2):
    for b in perm(range(1, 10), 2):
        a_int = a[0]*10 + a[1]
        b_int = b[0]*10 + b[1]

        if a_int / b_int < 1:
            
            if a[0] == b[0] and a_int*b[1] == b_int*a[1]:
                curious.append((a_int, b_int))
            if a[0] == b[1] and a_int*b[0] == b_int*a[1]:
                curious.append((a_int, b_int))
            if a[1] == b[0] and a_int*b[1] == b_int*a[0]:
                curious.append((a_int, b_int))
            if a[1] == b[1] and a_int*b[0] == b_int*a[0]:
                curious.append((a_int, b_int))

num = reduce(operator.mul, [c[0] for c in curious], 1)
den = reduce(operator.mul, [c[1] for c in curious], 1)

print den / gcd(num, den)
