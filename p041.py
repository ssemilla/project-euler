#!/usr/bin/env python

# we only need to check n=7 and n=7 pandigital numbers since all others
# have sums divisible by 3

# let us just try n=7, if we find a prime pandigital, we don't need
# to check for n=4

from itertools import permutations as perm
import utils

prime = utils.sieve_arr(7654322)

largest = 0
for p in perm('1234567'):
    n = int(''.join(p))
    if prime[n] and n > largest:
        largest = n

print largest        
