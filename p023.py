#!/usr/bin/env python

# Damn, I can't see the trick for this one
# this is a brute force solution

from utils import sum_divisors

MAX = 28123

universe = [True]*MAX
abundant = [ n for n in xrange(1, MAX) if sum_divisors(n) > n ]

i = 0
abundant_len = len(abundant)
while i < abundant_len:
    j = i
    while j < abundant_len:
        sum = abundant[i] + abundant[j]
        if sum >= MAX:
            break
        else:
            universe[sum] = False
        j = j + 1
    i = i + 1

i = 0
sum = 0
while i < MAX:
    if universe[i]: sum = sum + i
    i = i + 1

print sum
