#!/usr/bin/env python

import math

def d(a):
    sqrt_a = int(math.sqrt(a))
    sum = 1
    divisor = 2
    while divisor < sqrt_a:
        if a % divisor == 0:
            sum = sum + divisor + (a/divisor)
        divisor = divisor + 1
    return sum

def amicable(a):
    b = d(a)
    if d(b) == a and b != a:
        return b
    return 0


sum = 0
for a in range(10000):
    b = amicable(a)
    if b: sum = sum + a
    # we can add b but we need to keep state for that
    
print sum
