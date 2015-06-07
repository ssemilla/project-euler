#!/usr/bin/env python

from math import sqrt

num = 600851475143
limit = int(sqrt(num))

i = 2
ans = 1
while i <= limit:
    if num % i == 0:
       ans = i
       num = num / ans
    else:
        # we don't need a primality test
        i = i + 1

print ans
