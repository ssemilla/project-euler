#!/usr/bin/env python

# Brute force

import utils

def rotations(n):
    n = str(n)
    out = []
    for i in range(1, len(n)):
        out.append(int(n[i:] + n[:i]))
    return out

prime = utils.sieve_arr(1000000)

total = 0
for i in xrange(len(prime)):
    if prime[i]:
        rotates = rotations(i)
        if not [prime[n] for n in rotates].count(False):
            total = total + 1

print total
